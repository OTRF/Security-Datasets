# Empire Wdigest Downgrade

Sets wdigest on the machine to explicitly use by setting HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest\UseLogonCredential

## Technique(s) ID

T1112

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_wdigest_downgrade.tar.gz](./empire_wdigest_downgrade.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18201922

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |             220 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             100 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |              83 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              16 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kerberos Authentication Service                        |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kerberos Service Ticket Operations                     |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |            1755 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             112 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |              92 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |              78 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              14 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |              14 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |               2 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               2 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             183 |

## Attacker Activity