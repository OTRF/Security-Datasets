# Covenant WMI Query and Execute

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-200806101439 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2020/08/06 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Covenant |
| Simulation Script | https://github.com/cobbr/Covenant/blob/19e4a17048ade1b854241bb5d938398860ab5981/Covenant/Data/Tasks/GhostPack.yaml |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_sharpwmi_dcerpc_wmi_execquery_execmethod.zip |

## Dataset Description
This dataset represents a threat actor querying and executing commands via WMI over the network.

## Adversary View
```
(wardog) > SharpWMI /command:"action=terminate process=PID|name computername=WORKSTATION6"
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_sharpwmi_dcerpc_wmi_execquery_execmethod.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        
