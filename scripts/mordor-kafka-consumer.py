#!/usr/bin/env python

# Author: Roberto Rodriguez @Cyb3rWard0g
# License: GPL-3.0
# Reference: https://github.com/confluentinc/confluent-kafka-python/blob/master/examples/consumer.py

from confluent_kafka import Consumer, KafkaException
import sys
import json
import logging
import time
import argparse

sys.stderr.write(r"""
   _____                   .___              __            _____ __            
  /     \   ___________  __| _/___________  |  | _______ _/ ____\  | _______   
 /  \ /  \ /  _ \_  __ \/ __ |/  _ \_  __ \ |  |/ /\__  \\   __\|  |/ /\__  \  
/    Y    (  <_> )  | \/ /_/ (  <_> )  | \/ |    <  / __ \|  |  |    <  / __ \_
\____|__  /\____/|__|  \____ |\____/|__|    |__|_ \(____  /__|  |__|_ \(____  /
        \/                  \/                   \/     \/           \/     \/ 
_________                                                                      
\_   ___ \  ____   ____   ________ __  _____   ___________                     
/    \  \/ /  _ \ /    \ /  ___/  |  \/     \_/ __ \_  __ \                    
\     \___(  <_> )   |  \\___ \|  |  /  Y Y  \  ___/|  | \/                    
 \______  /\____/|___|  /____  >____/|__|_|  /\___  >__|                       
        \/            \/     \/            \/     \/      V0.0.1

Creator: Roberto Rodriguez @Cyb3rWard0g
License: GPL-3.0
 
""")

# Initial description
text = "This mordor script allows you to retrieve security events from a specific kafka topic available in a running kafka broker"
example_text = '''examples:

 python3 mordor-kafka-consumer.py -b localhost:9092 -t winevent
 python3 mordor-kafka-consumer.py -b localhost:9092 -t winevent -E '{"tactic":"Credential Access"}'
 python3 mordor-kafka-consumer.py -b localhost:9092 -t winevent -n wmi_subscriptions -o datasets/
 python3 mordor-kafka-consumer.py -b localhost:9092 -t winevent -n wmi_subscriptions -o datasets/ -E '{"tactic":"Credential Access"}'
 '''

# Initiate the parser
parser = argparse.ArgumentParser(description=text,epilog=example_text,formatter_class=argparse.RawDescriptionHelpFormatter)

# Add arguments (store_true means no argument needed)
parser.add_argument("-b", "--kafka-broker", help="Kafka broker to connect to consume security events. i.e. localhost:9092", required=True)
parser.add_argument("-t", "--kafka-topics", help="Kafka topics where to retrieve security events from. i.e. winevent,linevent", type=str, required=True)
parser.add_argument("-g", "--kafka-group-id", help="Kafka group id i.e. mordor", required=False)
parser.add_argument("-n", "--dataset-name", help="name of the dataset being created", required=False)
parser.add_argument("-o", "--output-dir", help="directory path where to write consumed events to. i.e mordor/datasets/", required=False)
parser.add_argument("-E", "--extra-fields", help="additional fields and values to add to each security event.", type=json.loads, required=False)

args = parser.parse_args()

# optional arguments
if (args.dataset_name and args.output_dir is None) or (args.output_dir and args.dataset_name is None):
    parser.error("--dataset-name and --output-dir are required together")
else:
    timestr = time.strftime("%Y%m%d_%H%M%S")
    dataset_name = "{}{}_{}.json".format(args.output_dir, args.dataset_name, timestr)
if args.kafka_group_id:
    group = args.kafka_group_id
else:
    group = "mordor"
# required arguments
broker = args.kafka_broker
topics = [item for item in args.kafka_topics.split(',')]

def print_assignment(consumer, partitions):
    sys.stderr.write("""Assignment: {}

""".format(partitions))

def commit_completed(err, partitions):
    if err:
        sys.stderr.write(str(err))
    else:
        sys.stderr.write("""Committed partition offsets: {}

""".format(str(partitions)))

# Consumer configuration
# See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
conf = {
    'bootstrap.servers': broker,
    'group.id': group,
    'session.timeout.ms': 6000,
    'auto.offset.reset': 'latest',
    'on_commit': commit_completed
}

# Create logger for consumer (logs will be emitted when poll() is called)
logger = logging.getLogger('consumer')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)-15s %(levelname)-8s %(message)s'))
logger.addHandler(handler)

# Create Consumer instance
c = Consumer(conf, logger=logger)

# Read messages from Kafka, print to stdout
try:
    # Subscribe to topics
    c.subscribe(topics, on_assign=print_assignment)

    while True:
        msg = c.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        else:
            # Proper message
            sys.stderr.write('%% %s [%d] at offset %d with key %s:\n' % (msg.topic(), msg.partition(), msg.offset(), str(msg.key())))
            # decode unicode to strings
            mordor_event = msg.value().decode('utf8')
            if args.extra_fields:
                # convert string to dictionary
                pythDict = json.loads(mordor_event)
                # update dictionary with extra fields
                pythDict.update(args.extra_fields)
                # convert dictionary back to strings
                mordor_event = json.dumps(pythDict)
            if dataset_name:
                with open("{}".format(dataset_name), 'a') as file:
                    file.write(mordor_event + '\n')
            else:       
                print(mordor_event)

except KeyboardInterrupt:
    sys.stderr.write('%% Aborted by user\n')

finally:
    # Close down consumer to commit final offsets.
    c.close()
    if dataset_name:
        sys.stderr.write("Events were written to {}\n".format(dataset_name))