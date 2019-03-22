
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

| log_name                                 | task                                                   |   record_number |
|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | Pipeline Execution Details                             |             130 |
| Security                                 | Filtering Platform Connection                          |             161 |
| Security                                 | Token Right Adjusted Events                            |             106 |
| Security                                 | Detailed File Share                                    |              92 |
| Security                                 | Group Membership                                       |              14 |
| Security                                 | Logon                                                  |              14 |
| Security                                 | Logoff                                                 |              12 |
| Security                                 | Special Logon                                          |               7 |
| Security                                 | Process Termination                                    |               6 |
| Security                                 | Process Creation                                       |               5 |
| Security                                 | Sensitive Privilege Use                                |               5 |
| Security                                 | User Account Management                                |               4 |
| Security                                 | Authorization Policy Change                            |               1 |
| Security                                 | File Share                                             |               1 |
| Security                                 | Kerberos Service Ticket Operations                     |               1 |
| Security                                 | Other Object Access Events                             |               1 |
| Security                                 | Security Group Management                              |               1 |
| Microsoft-Windows-Sysmon/Operational     | Image loaded (rule: ImageLoad)                         |             230 |
| Microsoft-Windows-Sysmon/Operational     | Process accessed (rule: ProcessAccess)                 |             128 |
| Microsoft-Windows-Sysmon/Operational     | Network connection detected (rule: NetworkConnect)     |              70 |
| Microsoft-Windows-Sysmon/Operational     | File created (rule: FileCreate)                        |              49 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Connected (rule: PipeEvent)                       |              26 |
| Microsoft-Windows-Sysmon/Operational     | Registry object added or deleted (rule: RegistryEvent) |              25 |
| Microsoft-Windows-Sysmon/Operational     | RawAccessRead detected (rule: RawAccessRead)           |               7 |
| Microsoft-Windows-Sysmon/Operational     | Process Create (rule: ProcessCreate)                   |               6 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational | Executing Pipeline                                     |             110 |


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