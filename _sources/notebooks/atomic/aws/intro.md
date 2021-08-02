# aws

## ATT&CK Navigator View

<iframe src="https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=https%3A%2F%2Fraw.githubusercontent.com%2FOTRF%2Fmordor%2Fmaster%2Fdocs%2Fnotebooks%2Fatomic%2Faws%2Faws.json&tabs=false&selecting_techniques=false" width="950" height="450"></iframe>

## 1 Datasets

|Created|Dataset|Description|Tags|Author|
| :---| :---| :---| :---| :---|
|2020/09/13 |[AWS Cloud Bank Breach S3](https://securitydatasets.com/notebooks/atomic/aws/initial_access/SDAWS-200914011940.html) |This dataset represents adversaries abusing a misconfigured EC2 reverse proxy to obtain instance profile keys and eventually exfiltrate files from an S3 bucket. | ['EC2 Proxy Abuse', 'S3 Data Exfiltration']| |


attack_mappings:
  - technique: T1018
    sub-technique:
    tactics:
      - TA0007