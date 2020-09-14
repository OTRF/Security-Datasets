# Covenant PsRemoting Command

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-200806115603 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2020/08/06 |
| platform              | Windows |
| Tactic(s)             | ['[TA0008](https://attack.mitre.org/tactics/TA0008)'] |
| Technique(s)          | ['[T1021.006](https://attack.mitre.org/techniques/T1021/006)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | ['https://github.com/cobbr/Covenant/blob/master/Covenant/Data/Tasks/SharpSploit.LateralMovement.yaml'] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_psremoting_command.zip |
| References        | None |

## Dataset Description
This dataset represents a threat actor leveraging WinRM to execute code remotely.

## Adversary View
```
[08/06/2020 15:56:13 UTC] PowerShellRemotingCommand completed

(wardog) > PowerShellRemotingCommand /computername:"WORKSTATION6" /command:"get-process" /domain:"theshire.local" /username:"pgustavo" /password:"W1n1!2019"

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName                     PSComputerName                

-------  ------    -----      -----     ------     --  -- -----------                     --------------                

    259      17     4712      24656       0.58   7996   2 ApplicationFrameHost            WORKSTATION6                  

    118       7     6396      10664       0.03   1356   0 conhost                         WORKSTATION6                  

    612      22     1720       4900       0.69    524   0 csrss                           WORKSTATION6                  

    168      11     1544       4164       0.06    604   1 csrss                           WORKSTATION6                  

    401      14     1664       5168       6.94   2528   2 csrss                           WORKSTATION6                  

    384      15     3648      13620       5.97   2888   2 ctfmon                          WORKSTATION6                  

    135       8     2016      12064       0.19   4952   2 dllhost                         WORKSTATION6                  

    235      22     5100      14172       0.33   5028   2 dllhost                         WORKSTATION6                  

    242      16     3776      12940       0.33   7864   2 dllhost                         WORKSTATION6                  

    665      24    17888      38728       0.27    588   1 dwm                             WORKSTATION6                  

    721      32    31996      69820      19.36   2512   2 dwm                             WORKSTATION6                  

  1961      75    43016     122660      26.72   4156   2 explorer                        WORKSTATION6                  

    32       5     1188       2072       0.03    880   1 fontdrvhost                     WORKSTATION6                  

    32       5     1260       2172       0.08    884   0 fontdrvhost                     WORKSTATION6                  

    32       7     3092       5864       0.75   4084   2 fontdrvhost                     WORKSTATION6                  

      0       0       60          8                 0   0 Idle                            WORKSTATION6                  

    632      34    17136      49032       0.48    608   1 LogonUI                         WORKSTATION6
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_psremoting_command.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        