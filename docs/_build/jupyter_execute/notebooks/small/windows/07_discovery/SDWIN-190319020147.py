# Empire Net Local Administrators Group

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-190319020147 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2019/03/19 |
| platform              | Windows |
| Tactic(s)             | ['[TA0007](https://attack.mitre.org/tactics/TA0007)'] |
| Technique(s)          | ['[T1069.001](https://attack.mitre.org/techniques/T1069/001)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | [None] |
| Dataset Host           | ['https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/discovery/host/empire_net_local_admins.tar.gz'] |
| References        | None |

## Dataset Description
This dataset represents adversaries enumerating members of the local Administratrors group via the net.exe utility

## Adversary View
```
(Empire: FD6A3MGY) >   
[*] Tasked FD6A3MGY to run TASK_SHELL
[*] Agent FD6A3MGY tasked with task ID 4
(Empire: FD6A3MGY) > Alias name     Administrators
Comment        

Members

-------------------------------------------------------------------------------
Administrator
Pedro
SHIRE\Domain Admins
SHIRE\SG DL shire Workstation Administrators
The command completed successfully.

..Command execution completed.

(Empire: FD6A3MGY) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/discovery/host/empire_net_local_admins.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        