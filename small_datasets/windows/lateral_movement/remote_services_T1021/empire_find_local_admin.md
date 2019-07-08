# Empire Find Local Admin Access

Finds machines on the local domain where the current user has local administrator access. It uses the OpenSCManagerW Win32API call to establish
a handle to the remote host. If this succeeds, the current user context has local administrator acess to the target.

## Technique(s) ID

T1021

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_find_local_admin.tar.gz](./empire_find_local_admin.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18224039

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |            1100 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |              40 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               9 |
| System                                     | Service Control Manager             | na                                                     |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             246 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             173 |
| Security                                   | Microsoft-Windows-Security-Auditing | Removable Storage                                      |             130 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              52 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              44 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |              16 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |              16 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |              16 |
| Security                                   | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |              15 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |              14 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | File System                                            |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             290 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             214 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             146 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             145 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              48 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              39 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |               6 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               2 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |               1 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |             986 |

## Attacker Activity

```
(Empire: V6W3TH8Y) > usemodule situational_awareness/network/powerview/find_localadmin_access
(Empire: powershell/situational_awareness/network/powerview/find_localadmin_access) > info

              Name: Find-LocalAdminAccess
            Module: powershell/situational_awareness/network/powerview/find_localadmin_access
        NeedsAdmin: False
         OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: True
   OutputExtension: None

Authors:
  @harmj0y

Description:
  Finds machines on the local domain where the current user
  has local administrator access. Part of PowerView.

Comments:
  https://github.com/PowerShellMafia/PowerSploit/blob/dev/Reco
  n/

Options:

  Name                    Required    Value                     Description
  ----                    --------    -------                   -----------
  ComputerName            False                                 Hosts to enumerate, comma separated.    
  SearchScope             False                                 Specifies the scope to search under,    
                                                                Base/OneLevel/Subtree (default of       
                                                                Subtree)                                
  ComputerSiteName        False                                 Search computers in the specific AD site
                                                                name, wildcards accepted.               
  Server                  False                                 Specifies an active directory server    
                                                                (domain controller) to bind to          
  Tombstone               False                                 Switch. Specifies that the search should
                                                                also return deleted/tombstoned objects. 
  ComputerOperatingSystem False                                 Searches computers with a specific      
                                                                operating system. Wildcards accepted.   
  ResultPageSize          False                                 Specifies the PageSize to set for the   
                                                                LDAP searcher object.                   
  ComputerDomain          False                                 Specifies the domain to query for       
                                                                computers, defaults to the current      
                                                                domain.                                 
  ComputerSearchBase      False                                 Specifies the LDAP source to search     
                                                                through for computers                   
  ServerTimeLimit         False                                 Specifies the maximum amount of time the
                                                                server spends searching. Default of 120 
                                                                seconds.                                
  ComputerServicePack     False                                 Search computers with a specific service
                                                                pack                                    
  Agent                   True        V6W3TH8Y                  Agent to run module on.                 
  CheckShareAccess        False                                 Switch. Only display found shares that  
                                                                the local user has access to.           
  ComputerLDAPFilter      False                                 Specifies an LDAP query string that is  
                                                                used to search for computer objects.    

(Empire: powershell/situational_awareness/network/powerview/find_localadmin_access) > execute
[*] Tasked V6W3TH8Y to run TASK_CMD_JOB
[*] Agent V6W3TH8Y tasked with task ID 11
[*] Tasked agent V6W3TH8Y to run module powershell/situational_awareness/network/powerview/find_localadmin_access
(Empire: powershell/situational_awareness/network/powerview/find_localadmin_access) > Job started: X3U8SY
HFDC01.shire.com
IT001.shire.com

Find-LocalAdminAccess completed!


(Empire: powershell/situational_awareness/network/powerview/find_localadmin_access) > 
```