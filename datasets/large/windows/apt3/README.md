# Adversary

APT3

## ATT&CK Group ID

G002

## ATT&CK STIX ID

intrusion-set--0bbdf25b-30ff-4894-a1cd-49260d0dd2d9

## Aliases

APT3, Gothic Panda, Pirpi, UPS Team, Buckeye, Threat Group-0110, TG-0110

## Description

[APT3](https://attack.mitre.org/groups/G0022) is a China-based threat group that researchers have attributed to China's Ministry of State Security. (Citation: FireEye Clandestine Wolf) (Citation: Recorded Future APT3 May 2017) This group is responsible for the campaigns known as Operation Clandestine Fox, Operation Clandestine Wolf, and Operation Double Tap. (Citation: FireEye Clandestine Wolf) (Citation: FireEye Operation Double Tap) As of June 2015, the group appears to have shifted from targeting primarily US victims to primarily political organizations in Hong Kong. (Citation: Symantec Buckeye)

## ATT&CK Evaluation 

There are two datasets as a result of us replicating APT3 activity from the [ATT&CK evaluations (Round 1)](https://attackevals.mitre.org/methodology/round1/)
* [First Scenario](https://attackevals.mitre.org/methodology/round1/operational-flow) via the [evals_caldera plugin](https://github.com/mitre-attack/evals_caldera)
* [Second Scenario](https://attackevals.mitre.org/methodology/round1/operational-flow) via [resource files](https://github.com/hunters-forge/mordor/tree/master/large_datasets/apt3/environment/empire/resource_files)

## Creators

Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)
Jose Luis Rodriguez [@Cyb3rPandaH](https://twitter.com/Cyb3rPandaH)

## Datasets

* Scenario 1: [caldera_apt3.tar.gz](./caldera_attack_evals_round1_day1_2019-10-20201108.tar.gz)
* Scenario 2: [empire_apt3.tar.gz](./empire_apt3.tar.gz)

## Network Environment

[Shire](https://mordor.readthedocs.io/en/latest/mordor_shire.html)

* [evals_caldera plugin](https://github.com/mitre-attack/evals_caldera)
* [Empire Resource Files](environment/empire/resource_files)

## Time Taken

* Scenario 1: 2019-10-20201108
* Scenario 2: 2019-05-14223117

## Playbooks

* Scenario 2: [apt3_mordor_playbook.xlsx](scope/apt3_mordor_playbook.xlsx)

## References

https://attack.mitre.org/docs/APT3_Adversary_Emulation_Plan.pdf
https://attackevals.mitre.org/methodology/round1/scope.html
https://attackevals.mitre.org/evaluations/microsoft.1.apt3.1/microsoft.1.apt3.1_overview
https://github.com/mitre-attack/evals_caldera