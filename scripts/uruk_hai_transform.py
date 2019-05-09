# Mordor script: uruk_hai_transform.py
# Mordor script description: Replace values in a mordor file
# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

import argparse
import datetime
import json
import copy
import time

# Initial description
text = 'This script allows you to replace values in a mordor file to make it look as if it occurred in your own network'

# Initiate the parser
parser = argparse.ArgumentParser(description=text)

# Add arguments (store_true means no argument needed)
parser.add_argument("-v", "--version", help="shows version of script", action="store_true")
parser.add_argument("-r", "--replace", help="Values to be replaced on every record. Format '{\"original_value\":\"new_value\",\"original_value\":\"new_value\"}' ", type=json.loads, nargs=1, required=True)
parser.add_argument("-t", "--timestamp", help="custom date for attack. Format YYYY-MM-DD", type=datetime.date.fromisoformat, required=True)
parser.add_argument("-f", "--file", help="file to customize and send", type=str , required=True)

args = parser.parse_args()

# Bannner
print(r"""
 _   _            _         _   _       _ 
| | | |_ __ _   _| | __    | | | | __ _(_)
| | | | '__| | | | |/ /____| |_| |/ _` | |
| |_| | |  | |_| |   <_____|  _  | (_| | |
 \___/|_|   \__,_|_|\_\    |_| |_|\__,_|_|                                         
 _____                     __                      
|_   _| __ __ _ _ __  ___ / _| ___  _ __ _ __ ___  
  | || '__/ _` | '_ \/ __| |_ / _ \| '__| '_ ` _ \ 
  | || | | (_| | | | \__ \  _| (_) | |  | | | | | |
  |_||_|  \__,_|_| |_|___/_|  \___/|_|  |_| |_| |_| V0.1

 Creator: Roberto Rodriguez @Cyb3rWard0g
 License: GPL-3.0
 """)

if args.version:
    print("script version 0.1")

time_start = time.time()

# Read mordor file json
event_logs = list()
with open(args.file) as file:
    for line in file:
        event_logs.append(json.loads(line))

# Set List
new_json = list()

# Iterating over each json record
count = 0

print("[*] Original Mordor file:", args.file)

# Loop through records
for event in event_logs:
    if "@timestamp" in event.keys():
        # Set Timestamp to datetime object
        if type(event['@timestamp']) is not datetime.datetime:
            event['@timestamp'] = datetime.datetime.strptime(event['@timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')
        # Extract originnal date (YYY-MM-DD)
        original_date = copy.deepcopy(event['@timestamp'])
        original_date = datetime.datetime.strftime(original_date, '%Y-%m-%d')

        # Update initial mappinng dictionary
        data_input = copy.deepcopy(args.replace[0])
        if original_date not in event.keys():
            data_input.update({original_date: str(args.timestamp)})
    
        event['@timestamp'] = datetime.datetime.strftime(event['@timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')
        event_strings = json.dumps(event,ensure_ascii=False)
        # Replace strings from dictionary input
        for k,v in data_input.items():
            event_strings = event_strings.replace(k,v)
        new_json.append(event_strings)

        # Increate coutn
        count += 1
    else:
        exit()

# Name of file
file_name = copy.deepcopy(args.file)
file_name = file_name.replace(original_date, str(args.timestamp))

# Write event dictionaries from a list to a json file
with open(file_name, 'w') as new_file:
    for new_event in new_json:
        print(new_event, file=new_file)

# Final time
time_end = time.time()
total_time = time_end - time_start

# Final stats
print("[*] Keys replaced by their values:",data_input)
print("[*] Records processed:", count)
print("[*] Time taken:",total_time,"seconds")
print("[*] New Mordor File:",file_name)