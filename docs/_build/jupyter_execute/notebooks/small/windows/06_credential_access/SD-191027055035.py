# Remote Interactive Task Manager Lsass dump

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-191027055035 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/10/27 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | Interactive Session |
| Simulation Tool   | Remote Desktop Protocol |
| Simulation Script |  |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/small_datasets/windows/credential_access/remoteinteractive_taskmngr_lsass_dump.tar.gz |

## Dataset Description
This dataset represents adversaries using RDP and task manager interactively and dump the memory space of lsass.

## Adversary View
```
RDP to victim
Open Windows Task Manager as Administrator
Select lsass.exe
Right-click on lsass.exe and select “Create dump file”
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/small_datasets/windows/credential_access/remoteinteractive_taskmngr_lsass_dump.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        