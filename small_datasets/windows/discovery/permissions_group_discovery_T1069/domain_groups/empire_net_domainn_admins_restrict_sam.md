
# Empire Net Domain Admins Group

An adversary can enumerate members of the "Domain Admins" active directory group via net.exe. However, if an organization restricts clients allowed to make remote calls to SAM, only specific users can enumerate users and groups in the local Security Accounts Manager (SAM) database and Active Directory.

## Technique(s) ID

T1069

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_net_domain_admins_restrict_sam.gz](./empire_net_domain_admins_restrict_sam.gz)

## Network Environment

Shire

## Time Taken

2019-04-0301001

## About this file

| log_name                                   | source_name                              | task                                                   |   record_number |
|--------------------------------------------|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                               | Pipeline Execution Details                             |             266 |
| System                                     | Microsoft-Windows-Directory-Services-SAM | na                                                     |               1 |
| System                                     | Service Control Manager                  | na                                                     |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Filtering Platform Connection                          |            4947 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Other Policy Change Events                             |            1906 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Token Right Adjusted Events                            |             901 |
| Security                                   | Microsoft-Windows-Security-Auditing      | MPSSVC Rule-Level Policy Change                        |             226 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Process Creation                                       |              90 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Sensitive Privilege Use                                |              70 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Process Termination                                    |              41 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Authorization Policy Change                            |              40 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Removable Storage                                      |              33 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Logon                                                  |              32 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Group Membership                                       |              29 |
| Security                                   | Microsoft-Windows-Security-Auditing      | User Account Management                                |              28 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Special Logon                                          |              22 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Registry                                               |              21 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Security System Extension                              |              21 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Handle Manipulation                                    |              20 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Security Group Management                              |              14 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Logoff                                                 |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Other Object Access Events                             |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Kernel Object                                          |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Other System Events                                    |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Plug and Play Events                                   |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing      | File Share                                             |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing      | SAM                                                    |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Detailed File Share                                    |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing      | System Integrity                                       |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity           | na                                                     |               1 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Image loaded (rule: ImageLoad)                         |            4958 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Process accessed (rule: ProcessAccess)                 |            4487 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Registry object added or deleted (rule: RegistryEvent) |             430 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Network connection detected (rule: NetworkConnect)     |             122 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Registry value set (rule: RegistryEvent)               |             116 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Pipe Connected (rule: PipeEvent)                       |              75 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | File created (rule: FileCreate)                        |              74 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | RawAccessRead detected (rule: RawAccessRead)           |              70 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Process Create (rule: ProcessCreate)                   |              33 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Driver loaded (rule: DriverLoad)                       |               5 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Pipe Created (rule: PipeEvent)                         |               3 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell             | Executing Pipeline                                     |             221 |
| Microsoft-Windows-DNS-Client/Operational   | Microsoft-Windows-DNS-Client             | na                                                     |             432 |

## Empire Activity

```
(Empire: NZB6SE34) > shell net group "Domain Admins" /domain
```

```
[*] Tasked NZB6SE34 to run TASK_SHELL
[*] Agent NZB6SE34 tasked with task ID 20
(Empire: NZB6SE34) > The request will be processed at a domain controller for domain shire.com.


..Command execution completed.

(Empire: NZB6SE34) >
```
