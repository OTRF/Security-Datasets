Mordor Categorization
=====================

Mordor hosts several datasets and can split in two options, small and large datasets.

Small Datasets
##############

* They are categorized by following the Mitre `ATT&CK Framework <https://attack.mitre.org/wiki/Main_Page>`_ structure (Platform, Tactic, Technique).
* They are also organized considering the concept of sub-techniques to provide variations of specific techniques.
* They represent events that get generated throughout the ``lifecycle of the specific technique`` being tested.
* They lack of context from other techniques that happen in other tactic categories. For example, if mordor data gives you credential dumping sub-techniques, you only get that and not the potential privilege escalation activity that might have been necessary to be able to dump credentials in the first place. 
* Think about them as the results of atomic testing.

Examples
********

* `DCSync Dataset <https://github.com/Cyb3rWard0g/mordor/blob/master/small_datasets/windows/credential_access/credential_dumping_T1003/credentials_from_ad/empire_dcsync.md>`_

Large Datasets
##############

* They are categorized by known APT groups or custom combination of techniques produced in the mordor lab environments
* They represent events that get generated throughout the ``whole attack lifecycle`` (Initial accesss, discovery, privilege escalation, etc)
* They have a lot of context to identify relationships across several data sources produced by the execution of several adversarial techniques in one mordor file.
* This is going to be available by the end of May 2019.
