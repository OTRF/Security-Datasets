# Empire Net User Domain Specific

An adversary can gather information about a specific domain user via the net.exe utility

## Technique(s) ID

T1087

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_net_user_domain_specific.tar.gz](./empire_net_user_domain_specific.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18230446

## About this file

| log_name                                   | source_name                              | task                                                   |   record_number |
|--------------------------------------------|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                               | Pipeline Execution Details                             |             440 |
| System                                     | Microsoft-Windows-Directory-Services-SAM | na                                                     |              42 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Filtering Platform Connection                          |             361 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Token Right Adjusted Events                            |              87 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Registry                                               |              24 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Other Object Access Events                             |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing      | SAM                                                    |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Handle Manipulation                                    |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Authorization Policy Change                            |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Detailed File Share                                    |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Group Membership                                       |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Logon                                                  |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Logoff                                                 |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Process Creation                                       |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing      | File Share                                             |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Special Logon                                          |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing      | Process Termination                                    |               2 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity           | na                                                     |               2 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Process accessed (rule: ProcessAccess)                 |             381 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Network connection detected (rule: NetworkConnect)     |             158 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Image loaded (rule: ImageLoad)                         |             101 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Registry object added or deleted (rule: RegistryEvent) |              78 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Pipe Connected (rule: PipeEvent)                       |              27 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | File created (rule: FileCreate)                        |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Process Create (rule: ProcessCreate)                   |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Process terminated (rule: ProcessTerminate)            |               2 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon                 | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell             | Executing Pipeline                                     |             364 |

## Attacker Activity

```
(Empire: TKV35P8X) > shell net user pgustavo /domain
[*] Tasked TKV35P8X to run TASK_SHELL
[*] Agent TKV35P8X tasked with task ID 38
(Empire: TKV35P8X) > The request will be processed at a domain controller for domain shire.com.

User name                    pgustavo
Full Name                    Pedro Gustavo
Comment                      
User's comment               
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            1/14/2019 1:20:18 PM
Password expires             Never
Password changeable          1/15/2019 1:20:18 PM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script                 
User profile                 
Home directory               
Last logon                   5/18/2019 5:32:46 PM

Logon hours allowed          All

Local Group Memberships      *SG DL shire Workstati
Global Group memberships     *Domain Users         *Domain Admins        
The command completed successfully.


..Command execution completed.

(Empire: TKV35P8X) >
```