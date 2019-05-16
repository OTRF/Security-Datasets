
# Empire Net User

An adversary can enumerate all users that belong to a domain via the net.exe utility

## Technique(s) ID

T1087

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_net_user_domain.tar.gz](./empire_net_user_domain.tar.gz)

## Network Environment

Shire

## Time Taken

2019-03-19021158

## About this file

| log_name                                 | source_name                         | task                                                   |   record_number |
|------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | PowerShell                          | Pipeline Execution Details                             |             114 |
| Security                                 | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |              55 |
| Security                                 | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |              21 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logoff                                                 |               9 |
| Security                                 | Microsoft-Windows-Security-Auditing | Group Membership                                       |               6 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logon                                                  |               6 |
| Security                                 | Microsoft-Windows-Security-Auditing | Special Logon                                          |               3 |
| Security                                 | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |               1 |
| Security                                 | Microsoft-Windows-Security-Auditing | File Share                                             |               1 |
| Security                                 | Microsoft-Windows-Security-Auditing | Process Creation                                       |               1 |
| Security                                 | Microsoft-Windows-Security-Auditing | SAM                                                    |               1 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |              96 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |              94 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |              44 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              23 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |              17 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               4 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |               3 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |               1 |
| Microsoft-Windows-PowerShell/Operational | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |              93 |

## Empire Activity

```
shell net user /domain
```

```
[*] Tasked FD6A3MGY to run TASK_SHELL
[*] Agent FD6A3MGY tasked with task ID 6
(Empire: FD6A3MGY) > The request will be processed at a domain controller for domain shire.com.


User accounts for \\HFDC01.shire.com

-------------------------------------------------------------------------------
Administrator            DefaultAccount           Guest                    
krbtgt                   lrodriguez               Mmidge                   
nmartha                  oda                      pgustavo                 
ttest                    WECserver                
The command completed successfully.


..Command execution completed.

(Empire: FD6A3MGY) >
```