
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

| log_name                                 | task                                                   |   events_count  |
|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | Pipeline Execution Details                             |             220 |
| Security                                 | Token Right Adjusted Events                            |             276 |
| Security                                 | Filtering Platform Connection                          |             264 |
| Security                                 | Group Membership                                       |              20 |
| Security                                 | Logon                                                  |              20 |
| Security                                 | Process Termination                                    |              17 |
| Security                                 | Detailed File Share                                    |              15 |
| Security                                 | Logoff                                                 |              15 |
| Security                                 | Process Creation                                       |              12 |
| Security                                 | Special Logon                                          |              10 |
| Security                                 | File Share                                             |               5 |
| Security                                 | SAM                                                    |               4 |
| Security                                 | Authorization Policy Change                            |               3 |
| Security                                 | Other Object Access Events                             |               1 |
| Security                                 | Sensitive Privilege Use                                |               1 |
| Microsoft-Windows-Sysmon/Operational     | Process accessed (rule: ProcessAccess)                 |             412 |
| Microsoft-Windows-Sysmon/Operational     | Image loaded (rule: ImageLoad)                         |             386 |
| Microsoft-Windows-Sysmon/Operational     | Network connection detected (rule: NetworkConnect)     |             125 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Connected (rule: PipeEvent)                       |              65 |
| Microsoft-Windows-Sysmon/Operational     | Registry object added or deleted (rule: RegistryEvent) |              57 |
| Microsoft-Windows-Sysmon/Operational     | File created (rule: FileCreate)                        |              22 |
| Microsoft-Windows-Sysmon/Operational     | Process Create (rule: ProcessCreate)                   |              11 |
| Microsoft-Windows-Sysmon/Operational     | RawAccessRead detected (rule: RawAccessRead)           |               5 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-Sysmon/Operational     | Registry value set (rule: RegistryEvent)               |               1 |
| Microsoft-Windows-PowerShell/Operational | Executing Pipeline                                     |             184 |


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