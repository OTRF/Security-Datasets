# WMI Event Subscription

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-200724174200 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2020/07/24 |
| platform              | Windows |
| Tactic(s)             | ['[TA0002](https://attack.mitre.org/tactics/TA0002)', '[TA0008](https://attack.mitre.org/tactics/TA0008)'] |
| Technique(s)          | ['[T1047](https://attack.mitre.org/techniques/T1047)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | ['https://3xpl01tc0d3r.blogspot.com/2020/02/gadgettojscript-covenant-donut.html'] |
| Dataset Host           | ['https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/host/covenant_wmi_event_subscription.zip'] |
| Dataset Network           | ['https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/network/covenant_wmi_event_subscription_WORKSTATION5_2020-09-01103012.cap', 'https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/network/covenant_wmi_event_subscription_WORKSTATION6_2020-09-01103012.cap'] |
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

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/host/covenant_wmi_event_subscription.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        