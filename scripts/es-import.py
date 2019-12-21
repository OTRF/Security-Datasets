#!/usr/bin/env python3
# Import datasets to Elasticsearch instance

from argparse import ArgumentParser
from pathlib import Path
import tarfile
import json
import progressbar
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from termcolor import colored

progressbar.streams.wrap_stdout()

argparser = ArgumentParser(description="Import datasets into Elasticsearch")
argparser.add_argument("--recursive", "-r", action="store_true", help="Recurse into directories")
argparser.add_argument("--elasticsearch", "-e", default="http://localhost:9200", help="URL of Elasticsearch instance (%(default)s)")
argparser.add_argument("--cacerts", "-c", default=None, help="Path to CA certificates for TLS verification")
argparser.add_argument("--insecure", "-I", action="store_false", dest="verify_certs", help="Don't verify TLS cerificates.")
argparser.add_argument("--index", "-i", default="winlogbeat-mordor", help="Target index for data import (%(default)s)")
argparser.add_argument("--no-index-creation", "-n", action="store_false", dest="create_index", help="Don't create index.")
argparser.add_argument("inputs", nargs="+", type=Path, help="Path to dataset")
args = argparser.parse_args()

print("Initializing Elasticsearch connection and index...")
index = args.index
es = Elasticsearch(
        [args.elasticsearch],
        ca_certs=args.cacerts,
        verify_certs=args.verify_certs,
        )
if  args.create_index:
    es.indices.create(
            index,
            body={ "settings": {
                        "index.mapping.total_fields.limit": 2000
                    }
                 }
        )

if args.recursive:
    paths = [ p for path in args.inputs for p in path.glob("**/*.tar.gz") if p.is_file() ]
else:
    paths = args.inputs

print("Calulating total file size...")
total_size = sum([
    member.size
    for path in progressbar.progressbar(paths)
    for member in tarfile.open(path).getmembers() if member.isfile()
    ])

with progressbar.DataTransferBar(max_value=total_size) as progress:
    for path in paths:
        print(f"Importing dataset {path}")
        tf = tarfile.open(path)
        for m in tf.getmembers():
            if m.isfile():
                print(f"- Importing member file {m.name}...")
                logfile = f"{path}/{m.name}"
                mf = tf.extractfile(m)
                def generate_actions(f, progress):
                    for line in f:
                        source = json.loads(line)
                        source["log"] = { "file": logfile }
                        progress.update(progress.value + len(line))
                        yield {
                                "_index": index,
                                "_source": source
                              }
                success_count, fail_count = bulk(es, generate_actions(mf, progress), True, raise_on_error=False)
                if fail_count > 0:
                    color = "red"
                else:
                    color = "green"
                print(colored(f"- Imported {success_count} events, {fail_count} failed", color))
        tf.close()
