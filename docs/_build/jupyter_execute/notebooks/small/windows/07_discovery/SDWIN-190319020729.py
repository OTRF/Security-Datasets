# Empire Net All Local Users

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-190319020729 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2019/03/19 |
| platform              | Windows |
| Tactic(s)             | ['[TA0007](https://attack.mitre.org/tactics/TA0007)'] |
| Technique(s)          | ['[T1087.001](https://attack.mitre.org/techniques/T1087/001)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | [None] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/discovery/empire_net_user.tar.gz |
| References        | None |

## Dataset Description
This dataset represents adversaries enumerating all local users via the net.exe utility

## Adversary View
```
(Empire: FD6A3MGY) >  shell net user
[*] Tasked FD6A3MGY to run TASK_SHELL
[*] Agent FD6A3MGY tasked with task ID 5
(Empire: FD6A3MGY) > User accounts for \\IT001

-------------------------------------------------------------------------------
Administrator            DefaultAccount           Guest                    
Pedro                    WDAGUtilityAccount       
The command completed successfully.


..Command execution completed.

(Empire: FD6A3MGY) > 
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/discovery/empire_net_user.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        