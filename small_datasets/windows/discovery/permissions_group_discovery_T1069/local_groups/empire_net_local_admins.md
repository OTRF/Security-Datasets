
# Empire Net Local Administrators Group

An adversary can enumerate members of the local Administratrors group via net.exe

## Technique(s) ID

T1069

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_net_local_admins.tar.gz](./empire_net_local_admins.tar.gz)

## Network Environment

Shire

## Time Taken

2019-03-19020147

## About this file

| log_name                                 | task                                                   |   record_number |
|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | Pipeline Execution Details                             |             150 |
| Security                                 | Filtering Platform Connection                          |             175 |
| Security                                 | Token Right Adjusted Events                            |              94 |
| Security                                 | User Account Management                                |              60 |
| Security                                 | Process Termination                                    |               9 |
| Security                                 | Logon                                                  |               5 |
| Security                                 | Group Membership                                       |               4 |
| Security                                 | Logoff                                                 |               4 |
| Security                                 | Special Logon                                          |               4 |
| Security                                 | Sensitive Privilege Use                                |               3 |
| Security                                 | Authorization Policy Change                            |               2 |
| Security                                 | Other Object Access Events                             |               2 |
| Security                                 | Process Creation                                       |               2 |
| Security                                 | File Share                                             |               1 |
| Microsoft-Windows-Sysmon/Operational     | Process accessed (rule: ProcessAccess)                 |             111 |
| Microsoft-Windows-Sysmon/Operational     | Image loaded (rule: ImageLoad)                         |              70 |
| Microsoft-Windows-Sysmon/Operational     | Network connection detected (rule: NetworkConnect)     |              65 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Connected (rule: PipeEvent)                       |              36 |
| Microsoft-Windows-Sysmon/Operational     | Registry object added or deleted (rule: RegistryEvent) |              28 |
| Microsoft-Windows-Sysmon/Operational     | RawAccessRead detected (rule: RawAccessRead)           |               5 |
| Microsoft-Windows-Sysmon/Operational     | File created (rule: FileCreate)                        |               4 |
| Microsoft-Windows-Sysmon/Operational     | Process Create (rule: ProcessCreate)                   |               3 |
| Microsoft-Windows-Sysmon/Operational     | Registry value set (rule: RegistryEvent)               |               3 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational | Executing Pipeline                                     |             123 |

## Empire Activity

```
shell net localgroup "Administrators"
```

```
(Empire: FD6A3MGY) >   
[*] Tasked FD6A3MGY to run TASK_SHELL
[*] Agent FD6A3MGY tasked with task ID 4
(Empire: FD6A3MGY) > Alias name     Administrators
Comment        

Members

-------------------------------------------------------------------------------
Administrator
Pedro
SHIRE\Domain Admins
SHIRE\SG DL shire Workstation Administrators
The command completed successfully.


..Command execution completed.

(Empire: FD6A3MGY) >
```