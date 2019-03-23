
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

| log_name                                 | task                                                   |   events_count  |
|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | Pipeline Execution Details                             |             114 |
| Security                                 | Token Right Adjusted Events                            |              55 |
| Security                                 | Filtering Platform Connection                          |              21 |
| Security                                 | Logoff                                                 |               9 |
| Security                                 | Group Membership                                       |               6 |
| Security                                 | Logon                                                  |               6 |
| Security                                 | Special Logon                                          |               3 |
| Security                                 | Detailed File Share                                    |               1 |
| Security                                 | File Share                                             |               1 |
| Security                                 | Process Creation                                       |               1 |
| Security                                 | SAM                                                    |               1 |
| Microsoft-Windows-Sysmon/Operational     | Process accessed (rule: ProcessAccess)                 |              96 |
| Microsoft-Windows-Sysmon/Operational     | Image loaded (rule: ImageLoad)                         |              94 |
| Microsoft-Windows-Sysmon/Operational     | Network connection detected (rule: NetworkConnect)     |              44 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Connected (rule: PipeEvent)                       |              23 |
| Microsoft-Windows-Sysmon/Operational     | Registry object added or deleted (rule: RegistryEvent) |              17 |
| Microsoft-Windows-Sysmon/Operational     | Process Create (rule: ProcessCreate)                   |               4 |
| Microsoft-Windows-Sysmon/Operational     | File created (rule: FileCreate)                        |               3 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-Sysmon/Operational     | Registry value set (rule: RegistryEvent)               |               1 |
| Microsoft-Windows-PowerShell/Operational | Executing Pipeline                                     |              93 |

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