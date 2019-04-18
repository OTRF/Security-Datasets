import sys

inFile = sys.argv[1]

import pandas as pd
from tabulate import tabulate

mordor_file = pd.read_json(inFile,lines=True)
mordor_summary = mordor_file.groupby(['log_name','task']).count()['record_number']
mordor_summary_df = mordor_summary.to_frame().sort_values(by=['log_name','record_number'],ascending=False)
mordor_summary_df_table = mordor_summary_df.reset_index(level=['task'])
print(tabulate(mordor_summary_df_table, tablefmt="github", headers="keys"))