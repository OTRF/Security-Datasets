# Empire Net User Domain Specific

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518230446 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script |  |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/discovery/empire_net_user_domain_specific.tar.gz |

## Dataset Description
This dataset represents adversaries enumerating a specific domain user via the net.exe utility

## Adversary View
```
(Empire: TKV35P8X) > shell net user pgustavo /domain
[*] Tasked TKV35P8X to run TASK_SHELL
[*] Agent TKV35P8X tasked with task ID 38
(Empire: TKV35P8X) > The request will be processed at a domain controller for domain shire.com.

User name                    pgustavo
Full Name                    Pedro Gustavo
Comment                      
User's comment               
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            1/14/2019 1:20:18 PM
Password expires             Never
Password changeable          1/15/2019 1:20:18 PM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script                 
User profile                 
Home directory               
Last logon                   5/18/2019 5:32:46 PM

Logon hours allowed          All

Local Group Memberships      *SG DL shire Workstati
Global Group memberships     *Domain Users         *Domain Admins        
The command completed successfully.


..Command execution completed.

(Empire: TKV35P8X) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/discovery/empire_net_user_domain_specific.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT channel, COUNT(1)
FROM mordorTable
GROUP BY channel
    '''
)
df.show(10,False)
        