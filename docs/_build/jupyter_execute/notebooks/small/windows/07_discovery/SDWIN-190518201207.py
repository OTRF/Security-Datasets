# Empire Net Domain Admins Group

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-190518201207 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | None |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/discovery/empire_net_domain_admins.tar.gz |

## Dataset Description
This dataset represents adversaries enumerating members of the "Domain Admins" active directory group via net.exe.

## Adversary View
```
(Empire: TKV35P8X) > shell net group "Domain Admins" /domain
[*] Tasked TKV35P8X to run TASK_SHELL
[*] Agent TKV35P8X tasked with task ID 14
(Empire: TKV35P8X) > The request will be processed at a domain controller for domain shire.com.

Group name     Domain Admins
Comment        Designated administrators of the domain

Members

-------------------------------------------------------------------------------
Administrator            Mmidge                   oda                      
pgustavo                 
The command completed successfully.

..Command execution completed.

(Empire: TKV35P8X) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/discovery/empire_net_domain_admins.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        