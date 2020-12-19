# Mordor script: Mordor-Stats.py
# Mordor script description: Provides basic stats by event log and task category
# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# Requirements

import argparse
import pandas as pd
from pandas.io.json import json_normalize
import json

# Initial description
text = 'This script allows you merge two JSON files'

# Initiate the parser
parser = argparse.ArgumentParser(description=text)

# Add arguments (store_true means no argument needed)
parser.add_argument("-a", "--file-a", help="file to merge", type=str , required=True)
parser.add_argument("-b", "--file-b", help="file to merge", type=str , required=True)
parser.add_argument("-o", "--file-output", help="file to output", type=str , required=True)

args = parser.parse_args()

f1data = f2data = "" 
 
with open(args.file_a) as f1: 
  f1data = f1.read()

with open(args.file_b) as f2: 
  f2data = f2.read() 
 
f1data += "\n"
f1data += f2data

with open (args.file_output, 'a') as f3: 
  f3.write(f1data)