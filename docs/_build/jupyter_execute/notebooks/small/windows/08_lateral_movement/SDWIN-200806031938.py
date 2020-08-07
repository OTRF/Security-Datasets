# Covenant RPC SMB ControlService

## Metadata


|                   |    |
|:------------------|:---|
| id                | SDWIN-200806031938 |
| author            | Roberto Rodriguez @Cyb3rWard0g |
| creation date     | 2020/08/06 |
| platform          | Windows |
| Mordor Environment| Mordor shire |
| Simulation Type   | C2 |
| Simulation Tool   | Covenant |
| Simulation Script | https://github.com/cobbr/Covenant/blob/19e4a17048ade1b854241bb5d938398860ab5981/Covenant/Data/Tasks/SharpSC.yaml |
| Mordor Dataset    | https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/lateral_movement/covenant_sharpsc_dcerpc_smb-svcctl_ControlService.zip |

## Dataset Description
This dataset represents a threat actor with network access to the service control manager (SCM) service over SMB of another enpoint in the network executing ControlService to interact with the service (i.e. stop service)

## Adversary View
```
(wardog) > SharpSC /command:"action=stop computername=WORKSTATION6 service=ikeext"

[*] Attempting to stop service ikeext on WORKSTATION6...

[+] Successfully stopped ikeext on WORKSTATION6!

  DisplayName: IKE and AuthIP IPsec Keying Modules

  ServiceName: ikeext

  Status     : Stopped

  CanStop    : False
  https://github.com/djhohnstein/SharpSC
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/hunters-forge/mordor/master/datasets/small/windows/lateral_movement/covenant_sharpsc_dcerpc_smb-svcctl_ControlService.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        