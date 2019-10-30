# Remote Interactive Task Manager Lsass dump

An adversary with local admin rights over the host can easily RDP to a victims box, use task manager interactively and dump the memory space of lsass.

## Technique(s) ID

T1003

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[remoteinteractive_taskmngr_lsass_dump.tar.gz](./remoteinteractive_taskmngr_lsass_dump.tar.gz)

## Network Environment

Shire

## Time Taken

2019-10-27055035

## About this file

| log_name                                                               | source_name                                                | task                                                   |   record_number |
|------------------------------------------------------------------------|------------------------------------------------------------|--------------------------------------------------------|-----------------|
| security                                                               | Microsoft-Windows-Security-Auditing                        | Filtering Platform Connection                          |             115 |
| security                                                               | Microsoft-Windows-Security-Auditing                        | User Account Management                                |              10 |
| security                                                               | Microsoft-Windows-Security-Auditing                        | Process Termination                                    |               3 |
| security                                                               | Microsoft-Windows-Security-Auditing                        | Sensitive Privilege Use                                |               1 |
| System                                                                 | Service Control Manager                                    |                                                        |               1 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Other Object Access Events                             |              74 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | SAM                                                    |              74 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Filtering Platform Connection                          |              67 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Kernel Object                                          |              20 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Process Creation                                       |              17 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Process Termination                                    |              16 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Token Right Adjusted Events                            |              15 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Handle Manipulation                                    |              14 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Sensitive Privilege Use                                |              12 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Logon                                                  |              10 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Removable Storage                                      |               9 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Group Membership                                       |               7 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Logoff                                                 |               6 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Special Logon                                          |               5 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | MPSSVC Rule-Level Policy Change                        |               4 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Other Logon/Logoff Events                              |               3 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Plug and Play Events                                   |               3 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Security System Extension                              |               3 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Authorization Policy Change                            |               2 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Kerberos Authentication Service                        |               1 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Kerberos Service Ticket Operations                     |               1 |
| Microsoft-Windows-Windows Firewall With Advanced Security/Firewall     | Microsoft-Windows-Windows Firewall With Advanced Security  |                                                        |               4 |
| Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational | Microsoft-Windows-TerminalServices-RemoteConnectionManager |                                                        |               2 |
| Microsoft-Windows-TerminalServices-LocalSessionManager/Operational     | Microsoft-Windows-TerminalServices-LocalSessionManager     |                                                        |               7 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Registry object added or deleted (rule: RegistryEvent) |            3564 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Process accessed (rule: ProcessAccess)                 |            2246 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Registry value set (rule: RegistryEvent)               |            1547 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Image loaded (rule: ImageLoad)                         |             879 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Network connection detected (rule: NetworkConnect)     |              81 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | File created (rule: FileCreate)                        |              49 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | RawAccessRead detected (rule: RawAccessRead)           |              30 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Process terminated (rule: ProcessTerminate)            |              18 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Process Create (rule: ProcessCreate)                   |              17 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Pipe Connected (rule: PipeEvent)                       |              15 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Dns query (rule: DnsQuery)                             |               5 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Pipe Created (rule: PipeEvent)                         |               2 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | File creation time changed (rule: FileCreateTime)      |               1 |

## Attacker Activity

```
RDP to victim
Open Windows Task Manager as Administrator
Select lsass.exe
Right-click on lsass.exe and select “Create dump file”
```