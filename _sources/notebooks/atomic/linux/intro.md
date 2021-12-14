# linux

## ATT&CK Navigator View

<iframe src="https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FOTRF%2Fmordor%2Fmaster%2Fdocs%2Fnotebooks%2Fatomic%2Flinux%2Flinux.json&tabs=false&selecting_techniques=false" width="950" height="450"></iframe>

## 3 Datasets

|Created|Dataset|Description|Tags|Author|
| :---| :---| :---| :---| :---|
|2021/12/14 |[Log4jShell LDAP JNDI Lookup](https://securitydatasets.com/notebooks/atomic/linux/initial_access/SDLIN-211214154100.html) |The JNDI lookup feature of log4j allows variables to be retrieved via JNDI - Java Naming and Directory Interface. This is an API that that provides naming and directory functionality to Java applications. | None| |
|2020/11/10 |[Arp Cache Discovery](https://securitydatasets.com/notebooks/atomic/linux/discovery/SDLIN-201110074812.html) |This dataset represents a threat actor using arp to list out the arp cache. | None| |
|2020/11/10 |[DD Binary Padding Hash Change](https://securitydatasets.com/notebooks/atomic/linux/defense_evasion/SDLIN-201110081941.html) |This dataset represents a threat actor using dd to add a zero to the binary to change the hash. | None| |


attack_mappings:
  - technique: T1018
    sub-technique:
    tactics:
      - TA0007