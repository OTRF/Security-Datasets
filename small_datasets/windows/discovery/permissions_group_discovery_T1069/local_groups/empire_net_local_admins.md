
# Empire Net Local Administrators Group

An adversary can enumerate members of the local Administratrors group via the net.exe utility

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

| log_name                                  | source_name                         | task                                                   |   record_number |
|-------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                        | PowerShell                          | Pipeline Execution Details                             |             150 |
| Security                                  | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             175 |
| Security                                  | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |              94 |
| Security                                  | Microsoft-Windows-Security-Auditing | User Account Management                                |              60 |
| Security                                  | Microsoft-Windows-Security-Auditing | Process Termination                                    |               9 |
| Security                                  | Microsoft-Windows-Security-Auditing | Logon                                                  |               5 |
| Security                                  | Microsoft-Windows-Security-Auditing | Group Membership                                       |               4 |
| Security                                  | Microsoft-Windows-Security-Auditing | Logoff                                                 |               4 |
| Security                                  | Microsoft-Windows-Security-Auditing | Special Logon                                          |               4 |
| Security                                  | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               3 |
| Security                                  | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               2 |
| Security                                  | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               2 |
| Security                                  | Microsoft-Windows-Security-Auditing | Process Creation                                       |               2 |
| Security                                  | Microsoft-Windows-Security-Auditing | File Share                                             |               1 |
| Microsoft-Windows-Sysmon/Operational      | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             111 |
| Microsoft-Windows-Sysmon/Operational      | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |              70 |
| Microsoft-Windows-Sysmon/Operational      | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |              65 |
| Microsoft-Windows-Sysmon/Operational      | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              36 |
| Microsoft-Windows-Sysmon/Operational      | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |              28 |
| Microsoft-Windows-Sysmon/Operational      | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |               5 |
| Microsoft-Windows-Sysmon/Operational      | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |               4 |
| Microsoft-Windows-Sysmon/Operational      | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               3 |
| Microsoft-Windows-Sysmon/Operational      | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |               3 |
| Microsoft-Windows-Sysmon/Operational      | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational  | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             123 |
| Microsoft-Windows-DNS-Client/Operational  | Microsoft-Windows-DNS-Client        | na                                                     |             186 |
| Microsoft-Windows-Bits-Client/Operational | Microsoft-Windows-Bits-Client       | na                                                     |               2 |

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