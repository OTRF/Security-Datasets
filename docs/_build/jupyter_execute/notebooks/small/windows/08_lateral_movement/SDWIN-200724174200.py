# WMI Event Subscription

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-200724174200 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2020/07/24 |
| platform              | Windows |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | [] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_wmi_event_subscription.zip |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_wmi_event_subscription_WORKSTATION5_2020-09-01103012.cap |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_wmi_event_subscription_WORKSTATION6_2020-09-01103012.cap |
| References        | ['https://www.mdsec.co.uk/2020/09/i-like-to-move-it-windows-lateral-movement-part-1-wmi-event-subscription/'] |

## Dataset Description
This dataset represents adversaries using WMI event subscriptions to move laterally.

## Adversary View
```
None
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_wmi_event_subscription.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        