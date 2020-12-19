# Mordor script: uruk_hai_transform.py
# Mordor script description: Replace values in a mordor file
# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

import argparse
import pandas as pd
from datetime import datetime
import logging
import copy
import time
import re
import yaml
import sys

# Initial description
text = 'This script allows you to replace values in a mordor file to make it look as if it occurred in your own network'
example_text = f'''Examples:
 python3 {sys.argv[0]} -f mordor_file_2019-10-10221033.json -t 2020-12-18102055
 python3 {sys.argv[0]} -f mordor_file_2019-10-10221033.json -t 2020-12-18102055 -m string-mappings.yml
 '''

# Initiate the parser
parser = argparse.ArgumentParser(description=text,epilog=example_text,formatter_class=argparse.RawDescriptionHelpFormatter)

# Add arguments (store_true means no argument needed)
parser.add_argument("-f", "--file", help="file to customize and send", type=str , required=True)
parser.add_argument("-t", "--timestamp", help="new timestamp from where to start. Format YYYY-MM-DDHHMMSS", type=lambda d: datetime.strptime(d, '%Y-%m-%d%H%M%S'), required=True)
parser.add_argument("-m", "--mappings-file", help="YAML file with string mappings in a dictionary format to replace string values", type=str , required=False)
parser.add_argument("-d", "--debug", help="Print lots of debugging statements", action="store_const", dest="loglevel", const=logging.DEBUG, default=logging.WARNING)
parser.add_argument("-v", "--verbose", help="Be verbose", action="store_const", dest="loglevel", const=logging.INFO)

args = parser.parse_args()

logging.basicConfig(level=args.loglevel, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
log = logging.getLogger(__name__)

# Bannner
print(r"""
   _____                   .___                                    
  /     \   ___________  __| _/___________                         
 /  \ /  \ /  _ \_  __ \/ __ |/  _ \_  __ \                        
/    Y    (  <_> )  | \/ /_/ (  <_> )  | \/                        
\____|__  /\____/|__|  \____ |\____/|__|                           
        \/                  \/                                     
___________                              _____                     
\__    ___/___________    ____   _______/ ____\___________  _____  
  |    |  \_  __ \__  \  /    \ /  ___/\   __\/  _ \_  __ \/     \ 
  |    |   |  | \// __ \|   |  \\___ \  |  | (  <_> )  | \/  Y Y  \
  |____|   |__|  (____  /___|  /____  > |__|  \____/|__|  |__|_|  /
                      \/     \/     \/                          \/   V0.1

 Creator: Roberto Rodriguez @Cyb3rWard0g
 License: GPL-3.0
 """)

log.debug(f'Started Stopwatch')
time_start = time.time()

# Read mordor file json
print("[+] Old Mordor File:",args.file)
log.debug(f'Reading {args.file} to dataframe..')
df = pd.read_json(args.file, lines=True)

# If string mappings are defined to replace
if args.mappings_file:
  log.info('Replacing strings..')
  log.debug(f'Reading {args.mappings_file} to dictionary..')
  replace_dict = yaml.safe_load(open(args.mappings_file).read())
  log.debug(f'Replacing the following: {replace_dict}..')
  df = df.replace(replace_dict, regex = True)

# Pick earliest time
log.info('Calculating earliest timestamp')
earliest_timestamp = df['@timestamp'].min()
earliest_timestamp = datetime.strptime(earliest_timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
log.debug(f'Earliest timestamp: {earliest_timestamp}')

# Calculate Delta
log.info('Calculating time delta..')
deltatime = args.timestamp - earliest_timestamp
log.debug(f'Time Delta: {deltatime}')

# Replace timestamp column
log.info('Replacing timestamp values..')
df['@timestamp'] = pd.to_datetime(df['@timestamp']) + deltatime

# Set Timestamp column as string
log.info('Updating timestamp type from datetime to string with specific format..')
df['@timestamp'] = df['@timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S.%f').str[:-3]+'Z'

# Getting new name of file
log.info('Defining new file name..')
log.debug(f'Old file name: {args.file}')
old_file_name = copy.deepcopy(args.file)
old_file_name = re.split('\d{4}-\d{2}-\d{8}.json',old_file_name)[0]
timestamp_input_string = args.timestamp.strftime('%Y-%m-%d%H%M%S')
log.debug(f'New file name: {old_file_name}{timestamp_input_string}.json')
new_file_name = f'{old_file_name}{timestamp_input_string}.json'

# Write event dictionaries from a list to a json file
log.info('Exporting dataframe to JSON')
df.apply(lambda x: x.dropna().to_dict(), axis=1).to_json(new_file_name,orient='records', lines=True)

# Final time
time_end = time.time()
total_time = time_end - time_start
log.debug(f'Stopped Stopwatch')

# Final stats
print("[+] Time taken:",total_time,"seconds")
print("[+] New Mordor File:",new_file_name)