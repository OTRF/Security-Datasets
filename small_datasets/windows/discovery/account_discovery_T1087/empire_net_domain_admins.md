# Empire Net Domain Admins Group

An adversary can enumerate members of the "Domain Admins" active directory group via net.exe. However, if an organization restricts clients allowed to make remote calls to SAM, only specific users can enumerate users and groups in the local Security Accounts Manager (SAM) database and Active Directory.

## Technique(s) ID

T1069

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_net_domain_admins.tar.gz](./empire_net_domain_admins.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18201207

## About this file

| log_name                                   | source_name                              | task                                                   |   record_number |
|--------------------------------------------|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                               | Pipeline Execution Details                             |             146 |
| System                                     | Microsoft-Windows-Directory-Services-SAM | na                                                     |              21 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Filtering Platform Connection                          |              70 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Token Right Adjusted Events                            |              44 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Registry                                               |              12 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Other Object Access Events                             |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing      | SAM                                                    |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Handle Manipulation                                    |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Detailed File Share                                    |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Group Membership                                       |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Kerberos Service Ticket Operations                     |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Logoff                                                 |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Logon                                                  |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Process Creation                                       |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Process Termination                                    |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Authorization Policy Change                            |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing      | File Share                                             |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Special Logon                                          |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity           | na                                                     |               1 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Process accessed (rule: ProcessAccess)                 |             236 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Network connection detected (rule: NetworkConnect)     |              65 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Image loaded (rule: ImageLoad)                         |              35 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Registry object added or deleted (rule: RegistryEvent) |              35 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Pipe Connected (rule: PipeEvent)                       |              13 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Process Create (rule: ProcessCreate)                   |               2 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Process terminated (rule: ProcessTerminate)            |               2 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | File created (rule: FileCreate)                        |               1 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell             | Executing Pipeline                                     |             119 |

## Attacker Activity

```
(Empire: TKV35P8X) > shell net group "Domain Admins" /domain
[*] Tasked TKV35P8X to run TASK_SHELL
[*] Agent TKV35P8X tasked with task ID 14
(Empire: TKV35P8X) > The request will be processed at a domain controller for domain shire.com.

Group name     Domain Admins
Comment        Designated administrators of the domain

Members

-------------------------------------------------------------------------------
Administrator            Mmidge                   oda                      
pgustavo                 
The command completed successfully.


..Command execution completed.

(Empire: TKV35P8X) >
```
