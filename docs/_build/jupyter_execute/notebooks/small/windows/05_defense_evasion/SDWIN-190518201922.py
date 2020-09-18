# Empire Wdigest Downgrade

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-190518201922 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2019/05/18 |
| platform              | Windows |
| Tactic(s)             | ['[TA0005](https://attack.mitre.org/tactics/TA0005)'] |
| Technique(s)          | ['[T1112](https://attack.mitre.org/techniques/T1112)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | ['https://github.com/EmpireProject/Empire/blob/dev/lib/modules/powershell/management/wdigest_downgrade.py'] |
| Dataset Host           | ['https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/defense_evasion/host/empire_wdigest_downgrade.tar.gz'] |
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

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/defense_evasion/host/empire_wdigest_downgrade.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        