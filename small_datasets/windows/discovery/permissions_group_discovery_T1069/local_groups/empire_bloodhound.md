
# Empire Bloodhund

An adversary can enumerate members of the local groups via LDAP

## Technique(s) ID

T1069

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_bloodhound.tar.gz](./empire_bloodhound.tar.gz)

## Network Environment

Shire

## Time Taken

2019-03-19031847

## About this file

| log_name                                 | task                                                   |   record_number |
|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | Pipeline Execution Details                             |             417 |
| Windows PowerShell                       | Provider Lifecycle                                     |              48 |
| Windows PowerShell                       | Engine Lifecycle                                       |              11 |
| Security                                 | Filtering Platform Connection                          |             264 |
| Security                                 | Token Right Adjusted Events                            |             171 |
| Security                                 | Detailed File Share                                    |             108 |
| Security                                 | Group Membership                                       |              28 |
| Security                                 | Logon                                                  |              28 |
| Security                                 | Logoff                                                 |              25 |
| Security                                 | Special Logon                                          |              11 |
| Security                                 | File Share                                             |               4 |
| Security                                 | Sensitive Privilege Use                                |               4 |
| Security                                 | Kerberos Service Ticket Operations                     |               3 |
| Security                                 | SAM                                                    |               2 |
| Security                                 | Authorization Policy Change                            |               1 |
| Security                                 | Process Creation                                       |               1 |
| Security                                 | Security Group Management                              |               1 |
| Microsoft-Windows-Sysmon/Operational     | Image loaded (rule: ImageLoad)                         |             375 |
| Microsoft-Windows-Sysmon/Operational     | Process accessed (rule: ProcessAccess)                 |             308 |
| Microsoft-Windows-Sysmon/Operational     | Network connection detected (rule: NetworkConnect)     |             206 |
| Microsoft-Windows-Sysmon/Operational     | File created (rule: FileCreate)                        |              69 |
| Microsoft-Windows-Sysmon/Operational     | Registry object added or deleted (rule: RegistryEvent) |              64 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Connected (rule: PipeEvent)                       |              54 |
| Microsoft-Windows-Sysmon/Operational     | Process Create (rule: ProcessCreate)                   |               9 |
| Microsoft-Windows-Sysmon/Operational     | RawAccessRead detected (rule: RawAccessRead)           |               8 |
| Microsoft-Windows-Sysmon/Operational     | Registry value set (rule: RegistryEvent)               |               6 |
| Microsoft-Windows-PowerShell/Operational | Executing Pipeline                                     |             383 |

## Empire Activity

```
usemodule situational_awareness/network/bloodhound
```

```
(Empire: powershell/situational_awareness/network/bloodhound) > info

              Name: Invoke-BloodHound
            Module: powershell/situational_awareness/network/bloodhound
        NeedsAdmin: False
         OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: True
   OutputExtension: None

Authors:
  @harmj0y
  @_wald0
  @cptjesus

Description:
  Execute BloodHound data collection.

Comments:
  https://bit.ly/getbloodhound

Options:

  Name                Required    Value                     Description
  ----                --------    -------                   -----------
  ComputerName        False                                 Array of one or more computers to       
                                                            enumerate                               
  UserADSPath         False                                 The LDAP source to search through for   
                                                            users/groups, e.g.                      
                                                            "LDAP://OU=secret,DC=testlab,DC=local"  
  DomainController    False                                 Domain controller to reflect LDAP       
                                                            queries through.                        
  ComputerADSpath     False                                 The LDAP source to search through for   
                                                            computers, e.g.                         
                                                            "LDAP://OU=secret,DC=testlab,DC=local"  
  SkipGCDeconfliction False                                 Switch. Skip global catalog enumeration 
                                                            for session deconfliction               
  Domain              False                                 The domain to use for the query,        
                                                            defaults to the current domain.         
  Agent               True        FD6A3MGY                  Agent to run module on.                 
  URI                 False                                 The BloodHound neo4j URL location       
                                                            (http://host:port/)                     
  GlobalCatalog       False                                 The global catalog location to resolve  
                                                            user memberships from.                  
  Threads             True        20                        The maximum concurrent threads to       
                                                            execute.                                
  CollectionMethod    True        Default                   The method to collect data. 'Group',    
                                                            'ComputerOnly', 'LocalGroup',           
                                                            'GPOLocalGroup', 'Session', 'LoggedOn', 
                                                            'Trusts, 'Stealth', or 'Default'.       
  Throttle            True        1000                      The number of cypher queries to queue up
                                                            for neo4j RESTful API ingestion.        
  UserPass            False                                 The "user:password" for the BloodHound  
                                                            neo4j instance                          
  SearchForest        False                                 Switch. Search all domains in the       
                                                            forest.                                 
  CSVFolder           False       $(Get-Location)           The CSV folder to use for output,       
                                                            defaults to the current folder location.
  CSVPrefix           False                                 A prefix for all CSV files.             

(Empire: powershell/situational_awareness/network/bloodhound) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked FD6A3MGY to run TASK_CMD_JOB
[*] Agent FD6A3MGY tasked with task ID 16
[*] Tasked agent FD6A3MGY to run module powershell/situational_awareness/network/bloodhound
(Empire: powershell/situational_awareness/network/bloodhound) > Job started: ZPHYFE

(Empire: powershell/situational_awareness/network/bloodhound) > Writing output to CSVs in: C:\Users\pgustavo\
Done writing output to CSVs in: C:\Users\pgustavo\



Invoke-BloodHound completed!


(Empire: powershell/situational_awareness/network/bloodhound) > 
```