# Adversary

APT29

## ATT&CK Group ID

G0016

## ATT&CK STIX ID

[intrusion-set--899ce53f-13a0-479b-a0e4-67d46e241542](https://github.com/mitre/cti/blob/b8b9e39cfd2acdc3b0cf4fbd09c29a7732af0e1d/enterprise-attack/intrusion-set/intrusion-set--899ce53f-13a0-479b-a0e4-67d46e241542.json)

## Aliases

APT29, YTTRIUM, The Dukes, Cozy Bear, CozyDuke

## Description

[APT29](https://attack.mitre.org/groups/G0016/) is a threat group that has been attributed to the Russian government and has operated since at least 2008. This group reportedly compromised the Democratic National Committee starting in the summer of 2015.

APT29 is distinguished by its commitment to stealth and sophisticated implementations of techniques via an arsenal of custom malware. APT29 typically accomplishes its goals via custom compiled binaries and alternate execution methods such as PowerShell and WMI. APT29 has also been known to employ various operational cadences (smash-and-grab vs. slow-and-deliberate) depending on the perceived intelligence value and/or infection method of victims. 

## ATT&CK Evaluation 

There are several datasets as a result of me replicating APT29 activity from the [ATT&CK evaluations (Round 2)](https://attackevals.mitre.org/evaluations.html?round=APT29)
* [First Scenario](https://github.com/mitre-attack/attack-arsenal/tree/master/adversary_emulation/APT29/Emulation_Plan/Day%201)
* [Second Scenario](https://github.com/mitre-attack/attack-arsenal/tree/master/adversary_emulation/APT29/Emulation_Plan/Day%202)

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

## Datasets

| Type | Scenario | Dataset | Size | Timestamp |
|--- |--- |--- |--- |---|
| Host | Day 1 | [apt29_evals_day1_manual.zip](day1/apt29_evals_day1_manual.zip) | 367M | 2020-05-01225525 |
| Host | Day 2 | [apt29_evals_day2_manual.zip](day2/apt29_evals_day1_manual.zip) | 1.6GB | 2020-05-02035409 |

### Host Day 1 Summary

```
+----------------------------------------------------------------------+------+----+
|Channel                                                               |count |%   |
+----------------------------------------------------------------------+------+----+
|Microsoft-Windows-Sysmon/Operational                                  |143884|73.4|
|Security                                                              |28627 |14.6|
|security                                                              |12375 |6.3 |
|Microsoft-Windows-PowerShell/Operational                              |5694  |2.9 |
|Windows PowerShell                                                    |5285  |2.7 |
|System                                                                |91    |0.0 |
|Microsoft-Windows-WMI-Activity/Operational                            |90    |0.0 |
|Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational|15    |0.0 |
|Microsoft-Windows-Windows Firewall With Advanced Security/Firewall    |10    |0.0 |
|Microsoft-Windows-TerminalServices-LocalSessionManager/Operational    |9     |0.0 |
|Microsoft-Windows-Bits-Client/Operational                             |1     |0.0 |
+----------------------------------------------------------------------+------+----+
```

### Host Day 2 Summary

```
+----------------------------------------------------------------------+------+----+
|Channel                                                               |count |%   |
+----------------------------------------------------------------------+------+----+
|Microsoft-Windows-Sysmon/Operational                                  |407265|69.3|
|Windows PowerShell                                                    |69084 |11.8|
|Microsoft-Windows-PowerShell/Operational                              |60372 |10.3|
|Security                                                              |27207 |4.6 |
|security                                                              |22854 |3.9 |
|Microsoft-Windows-Windows Firewall With Advanced Security/Firewall    |292   |0.0 |
|System                                                                |105   |0.0 |
|Microsoft-Windows-WMI-Activity/Operational                            |81    |0.0 |
|Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational|14    |0.0 |
|Microsoft-Windows-TerminalServices-LocalSessionManager/Operational    |10    |0.0 |
|Microsoft-Windows-Bits-Client/Operational                             |2     |0.0 |
+----------------------------------------------------------------------+------+----+
```

## Network Environment

* Infrastructure: https://medium.com/threat-hunters-forge/mordor-labs-part-1-deploying-att-ck-apt29-evals-environments-via-arm-templates-to-create-1c6c4bc32c9a
* Information about users and passwords: https://github.com/OTRF/mordor-labs/tree/master/environments/attack-evals/apt29#domain-users-information

## Time Taken

* Scenario 1: 2020-05-01225525
* Scenario 2: 2020-05-02035409

## Emulation Plans

* Scenario 1 & 2: [apt29.xlsx](emulationplans/apt29.xlsx)

* Scenario 1 Description

The first scenario (executed with Pupy, Meterpreter, and custom tooling) begins with the execution of a payload delivered by a widespread "spray and pray" spearphishing campaign, followed by a rapid "smash and grab" collection and exfiltration of specific file types. After completing the initial data theft, the value of the target is realized, and the adversary drops a secondary, stealthier toolkit used to further explore and compromise the target network.

Video: https://www.youtube.com/watch?v=fJAuBrzYTzI

* Scenario 2 Description:

The second scenario (executed with PoshC2 and custom tooling) focuses on a very targeted and methodical breach, beginning with the execution of a specially crafted payload designed to scrutinize the target environment before executing. The scenario continues through a low and slow takeover of the initial target and eventually the entire domain. Both scenarios include executing previously established persistence mechanisms after a simulated time lapse to further the scope of the breach.

Video: https://www.youtube.com/watch?v=PzYKvfwoHEY

## References

https://attack.mitre.org/docs/APT3_Adversary_Emulation_Plan.pdf
https://attackevals.mitre.org/methodology/round1/scope.html
https://attackevals.mitre.org/evaluations/microsoft.1.apt3.1/microsoft.1.apt3.1_overview
https://github.com/mitre-attack/evals_caldera