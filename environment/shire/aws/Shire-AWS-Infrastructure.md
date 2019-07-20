# Shire AWS Infrastructure

<p align="center"><img src="https://github.com/Cyb3rWard0g/mordor/blob/mordor_aws/environment/shire/aws/images/Infrastructure.png"/></p>
<p align="center"><strong> Infrastructure of Mordor inside of AWS</strong> </p>
Above you will see Mordor’s Infrastructure inside of AWS. The lines represent how the data and logs flow within the environment. The environment is utilizing the Windows Event Collector (WEC) service that pulls the logs from other machines through Subscriptions. After the logs are inside of the WEC Server, they are being forwarded through winlogbeat to HELK. 

#### *Note*: ####  You might see AWS events on the endpoints after the lab is built. 

#### For a detailed overview of the AWS Lab, please see below:

## AD Environment:

### 5 Machines:
	1 AD/DC (Active Directory/Domain Controller)
		
	1 WEC (Windows Event Collector)
		
	3 Windows 10 Workstations


## Non-Domain joined machines:
### 3 Ubuntu 16.04 Machines: 

	1 HELK  (From  project -  https://github.com/Cyb3rWard0g/HELK.git)
		
	1 Apache Guacamole (installed from https://github.com/jsecurity101/ApacheGuacamole. Modification were made to user-mapping.xml to fit this project)
		
	1 Operator machine (Created for C2’s. Currently only Powershell Empire (https://github.com/EmpireProject/Empire) is the only one on this machine)


## Users:
|Firstname|Lastname|Username|Identity|Province|Password|OU|
|---------|---------|---------|---------|---------|---------|---------|
|Pedro|Gustavo|pgustavo|Domain Admins|Shire|S@lv@m3!M0d3|"CN=Users,DC=shire,DC=com"|
|Lucho|Rodriguez|lrodriguez|Users|Shire|Ann0n@!|"CN=Users,DC=shire,DC=com"|
|Wec|Server|wecserver|Users|Shire|Edhellen$|"CN=Users,DC=shire,DC=com"|
|Norah|Martha|nmartha|Users|Shire|ShiRe012!|"CN=Users,DC=shire,DC=com"|
|Gandalf|TheWhite|gandalf|Administrators|Maiar|$hadowf@x1|"CN=Users,DC=shire,DC=com"|
|Bilbo|Baggins|bilbo|Users|Shire|LittleThief1!|"CN=Users,DC=shire,DC=com"|
|Frodo|Baggins|frodo|Administrators|Shire|RingBeaRer12!|"CN=Users,DC=shire,DC=com"|
|Merry|Brandybuck|merry|Users|Shire|Meri@d0c!|"CN=Users,DC=shire,DC=com"|
|Pippin|Took|pippin|Users|Shire|PeRegRin1!|"CN=Users,DC=shire,DC=com"|
|Samwise|Gamgee|samwise|Users|Shire|TheBr@ve1!|"CN=Users,DC=shire,DC=com"|
|Saruman| |saruman|Users|Blessed Realm|EvilWiz@rd2!|"CN=Users,DC=shire,DC=com"|
|Smaug| |smaug|Users|Lonely Mountain|TheImpenetr@ble1!|"CN=Users,DC=shire,DC=com"|
|Aragorn|Arathorn|aragorn|Administrators|Gondor|R@ngerofTheN0rth|"CN=Users,DC=shire,DC=com"|
|Gimili|Gloin|gimili|Users|Glittering Caves|Dw@rv3s|"CN=Users,DC=shire,DC=com"|
|Legolas|Greenleaf|legolas|Users|Woodland|W00dl@ndR3alm1!|"CN=Users,DC=shire,DC=com"|
|Boromir| |boromir|Users|Gondor|C@ptain0fGond0r1!|"CN=Users,DC=shire,DC=com"|
|Elrond| |elrond|Users|Rivendell|Vily@12!|"CN=Users,DC=shire,DC=com"|

#### The `Gandalf` user will also have an Service Principal Name (SPN) of `glamdring/shire.com`


## Users that are set to login through Apache Guacamole:
|Platform|Version|Purpose|FQDN|IP|LoginUser|
|---------|---------|---------|---------|---------|---------|
|Windows|Windows Server 2016|DC|HFDC1.shire.com|172.18.39.5|Administrator:S@lv@m3!M0d3|
|Windows|Windows 10|Workstation|HR001.shire.com|172.18.39.106|nmartha:ShiRe012!|
|Windows|Windows 10|Workstation|IT001.shire.com|172.18.39.105|pgustavo:S@lv@m3!M0d3|
|Windows|Windows 10|Workstation|ACCT001.shire.com|172.18.39.100|lrodrigues:Ann0n@!|
|Windows|Windows Server 2016|WEC-Log Collector|WECServer.shire.com|172.18.39.102|Administrator:S@lv@m3!M0d3|
|Linux|Ubuntu 16.04|HELK|helk|172.18.39.6|aragorn:aragorn|
|Linux|Ubuntu 16.04|Apache Guacamole|guac|172.18.39.9|guac:guac|
|Linux|Ubuntu 16.04|Red Team C2|empire|172.18.39.8|wardog:wardog|








