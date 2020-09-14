# Empire Wdigest Downgrade

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-190518201922 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2019/05/18 |
| platform              | Windows |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | [] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/defense_evasion/empire_wdigest_downgrade.tar.gz |
| References        | None |

## Dataset Description
This dataset represents adversaries setting the UseLogonCredential property value from HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest key to 1 to enable plain text passwords.

## Adversary View
```
None
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/defense_evasion/empire_wdigest_downgrade.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        