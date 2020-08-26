# Covenant Service Query with QueryServiceStatus

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-200805034820 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2020/08/05 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Covenant |
| Simulation Script | https://github.com/cobbr/Covenant/blob/19e4a17048ade1b854241bb5d938398860ab5981/Covenant/Data/Tasks/SharpSC.yaml |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_sc_dcerpc_smb_svcctl_QueryServiceStatus.zip |

## Dataset Description
This dataset represents a threat actor with network access to the service control manager (SCM) service over SMB of another enpoint in the network executing the QueryServiceStatus method to get information about a specific service.

## Adversary View
```
sc.exe \\WORKSTATION6 query ikeext
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_sc_dcerpc_smb_svcctl_QueryServiceStatus.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        