
# Empire Net Domain Admins Group

An adversary can enumerate members of the "Domain Admins" active directory group via net.exe

## Technique(s) ID

T1069

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_net_domain_admins.gz](./empire_net_domain_admins.gz)

## Network Environment

Shire

## Time Taken

2019-03-19014732

## About this file

| log_name                                 | source_name                         | task                                                   |   record_number |
|------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | PowerShell                          | Pipeline Execution Details                             |             220 |
| Security                                 | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             276 |
| Security                                 | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             264 |
| Security                                 | Microsoft-Windows-Security-Auditing | Group Membership                                       |              20 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logon                                                  |              20 |
| Security                                 | Microsoft-Windows-Security-Auditing | Process Termination                                    |              17 |
| Security                                 | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |              15 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logoff                                                 |              15 |
| Security                                 | Microsoft-Windows-Security-Auditing | Process Creation                                       |              12 |
| Security                                 | Microsoft-Windows-Security-Auditing | Special Logon                                          |              10 |
| Security                                 | Microsoft-Windows-Security-Auditing | File Share                                             |               5 |
| Security                                 | Microsoft-Windows-Security-Auditing | SAM                                                    |               4 |
| Security                                 | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               3 |
| Security                                 | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               1 |
| Security                                 | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               1 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             412 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             386 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             125 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              65 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |              57 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              22 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |              11 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |               5 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |               1 |
| Microsoft-Windows-PowerShell/Operational | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             184 |
| Microsoft-Windows-DNS-Client/Operational | Microsoft-Windows-DNS-Client        | na                                                     |             188 |

## Empire Activity

```
shell net group "Domain Admins" /domain
```

```
(Empire: FD6A3MGY) > 
[*] Tasked FD6A3MGY to run TASK_SHELL
[*] Agent FD6A3MGY tasked with task ID 3
(Empire: FD6A3MGY) > The request will be processed at a domain controller for domain shire.com.

Group name     Domain Admins
Comment        Designated administrators of the domain

Members

-------------------------------------------------------------------------------
Administrator            Mmidge                   oda                      
The command completed successfully.


..Command execution completed.

(Empire: FD6A3MGY) >
```