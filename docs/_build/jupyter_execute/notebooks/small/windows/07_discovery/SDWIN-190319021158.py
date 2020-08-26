# Empire Net All User Domain

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-190319021158 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/03/19 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | None |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/discovery/empire_net_user_domain.tar.gz |

## Dataset Description
This dataset represents adversaries enumerating all users that belong to a domain via the net.exe utility

## Adversary View
```
(Empire: FD6A3MGY) >shell net user /domain
[*] Tasked FD6A3MGY to run TASK_SHELL
[*] Agent FD6A3MGY tasked with task ID 6
(Empire: FD6A3MGY) > The request will be processed at a domain controller for domain shire.com.


User accounts for \\HFDC01.shire.com

-------------------------------------------------------------------------------
Administrator            DefaultAccount           Guest                    
krbtgt                   lrodriguez               Mmidge                   
nmartha                  oda                      pgustavo                 
ttest                    WECserver                
The command completed successfully.


..Command execution completed.

(Empire: FD6A3MGY) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/discovery/empire_net_user_domain.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        
