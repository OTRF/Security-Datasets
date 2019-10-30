# Interactive Task Manager Lsass dump

An adversary with local admin rights over the host can easily use task manager interactively and dump the memory space of lsass.

## Technique(s) ID

T1003

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[interactive_taskmngr_lsass_dump.tar.gz](./interactive_taskmngr_lsass_dump.tar.gz)

## Network Environment

Shire

## Time Taken

2019-10-27054517

## About this file

| log_name                             | source_name                         | task                                                   |   record_number |
|--------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| security                             | Microsoft-Windows-Security-Auditing | Kernel Object                                          |              24 |
| security                             | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              20 |
| security                             | Microsoft-Windows-Security-Auditing | Removable Storage                                      |              15 |
| security                             | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |              15 |
| security                             | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |              10 |
| security                             | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               8 |
| security                             | Microsoft-Windows-Security-Auditing | File System                                            |               2 |
| security                             | Microsoft-Windows-Security-Auditing | Process Creation                                       |               2 |
| security                             | Microsoft-Windows-Security-Auditing | Security System Extension                              |               2 |
| security                             | Microsoft-Windows-Security-Auditing | Process Termination                                    |               1 |
| System                               | Service Control Manager             |                                                        |               1 |
| Security                             | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |               7 |
| Security                             | Microsoft-Windows-Security-Auditing | File Share                                             |               1 |
| Security                             | Microsoft-Windows-Security-Auditing | Process Termination                                    |               1 |
| Microsoft-Windows-Sysmon/Operational | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |            1444 |
| Microsoft-Windows-Sysmon/Operational | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             471 |
| Microsoft-Windows-Sysmon/Operational | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             237 |
| Microsoft-Windows-Sysmon/Operational | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |              68 |
| Microsoft-Windows-Sysmon/Operational | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              16 |
| Microsoft-Windows-Sysmon/Operational | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |              12 |
| Microsoft-Windows-Sysmon/Operational | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |               4 |
| Microsoft-Windows-Sysmon/Operational | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |               4 |
| Microsoft-Windows-Sysmon/Operational | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               2 |
| Microsoft-Windows-Sysmon/Operational | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               2 |
| Microsoft-Windows-Sysmon/Operational | Microsoft-Windows-Sysmon            | File creation time changed (rule: FileCreateTime)      |               1 |

## Attacker Activity

```
Open Windows Task Manager as Administrator
Select lsass.exe
Right-click on lsass.exe and select “Create dump file”
```