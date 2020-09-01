# WMI Event Subscription

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-200724174200 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2020/07/24 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | manual |
| Simulation Tool   | shell |
| Simulation Script | https://3xpl01tc0d3r.blogspot.com/2020/02/gadgettojscript-covenant-donut.html |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/wmi_event_subscription.pcapng |

## Dataset Description
This dataset represents adversaries using WMI subscriptions remotely for persistence and execution

## Adversary View
```
None
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/wmi_event_subscription.pcapng"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        