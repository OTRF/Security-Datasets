# APT29 Evals - Open Datasets 🌎

Welcome to the datasets section of this **Detection Hackathon**. Get familiarized with the data and start exploring the schema of the events you will use to develop detections. For this event I collected host and network events.

# About Datasets

**Host** and **Network** event logs! 🔥

| Type | Scenario | Dataset | Size | Timestamp |
|--- |--- |--- |--- |---|
| Host | Day 1 | [apt29_evals_day1_manual.zip](apt29_evals_day1_manual.zip) | 367M | 2020-04-29200743 |
| Network | Day 1 | [scranton.zip](pcaps/SCRANTON.zip) |  | 2020-04-30235600 |
| Network | Day 1 | [nashua.zip](pcaps/NASHUA.zip) |  | 2020-04-30235600 |

## About Host Data

### Host Audit Configs

The following configs were appllied to the endpoints:

| Type | Document |
|--- |--- |
| Windows Security Audit Policy | [PS Script](https://github.com/hunters-forge/Blacksmith/blob/master/resources/scripts/powershell/auditing/Enable-WinAuditCategories.ps1) |
| PowerShell ScriptBlock and Module Logging | [PS Script](https://github.com/hunters-forge/Blacksmith/blob/master/resources/scripts/powershell/auditing/Enable-PowerShell-Logging.ps1) |
| Sysmon Config (v.11 - 4.30) | [XML File](https://github.com/hunters-forge/Blacksmith/blob/master/resources/configs/sysmon/sysmonv11.0.xml) |
| SACLs | [PS Script](https://github.com/hunters-forge/Blacksmith/blob/master/resources/scripts/powershell/auditing/Set-SACLs.ps1) |
| WEF Subscriptions | [XML Files](https://github.com/hunters-forge/Blacksmith/tree/master/resources/configs/wef/subscriptions)

### Day 1 Host - Summary

Number of events per Windows Event Provider

```
+----------------------------------------------------------------------+------+----+
|Channel                                                               |count |%   |
+----------------------------------------------------------------------+------+----+
|Microsoft-Windows-Sysmon/Operational                                  |164435|68.5|
|Security                                                              |40841 |17.0|
|security                                                              |19160 |8.0 |
|Microsoft-Windows-PowerShell/Operational                              |7938  |3.3 |
|Windows PowerShell                                                    |7303  |3.0 |
|Microsoft-Windows-WMI-Activity/Operational                            |198   |0.1 |
|System                                                                |99    |0.0 |
|Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational|15    |0.0 |
|Microsoft-Windows-Windows Firewall With Advanced Security/Firewall    |10    |0.0 |
|Microsoft-Windows-TerminalServices-LocalSessionManager/Operational    |9     |0.0 |
|Microsoft-Windows-Bits-Client/Operational                             |1     |0.0 |
+----------------------------------------------------------------------+------+----+
```
### Day 1 Host - Sysmon

Number of events per Sysmon event Ids.

```
+-------+-----+----+
|EventID|count|%   |
+-------+-----+----+
|12     |63047|38.3|
|10     |54091|32.9|
|7      |20736|12.6|
|13     |19171|11.7|
|3      |2771 |1.7 |
|11     |1605 |1.0 |
|9      |844  |0.5 |
|18     |586  |0.4 |
|1      |433  |0.3 |
|5      |407  |0.2 |
|23     |367  |0.2 |
|17     |125  |0.1 |
|8      |98   |0.1 |
|22     |78   |0.0 |
|2      |62   |0.0 |
|15     |13   |0.0 |
|4      |1    |0.0 |
+-------+-----+----+
```

### Day 1 Host - Windows Security Auditing

Top 20 Event Ids

```
+-------+-----+----+
|EventID|count|%   |
+-------+-----+----+
|4658   |14614|24.4|
|5156   |8730 |14.5|
|4656   |7311 |12.2|
|4690   |7282 |12.1|
|4663   |6921 |11.5|
|5158   |3680 |6.1 |
|5447   |2617 |4.4 |
|4703   |2534 |4.2 |
|5154   |1610 |2.7 |
|4673   |1204 |2.0 |
|4688   |541  |0.9 |
|4689   |474  |0.8 |
|4624   |380  |0.6 |
|4627   |380  |0.6 |
|4672   |295  |0.5 |
|4634   |286  |0.5 |
|4945   |176  |0.3 |
|4670   |174  |0.3 |
|5145   |114  |0.2 |
|5140   |59   |0.1 |
+-------+-----+----+
```