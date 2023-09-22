#!/usr/bin/env python3
# Import datasets to Elasticsearch or logstash instance

from argparse import ArgumentParser
from pathlib import Path
import tarfile
import zipfile
import json
import progressbar
import sys
from termcolor import colored

progressbar.streams.wrap_stdout()

argparser = ArgumentParser(description="Import datasets into Elasticsearch or Logstash")
argparser.add_argument("--output", "-o", default="elasticsearch", help="Choose Elasticsearch or Logstash as output")
argparser.add_argument("--recursive", "-r", action="store_true", help="Recurse into directories")
argparser.add_argument("--url", "-u", default="http://localhost:9200", help="URL of Elasticsearch instance (%(default)s) or Logstash")
argparser.add_argument("--cacerts", "-c", default=None, help="Path to CA certificates for TLS verification")
argparser.add_argument("--insecure", "-I", default=True, action="store_false", dest="verify_certs", help="Don't verify TLS cerificates.")
argparser.add_argument("--index", "-i", default="winlogbeat-mordor", help="Target index for data import (%(default)s)")
argparser.add_argument("--no-index-creation", "-n", action="store_false", dest="create_index", help="Don't create index.")
argparser.add_argument("inputs", nargs="+", type=Path, help="Path to dataset")
args = argparser.parse_args()

if args.output == "elasticsearch":
    #Only import ES module when required
    from elasticsearch import Elasticsearch
    from elasticsearch.helpers import bulk

    print("Initializing Elasticsearch connection and index...")
    index = args.index
    es = Elasticsearch(
            [args.url],
            ca_certs=args.cacerts,
            verify_certs=args.verify_certs,
            )
    if  args.create_index:
        es.indices.create(
                index=index,
                body= { "settings": { "index.mapping.total_fields.limit": 2000 } }
            )
elif args.output == "logstash":
    #Only import requests when logstash is used
    import requests

    print("Initializing Logstash connection...")
    logstash_url = args.url
    if args.verify_certs and args.cacerts:
        verify_certs = args.cacerts
    elif not args.verify_certs:
        from urllib3.exceptions import InsecureRequestWarning
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        verify_certs = False
    else:
        verify_certs = True
else:
    print("Output type was not recognized. Exiting...")
    sys.exit()

paths = []
types = ('.gz', '.zip')
if args.recursive:
    for path in args.inputs:
        for p in path.glob(f"**/*"):
            if p.is_file() and p.suffix in types:
                paths.append(p)
else:
    paths = [ path for path in args.inputs if path.is_file() ]


print("Calulating total file size...")
def sum(paths):
    total_size = 0
    for path in progressbar.progressbar(paths):
        if tarfile.is_tarfile(path):
            for member in tarfile.open(path).getmembers():
                if member.isfile():
                    total_size += member.size
        elif zipfile.is_zipfile(path):
            for member in zipfile.ZipFile(path).filelist:
                total_size += member.file_size
        else:
            total_size += path.stat().st_size
    return total_size

total_size = sum(paths)
print(total_size)

total_success = 0
total_failed = 0

