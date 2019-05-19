# Empire Net Start

An adversary can enumerate the services available on the system via net.exe

## Technique(s) ID

T1007

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_net_start.tar.gz](./empire_net_start.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18220124

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |             283 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |              90 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |              44 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              12 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               1 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             153 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |              77 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |              52 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |              33 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              13 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               2 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             235 |

## Attacker Activity

```
(Empire: V6W3TH8Y) > shell net start
[*] Tasked V6W3TH8Y to run TASK_SHELL
[*] Agent V6W3TH8Y tasked with task ID 8
(Empire: V6W3TH8Y) > These Windows services are started:

   Application Information
   AVCTP service
   Background Intelligent Transfer Service
   Background Tasks Infrastructure Service
   Base Filtering Engine
   Certificate Propagation
   Clipboard User Service_c5665
   CNG Key Isolation
   COM+ Event System
   Connected Devices Platform Service
   Connected Devices Platform User Service_c5665
   Connected User Experiences and Telemetry
   Contact Data_c5665
   CoreMessaging
   Credential Manager
   Cryptographic Services
   Data Sharing Service
   Data Usage
   DCOM Server Process Launcher
   DHCP Client
   Diagnostic Policy Service
   Diagnostic Service Host
   Distributed Link Tracking Client
   DNS Client
   Geolocation Service
   IKE and AuthIP IPsec Keying Modules
   IP Helper
   IPsec Policy Agent
   Local Session Manager
   Netlogon
   Network Connection Broker
   Network List Service
   Network Location Awareness
   Network Store Interface Service
   Plug and Play
   Power
   Print Spooler
   Program Compatibility Assistant Service
   Remote Desktop Configuration
   Remote Desktop Services
   Remote Desktop Services UserMode Port Redirector
   Remote Procedure Call (RPC)
   RPC Endpoint Mapper
   Secondary Logon
   Security Accounts Manager
   Security Center
   Server
   Shell Hardware Detection
   SSDP Discovery
   State Repository Service
   Storage Service
   Sync Host_c5665
   Sysmon
   System Event Notification Service
   System Events Broker
   System Guard Runtime Monitor Broker
   Task Scheduler
   TCP/IP NetBIOS Helper
   Themes
   Time Broker
   Touch Keyboard and Handwriting Panel Service
   Update Orchestrator Service
   User Data Access_c5665
   User Data Storage_c5665
   User Manager
   User Profile Service
   WarpJITSvc
   Web Account Manager
   Windows Audio
   Windows Audio Endpoint Builder
   Windows Connection Manager
   Windows Defender Firewall
   Windows Event Log
   Windows Font Cache Service
   Windows License Manager Service
   Windows Licensing Monitoring Service
   Windows Management Instrumentation
   Windows Push Notifications System Service
   Windows Push Notifications User Service_c5665
   Windows Remote Management (WS-Management)
   Windows Search
   Windows Security Service
   Windows Time
   WinHTTP Web Proxy Auto-Discovery Service
   Workstation

The command completed successfully.


..Command execution completed.

(Empire: V6W3TH8Y) >
```