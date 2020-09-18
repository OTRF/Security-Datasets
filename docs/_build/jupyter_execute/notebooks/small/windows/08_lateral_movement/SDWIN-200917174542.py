# DCOM ExecuteExcel4macro

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-200917174542 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2020/09/18 |
| platform              | Windows |
| Tactic(s)             | ['[TA0008](https://attack.mitre.org/tactics/TA0008)'] |
| Technique(s)          | ['[T1021.003](https://attack.mitre.org/techniques/T1021/003)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | ['https://github.com/cobbr/Covenant/blob/7555b19ffb9401c0e37094c25e404a640b1688d7/Covenant/Data/Tasks/SharpSploit.Execution.yaml#L96'] |
| Dataset Host           | ['https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/host/covenant_dcom_executeexcel4macro_allowed.zip', 'https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/host/covenant_dcom_executeexcel4macro_blocked.zip'] |
| Dataset Network           | ['https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/network/covenant_dcom_executeexcel4macro_allowed.zip', 'https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/network/covenant_dcom_executeexcel4macro_blocked.zip'] |
| References        | ['https://www.mdsec.co.uk/2020/09/i-like-to-move-it-windows-lateral-movement-part-2-dcom/'] |

## Dataset Description
This dataset represents adversaries leveraging the COM Method ExecuteExcel4Macro over DCOM to execute Excel4 macros remotely

## Adversary View
```
(wardog) > ShellCmd /shellcommand:"C:\Users\pgustavo\Desktop\MoveExcel4.exe 172.18.39.6
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/host/covenant_dcom_executeexcel4macro_allowed.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        