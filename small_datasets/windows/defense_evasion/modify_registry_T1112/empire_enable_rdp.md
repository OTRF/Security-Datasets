# Empire Enable RDP

Enables RDP on the remote machine and adds a firewall exception.

## Technique(s) ID

T1112

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_enable_rdp.tar.gz](./empire_enable_rdp.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18203650

## About this file

| log_name                                                               | source_name                                                | task                                                   |   record_number |
|------------------------------------------------------------------------|------------------------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                                                     | PowerShell                                                 | Pipeline Execution Details                             |             169 |
| System                                                                 | Microsoft-Windows-TerminalServices-RemoteConnectionManager | na                                                     |               1 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Filtering Platform Connection                          |             115 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Token Right Adjusted Events                            |              56 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Registry                                               |              24 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Process Creation                                       |              11 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Authorization Policy Change                            |               9 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Group Membership                                       |               9 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Logon                                                  |               9 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | MPSSVC Rule-Level Policy Change                        |               9 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Special Logon                                          |               7 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Handle Manipulation                                    |               6 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Logoff                                                 |               4 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Process Termination                                    |               4 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Sensitive Privilege Use                                |               3 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Computer Account Management                            |               2 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Other System Events                                    |               2 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | System Integrity                                       |               2 |
| Security                                                               | Microsoft-Windows-Security-Auditing                        | Kerberos Service Ticket Operations                     |               1 |
| Microsoft-Windows-Windows Firewall With Advanced Security/Firewall     | Microsoft-Windows-Windows Firewall With Advanced Security  | na                                                     |               9 |
| Microsoft-Windows-WMI-Activity/Operational                             | Microsoft-Windows-WMI-Activity                             | na                                                     |               1 |
| Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational | Microsoft-Windows-TerminalServices-RemoteConnectionManager | na                                                     |               1 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Registry object added or deleted (rule: RegistryEvent) |             701 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Image loaded (rule: ImageLoad)                         |             481 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Process accessed (rule: ProcessAccess)                 |             452 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Registry value set (rule: RegistryEvent)               |             293 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Network connection detected (rule: NetworkConnect)     |              89 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Pipe Connected (rule: PipeEvent)                       |              18 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | File created (rule: FileCreate)                        |              15 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Process Create (rule: ProcessCreate)                   |              11 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Pipe Created (rule: PipeEvent)                         |               7 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | Process terminated (rule: ProcessTerminate)            |               4 |
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   | RawAccessRead detected (rule: RawAccessRead)           |               3 |
| Microsoft-Windows-PowerShell/Operational                               | Microsoft-Windows-PowerShell                               | Executing Pipeline                                     |             140 |

## Attackers Activity

```
(Empire: TKV35P8X) > usemodule management/enable_rdp*           
(Empire: powershell/management/enable_rdp) > info

              Name: Enable-RDP
            Module: powershell/management/enable_rdp
        NeedsAdmin: True
         OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
   OutputExtension: None

Authors:
  @harmj0y

Description:
  Enables RDP on the remote machine and adds a firewall
  exception.

Options:

  Name  Required    Value                     Description
  ----  --------    -------                   -----------
  Agent True        TKV35P8X                  Agent to run module on.                 

(Empire: powershell/management/enable_rdp) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked TKV35P8X to run TASK_CMD_WAIT
[*] Agent TKV35P8X tasked with task ID 21
[*] Tasked agent TKV35P8X to run module powershell/management/enable_rdp
(Empire: powershell/management/enable_rdp) > The operation completed successfully.


(Empire: powershell/management/enable_rdp) > 
```