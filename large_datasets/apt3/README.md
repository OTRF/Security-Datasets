# Adversary

APT3

## ATT&CK Group ID

G002

## ATT&CK STIX ID

intrusion-set--0bbdf25b-30ff-4894-a1cd-49260d0dd2d9

## Aliases

APT3, Gothic Panda, Pirpi, UPS Team, Buckeye, Threat Group-0110, TG-0110

## Description

[APT3](https://attack.mitre.org/groups/G0022) is a China-based threat group that researchers have attributed to China's Ministry of State Security. (Citation: FireEye Clandestine Wolf) (Citation: Recorded Future APT3 May 2017) This group is responsible for the campaigns known as Operation Clandestine Fox, Operation Clandestine Wolf, and Operation Double Tap. (Citation: FireEye Clandestine Wolf) (Citation: FireEye Operation Double Tap) As of June 2015, the group appears to have shifted from targeting primarily US victims to primarily political organizations in Hong Kong. (Citation: Symantec Buckeye)

## ATT&CK Evaluation 

This large dataset is the result of us replicating APT3 ([Second Scenario](https://attackevals.mitre.org/methodology/round1/scope.html)) from [ATT&CK evaluations (Round 1)](https://attackevals.mitre.org/methodology/round1/)

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)
Jose Luis Rodriguez [@Cyb3rPandaH](https://twitter.com/Cyb3rPandaH)

## Dataset

[empire_apt3.tar.gz](./empire_apt3.tar.gz)

## Network Environment

Shire

* [Empire Resource Files](environment/empire/resource_files)

## Time Taken

2019-05-14223117

## About this file

| log_name                                                               | source_name                                                | task                                                   |   record_number |
|------------------------------------------------------------------------|------------------------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                                                     | PowerShell                                                 | Pipeline Execution Details                             |           18366 |
| Windows PowerShell                                                     | PowerShell                                                 | Provider Lifecycle                                     |            1106 |
| Windows PowerShell                                                     | PowerShell                                                 | Engine Lifecycle                                       |             184 |
| System                                                                 | Microsoft-Windows-Directory-Services-SAM                   | na                                                     |              49 |
| System                                                                 | Service Control Manager                                    | na                                                     |              32 |
| System                                                                 | Microsoft-Windows-GroupPolicy                              | na                                                     |               5 |
| System                                                                 | Microsoft-Windows-Kernel-General                           | na                                                     |               3 |
| System                                                                 | Microsoft-Windows-DistributedCOM                           | na                                                     |               1 |
| System                                                                 | Microsoft-Windows-Winlogon                                 | na                                                     |               1 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Filtering Platform Connection                          |            7621 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Token Right Adjusted Events                            |            3259 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Removable Storage                                      |            1927 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Registry                                               |            1762 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Handle Manipulation                                    |            1077 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Detailed File Share                                    |             497 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Logon                                                  |             385 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Group Membership                                       |             363 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Logoff                                                 |             335 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Sensitive Privilege Use                                |             315 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Process Creation                                       |             312 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Process Termination                                    |             290 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Special Logon                                          |             268 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Other Object Access Events                             |             146 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | SAM                                                    |             127 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Authorization Policy Change                            |              86 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | File Share                                             |              70 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | User Account Management                                |              68 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Kerberos Authentication Service                        |              64 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Kerberos Service Ticket Operations                     |              34 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Security System Extension                              |              27 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | MPSSVC Rule-Level Policy Change                        |              16 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | File System                                            |              11 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Other Logon/Logoff Events                              |              10 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Kernel Object                                          |               6 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Security Group Management                              |               6 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Plug and Play Events                                   |               3 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Credential Validation                                  |               2 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Other System Events                                    |               2 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | System Integrity                                       |               2 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Directory Service Access                               |               1 |
| Microsoft-Windows-Windows Firewall With Advanced Security/Firewall     | Microsoft-Windows-Windows Firewall With Advanced Security  | na                                                     |              16 |
| Microsoft-Windows-WMI-Activity/Operational                             | Microsoft-Windows-WMI-Activity                             | na                                                     |              53 |
| Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational | Microsoft-Windows-TerminalServices-RemoteConnectionManager | na                                                     |               1 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Registry object added or deleted (rule: RegistryEvent) |           19846 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Process accessed (rule: ProcessAccess)                 |           19199 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Image loaded (rule: ImageLoad)                         |           14178 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Network connection detected (rule: NetworkConnect)     |            5951 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Registry value set (rule: RegistryEvent)               |            3522 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Pipe Connected (rule: PipeEvent)                       |            1369 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | File created (rule: FileCreate)                        |            1346 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Process Create (rule: ProcessCreate)                   |             308 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Process terminated (rule: ProcessTerminate)            |             243 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | RawAccessRead detected (rule: RawAccessRead)           |             182 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Pipe Created (rule: PipeEvent)                         |             139 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | File stream created (rule: FileCreateStreamHash)       |              38 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | File creation time changed (rule: FileCreateTime)      |              28 |
| Microsoft-Windows-PowerShell/Operational                               | Microsoft-Windows-PowerShell                               | Executing Pipeline                                     |           15635 |
| Microsoft-Windows-PowerShell/Operational                               | Microsoft-Windows-PowerShell                               | Starting Command                                       |             297 |
| Microsoft-Windows-PowerShell/Operational                               | Microsoft-Windows-PowerShell                               | Stopping Command                                       |             289 |
| Microsoft-Windows-PowerShell/Operational                               | Microsoft-Windows-PowerShell                               | Execute a Remote Command                               |             140 |
| Microsoft-Windows-PowerShell/Operational                               | Microsoft-Windows-PowerShell                               | PowerShell Console Startup                             |              24 |
| Microsoft-Windows-PowerShell/Operational                               | Microsoft-Windows-PowerShell                               | PowerShell Named Pipe IPC                              |              14 |
| Microsoft-Windows-Bits-Client/Operational                              | Microsoft-Windows-Bits-Client                              | na                                                     |               2 |

## Playbook

[apt3_mordor_playbook.xlsx](scope/apt3_mordor_playbook.xlsx)

## References

https://attack.mitre.org/docs/APT3_Adversary_Emulation_Plan.pdf
https://attackevals.mitre.org/methodology/round1/scope.html
https://attackevals.mitre.org/evaluations/microsoft.1.apt3.1/microsoft.1.apt3.1_overview