disallowed_extensions = ['.cap', '.pcap', '.sha1sum', '.pcapng']
with progressbar.DataTransferBar(max_value=total_size) as progress:
    for path in paths:
        print(f"Importing dataset {path}")
        if tarfile.is_tarfile(path):
            tf = tarfile.open(path)
            members = tf.getmembers()
        elif zipfile.is_zipfile(path):
            zf = zipfile.ZipFile(path)
            members = [f.filename for f in zf.filelist]
        else:
            members = [path]

        for m in members:
            if tarfile.is_tarfile(path):
                if not m.isfile() or Path(m.name).suffix in disallowed_extensions:
                    continue
                else:
                    print(f"- Importing member file {m.name}...")
                    logfile = f"{path}/{m.name}"
                    mf = tf.extractfile(m)
            elif zipfile.is_zipfile(path):
                if m.endswith('/') or Path(m).suffix in disallowed_extensions:
                    continue
                else:
                    print(f"- Importing member file {m}...")
                    logfile = f"{path}/{m}"
                    mf = zf.open(m)
            else:
                if not Path(m).is_file() or Path(m).suffix in disallowed_extensions:
                    continue
                else:
                    print(f"- Importing member file {m}...")
                    logfile = f"{m}"
                    mf = open(m)

            def generate_actions(f, progress):
                for line in f:
                    try:
                        source = json.loads(line)
                    except json.decoder.JSONDecodeError as e:
                        # This allows for pushing in raw logs (e.g. Zeek from compound dataset apt29)
                        source = { "message": line }
                    source["log"] = { "file": { "name": logfile }}
                    source.setdefault("winlog", dict())

                    # Plain data created by nxlog is completely moved to winlog.event_data except blacklisted
                    if "EventID" in source:
                        # Move event id to appropriate location
                        source["winlog"]["event_id"] = source["EventID"]
                        del source["EventID"]

                        # Discard unneeded fields
                        try:
                            del source["type"]
                        except KeyError:
                            pass

                        try:
                            del source["host"]
                        except KeyError:
                            pass

                        # Move fields from top level to winlog.event_data
                        source["winlog"]["event_data"] = {
                                    k: v
                                    for k, v in source.items()
                                    if k not in ("winlog", "log", "Channel", "Hostname", "@timestamp", "@version")
                                }
                        for k in source["winlog"]["event_data"].keys():
                            del source[k]

                        # Special handling for host name
                        try:
                            source["winlog"]["computer_name"] = source["Hostname"]
                            del source["Hostname"]
                        except KeyError:
                            pass

                        # Special handling for channel
                        try:
                            source["winlog"]["channel"] = source["Channel"]
                            del source["Channel"]
                        except KeyError:
                            pass

                    # Data created with Winlogbeat <7 contains event fields in event_data instead of winlog.event_data - move it
                    if "event_data" in source:
                        source["winlog"]["event_data"] = source["event_data"]
                        del source["event_data"]
                    # Old Winlogbeats also put the channel name in the log_name field move this to new field names
                    if "log_name" in source:
                        source["winlog"]["channel"] = source["log_name"]
                        del source["log_name"]
                    # Some log records contain the channel name "security" in small letters, fix this
                    try:
                        if source["winlog"]["channel"] == "security":
                            source["winlog"]["channel"] = "Security"
                    except KeyError:
                        pass
                    # Old Winlogbeats also put the event id in a different location, move it to the new one
                    if "event_id" in source:
                        source["winlog"]["event_id"] = source["event_id"]
                        del source["event_id"]
                        # Also set event.code to event id
                        source.setdefault("event", dict())["code"] = source["winlog"]["event_id"]

                    progress.update(progress.value + len(line))
                    if args.output == "elasticsearch":
                        yield {
                                "_index": index,
                                "_source": source
                            }
                    elif args.output == "logstash":
                        yield source
            if args.output == "elasticsearch":
                success_count, fail_count = bulk(es, generate_actions(mf, progress), True, raise_on_error=False)
                total_success += success_count
                total_failed += fail_count
                if fail_count > 0:
                    color = "red"
                else:
                    color = "green"
            elif args.output == "logstash":
                fail_count = 0
                success_count = 0
                for event in generate_actions(mf, progress):
                    r = requests.post(logstash_url, json=event, verify=verify_certs)
                    if r.status_code == 200:
                        success_count += 1
                        total_success += 1
                        color = "green"
                    else:
                        fail_count += 1
                        total_failed += 1
                        color = "red"
            print(colored(f"- Imported {success_count} events, {fail_count} failed", color))
        if tarfile.is_tarfile(path):
            tf.close()
        elif zipfile.is_zipfile(path):
            zf.close()
        else:
            pass
        
print(f"Imported {total_success} log records, {total_failed} failed.")
