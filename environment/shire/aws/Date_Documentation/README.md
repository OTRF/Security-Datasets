# Shire AWS Infrastructure

<p align="center"><img src="https://github.com/Cyb3rWard0g/mordor/blob/master/environment/shire/aws/images/Infrastructure.png"></p>
<p align="center"><strong> Infrastructure of Mordor inside of AWS</strong> </p>
Above you will see Mordor’s Infrastructure inside of AWS. The lines represent how the data and logs flow within the environment. The environment is utilizing the Windows Event Collector (WEC) service that pulls the logs from other machines through Subscriptions. After the logs are inside of the WEC Server, they are being forwarded through winlogbeat to HELK. It shoudl be noted as well, that the logs for the host <strong> WECServer.shire.com</strong> will not be forwarded to HELK. This is to reduce dataset sizes. In a real enviroment you WOULD want this host to forward logs to the enviroments SIEM. 

#### *Note*:   You might see AWS events on the endpoints after the lab is built. 

#### For a detailed overview of the AWS Lab, please see below:

## AD Environment:

### 5 Machines:
	1 AD/DC (Active Directory/Domain Controller)
		
	1 WEC (Windows Event Collector)
		
	3 Windows 10 Workstations


## Non-Domain joined machines:
### 3 Ubuntu Machines: 

	1 HELK  (From  project -  https://github.com/Cyb3rWard0g/HELK.git) (Ubuntu 18.04)
		
	1 Apache Guacamole (installed from https://github.com/jsecurity101/ApacheGuacamole. Modification were made to user-mapping.xml to fit this project) (Ubuntu 16.04)
		
	1 Red Team Operator machine (Created for C2’s. Currently only Powershell Empire (https://github.com/EmpireProject/Empire) is the only one on this machine) (Ubuntu 18.04)

## Audit Policies:
Audit policies are pushed out through GPOs within `HFDC1.shire.com`. Registry audit rules are pull from the [Set-AuditRule](https://github.com/hunters-forge/Set-AuditRule) project and pushed out to each machine during the configuration process in Terraform. The list of server and workstation audit policies that were pushed out, can be found:
* [Server Audit Policies](https://github.com/Cyb3rWard0g/mordor/blob/master/environment/shire/aws/Date_Documentation/Server-Audit-Settings.md)

* [Workstation Audit Policies](https://github.com/Cyb3rWard0g/mordor/blob/master/environment/shire/aws/Date_Documentation/Workstation-Audit-Settings.md)

## Users:
|Firstname|Lastname|Username|Identity|Province|Password|NTLM Hash|OU|
|---------|---------|---------|---------|---------|---------|---------|---------|
|Pedro|Gustavo|pgustavo|Domain Admins|Shire|S@lv@m3!M0d3|5B1DF8099DB9998C12C045347D4F5BEC|"CN=Users,DC=shire,DC=com"|
|Lucho|Rodriguez|lrodriguez|Users|Shire|Ann0n@!|7DF4090B3A849071DE65F066FB1C845E|"CN=Users,DC=shire,DC=com"|
|Wec|Server|wecserver|Users|Shire|Edhellen$|2B73258D609C326C99F10592812D842F|"CN=Users,DC=shire,DC=com"|
|Norah|Martha|nmartha|Users|Shire|ShiRe012!|9C77F30FD10998EBF825A71CD292C3CF|"CN=Users,DC=shire,DC=com"|
|Gandalf|TheWhite|gandalf|Administrators|Maiar|$hadowf@x1|F814541A42785456359BDD7A9107E4F1|"CN=Users,DC=shire,DC=com"|
|Bilbo|Baggins|bilbo|Users|Shire|LittleThief1!|6B6308F2839A6BD861518FCD354E0BF5|"CN=Users,DC=shire,DC=com"|
|Frodo|Baggins|frodo|Administrators|Shire|RingBeaRer12!|22DECE71F50648DC9850B6409D4FC2F7|"CN=Users,DC=shire,DC=com"|
|Merry|Brandybuck|merry|Users|Shire|Meri@d0c!|2F7A822076D4DAACD9AB8E258C8EDCF5|"CN=Users,DC=shire,DC=com"|
|Pippin|Took|pippin|Users|Shire|PeRegRin1!|4DFE2C9E8C08B0C4B11C0A03CBA55FE6|"CN=Users,DC=shire,DC=com"|
|Samwise|Gamgee|samwise|Users|Shire|TheBr@ve1!|85A27C2606CE84DCFCEA7C2C23BB408B|"CN=Users,DC=shire,DC=com"|
|Saruman| |saruman|Users|Blessed Realm|EvilWiz@rd2!|F1B3CA7B2B36A9E3AC81E131040A0B7A|"CN=Users,DC=shire,DC=com"|
|Smaug| |smaug|Users|Lonely Mountain|TheImpenetr@ble1!|43AC98E745BB34C58C2EEC08F547F00B|"CN=Users,DC=shire,DC=com"|
|Aragorn|Arathorn|aragorn|Administrators|Gondor|R@ngerofTheN0rth|CF3CE8E51196F2654833E34B3D1D5339|"CN=Users,DC=shire,DC=com"|
|Gimili|Gloin|gimili|Users|Glittering Caves|Dw@rv3s|90CFC8DB2B08FEF5BDAC797F811A6FFF|"CN=Users,DC=shire,DC=com"|
|Legolas|Greenleaf|legolas|Users|Woodland|W00dl@ndR3alm1!|54DDD51A3FCDF7EA4252915147C3F2E3|"CN=Users,DC=shire,DC=com"|
|Boromir| |boromir|Users|Gondor|C@ptain0fGond0r1!|2906ABC9768E9D1748C979C0ED097C8F|"CN=Users,DC=shire,DC=com"|
|Elrond| |elrond|Users|Rivendell|Vily@12!|D49A534CD25BE349E2A5674EC4338F42|"CN=Users,DC=shire,DC=com"|

#### The `Gandalf` user will also have an Service Principal Name (SPN) of `glamdring/shire.com`


## Users that are set to login through Apache Guacamole:
|Platform|Version|Purpose|FQDN|IP|LoginUser|
|---------|---------|---------|---------|---------|---------|
|Windows|Windows Server 2016|DC|HFDC1.shire.com|172.18.39.5|Administrator:S@lv@m3!M0d3|
|Windows|Windows 10|Workstation|HR001.shire.com|172.18.39.106|nmartha:ShiRe012!|
|Windows|Windows 10|Workstation|IT001.shire.com|172.18.39.105|pgustavo:S@lv@m3!M0d3|
|Windows|Windows 10|Workstation|ACCT001.shire.com|172.18.39.100|lrodrigues:Ann0n@!|
|Windows|Windows Server 2016|WEC-Log Collector|WECServer.shire.com|172.18.39.102|Administrator:S@lv@m3!M0d3|
|Linux|Ubuntu 18.04|HELK|helk|172.18.39.6|aragorn:aragorn|
|Linux|Ubuntu 16.04|Apache Guacamole|guac|172.18.39.9|guac:guac|
|Linux|Ubuntu 16.04|Red Team Operations|RTO|172.18.39.8|wardog:wardog|








