# Covenant Ldap Search Request Domain Admins

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-200806130039 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2020/08/06 |
| platform              | Windows |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | [] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/discovery/covenant_ldap_searchrequest_domainadmins.cap |
| References        | None |

## Dataset Description
This dataset represents a threat actor enumerating the domain admins group in an environment.

## Adversary View
```
[08/06/2020 17:00:59 UTC] GetDomainGroup completed

(wardog) > GetDomainGroup /identities:"Domain Admins"

samaccountname: Domain Admins

samaccounttype: GROUP_OBJECT

distinguishedname: CN=Domain Admins,CN=Users,DC=theshire,DC=local

cn: Domain Admins

objectsid: S-1-5-21-1363495622-3806888128-621328882-512

grouptype: 0

admincount: 1

name: Domain Admins

description: Designated administrators of the domain

memberof: CN=Denied RODC Password Replication Group,CN=Users,DC=theshire,DC=local, CN=Administrators,CN=Builtin,DC=theshire,DC=local

useraccountcontrol: 0

badpasswordtime: 1/1/0001 12:00:00 AM

pwdlastset: 1/1/0001 12:00:00 AM

whencreated: 8/6/2020 1:16:12 AM

whenchanged: 8/6/2020 1:31:21 AM

accountexpires: 1/1/0001 12:00:00 AM

lastlogon: 1/1/0001 12:00:00 AM

lastlogoff: 1/1/0001 12:00:00 AM

objectcategory: CN=Group,CN=Schema,CN=Configuration,DC=theshire,DC=local

usnchanged: 12913

instancetype: 4

objectclass: top, group

iscriticalsystemobject: True

usncreated: 12345

dscorepropagationdata: 8/6/2020 1:31:21 AM, 8/6/2020 1:16:12 AM, 1/1/1601 12:04:16 AM

adspath: LDAP://CN=Domain Admins,CN=Users,DC=theshire,DC=local

objectguid: a5cafdc2-9e14-43bb-8ccb-fccba96e3b2c

lastlogontimestamp: 1/1/0001 12:00:00 AM

------
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/discovery/covenant_ldap_searchrequest_domainadmins.cap"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        