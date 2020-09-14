# Covenant SMB Create Request

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-200806015757 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2020/08/06 |
| platform              | Windows |
| Tactic(s)             | ['[TA0008](https://attack.mitre.org/tactics/TA0008)'] |
| Technique(s)          | ['[T1021.002](https://attack.mitre.org/techniques/T1021/002)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | [None] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_copy_smb_create_request.zip |
| References        | None |

## Dataset Description
This dataset represents a threat actor copying a file over SMB.

## Adversary View
```
(wardog) > copy
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_copy_smb_create_request.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        