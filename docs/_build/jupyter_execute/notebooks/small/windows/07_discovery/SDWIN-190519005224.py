# Empire Get Local Sessions

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-190519005224 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2019/05/19 |
| platform              | Windows |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | [] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/discovery/empire_get_session_local.tar.gz |
| References        | None |

## Dataset Description
This dataset represents adversaries executing the NetSessionEnum Win32API call to query the local host for active sessions

## Adversary View
```
(Empire: H3DKB8SA) > usemodule situational_awareness/network/powerview/get_session
(Empire: powershell/situational_awareness/network/powerview/get_session) > info

              Name: Get-NetSession
            Module: powershell/situational_awareness/network/powerview/get_session
        NeedsAdmin: False
        OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: True
  OutputExtension: None

Authors:
  @harmj0y

Description:
  Execute the NetSessionEnum Win32API call to query a given
  host for active sessions on the host. Part of PowerView.

Comments:
  https://github.com/PowerShellMafia/PowerSploit/blob/dev/Reco
  n/

Options:

  Name         Required    Value                     Description
  ----         --------    -------                   -----------
  ComputerName False       localhost                 The hostname or IP to query for local   
                                                    group users.                            
  Agent        True        H3DKB8SA                  Agent to run module on.                 

(Empire: powershell/situational_awareness/network/powerview/get_session) > set ComputerName HFDC01
(Empire: powershell/situational_awareness/network/powerview/get_session) > execute
[*] Tasked H3DKB8SA to run TASK_CMD_JOB
[*] Agent H3DKB8SA tasked with task ID 19
[*] Tasked agent H3DKB8SA to run module powershell/situational_awareness/network/powerview/get_session
(Empire: powershell/situational_awareness/network/powerview/get_session) > Job started: VMY6RB

CName           UserName   Time IdleTime ComputerName
-----           --------   ---- -------- ------------
\\172.18.39.106 nmartha       1        1 HFDC01      
\\172.18.39.106 pgustavo 352718       55 HFDC01      

Get-NetSession completed!

(Empire: powershell/situational_awareness/network/powerview/get_session) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/discovery/empire_get_session_local.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        