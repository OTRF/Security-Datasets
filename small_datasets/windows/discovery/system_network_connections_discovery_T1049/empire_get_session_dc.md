# Empire Get Session DC

Execute the NetSessionEnum Win32API call to query a given host for active sessions on the host.

## Technique(s) ID

T1049

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_get_session_dc.tar.gz](./empire_get_session_dc.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-19005609

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |             659 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |               8 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             170 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |              82 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              24 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kerberos Service Ticket Operations                     |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kerberos Authentication Service                        |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               1 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             374 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             162 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             103 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              20 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |               2 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             562 |

## Attacker Activity

```
(Empire: H3DKB8SA) > usemodule situational_awareness/network/powerview/get_session
(Empire: powershell/situational_awareness/network/powerview/get_session) > info

              Name: Get-NetSession
            Module: powershell/situational_awareness/network/powerview/get_session
        NeedsAdmin: False
         OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: True
   OutputExtension: None

Authors:
  @harmj0y

Description:
  Execute the NetSessionEnum Win32API call to query a given
  host for active sessions on the host. Part of PowerView.

Comments:
  https://github.com/PowerShellMafia/PowerSploit/blob/dev/Reco
  n/

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  ComputerName False       localhost                 The hostname or IP to query for local   
                                                     group users.                            
  Agent        True        H3DKB8SA                  Agent to run module on.                 

(Empire: powershell/situational_awareness/network/powerview/get_session) > set ComputerName HFDC01
(Empire: powershell/situational_awareness/network/powerview/get_session) > execute
[*] Tasked H3DKB8SA to run TASK_CMD_JOB
[*] Agent H3DKB8SA tasked with task ID 19
[*] Tasked agent H3DKB8SA to run module powershell/situational_awareness/network/powerview/get_session
(Empire: powershell/situational_awareness/network/powerview/get_session) > Job started: VMY6RB

CName           UserName   Time IdleTime ComputerName
-----           --------   ---- -------- ------------
\\172.18.39.106 nmartha       1        1 HFDC01      
\\172.18.39.106 pgustavo 352718       55 HFDC01      

Get-NetSession completed!

(Empire: powershell/situational_awareness/network/powerview/get_session) >
```