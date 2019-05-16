
# Empire Net User

An adversary can enumerate local users via the net.exe utility

## Technique(s) ID

T1087

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_net_user.tar.gz](./empire_net_user.tar.gz)

## Network Environment

Shire

## Time Taken

2019-03-19020729

## About this file

| log_name                                 | source_name                         | task                                                   |   record_number |
|------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | PowerShell                          | Pipeline Execution Details                             |             130 |
| Security                                 | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             161 |
| Security                                 | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             106 |
| Security                                 | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |              92 |
| Security                                 | Microsoft-Windows-Security-Auditing | Group Membership                                       |              14 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logon                                                  |              14 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logoff                                                 |              12 |
| Security                                 | Microsoft-Windows-Security-Auditing | Special Logon                                          |               7 |
| Security                                 | Microsoft-Windows-Security-Auditing | Process Termination                                    |               6 |
| Security                                 | Microsoft-Windows-Security-Auditing | Process Creation                                       |               5 |
| Security                                 | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               5 |
| Security                                 | Microsoft-Windows-Security-Auditing | User Account Management                                |               4 |
| Security                                 | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               1 |
| Security                                 | Microsoft-Windows-Security-Auditing | File Share                                             |               1 |
| Security                                 | Microsoft-Windows-Security-Auditing | Kerberos Service Ticket Operations                     |               1 |
| Security                                 | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               1 |
| Security                                 | Microsoft-Windows-Security-Auditing | Security Group Management                              |               1 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             230 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             128 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |              70 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              49 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              26 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |              25 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |               7 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               6 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             110 |

## Empire Activity

```
shell net user
```

```
[*] Tasked FD6A3MGY to run TASK_SHELL
[*] Agent FD6A3MGY tasked with task ID 5
(Empire: FD6A3MGY) > User accounts for \\IT001

-------------------------------------------------------------------------------
Administrator            DefaultAccount           Guest                    
Pedro                    WDAGUtilityAccount       
The command completed successfully.


..Command execution completed.

(Empire: FD6A3MGY) > 
```