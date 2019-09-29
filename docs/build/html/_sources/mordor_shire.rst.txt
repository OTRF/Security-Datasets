The Shire
=========

.. image:: _static/network-shire.png
    :alt: The Shire
    :scale: 60%

This mordor environment was designed to replicate a very small network with the essential devices to colllect information from adversarial activities.
This environment is a Windows environment.

Network Design
##############

.. image:: _static/mordor-shire-environment.png
    :alt: The Shire Design
    :scale: 35%

Endpoints To Users
******************

+-----------+-------------+---------------+---------------------+---------------+---------------+
| Platform  | Version     | Purpose       | FQDN                | IP Address    | Main User     |
+===========+=============+===============+=====================+===============+===============+
| Windows   | Win 2019    | DC            | HFDC1.shire.com     | 172.18.39.5   | Administrator |
+-----------+-------------+---------------+---------------------+---------------+---------------+
| Windows   | Win 10      | Client        | HR001.shire.com     | 172.18.39.106 | nmartha       |
+-----------+-------------+---------------+---------------------+---------------+---------------+
| Windows   | Win 10      | Client        | IT001.shire.com     | 172.18.39.105 | pgustavo      |
+-----------+-------------+---------------+---------------------+---------------+---------------+
| Windows   | Win 10      | Client        | ACCT001.shire.com   | 172.18.39.100 | lrodriguez    |
+-----------+-------------+---------------+---------------------+---------------+---------------+
| Windows   | Win 2019    | Log Collector | WECServer.shire.com | 172.18.39.102 | wecserver     |
+-----------+-------------+---------------+---------------------+---------------+---------------+
| Linux     | Ubuntu 18   | Data Analysis | HELK                | 172.18.39.6   | ubuntu        |
+-----------+-------------+---------------+---------------------+---------------+---------------+
| Linux     | Ubuntu 18   | Red Team C2   | RTO                 | 172.18.39.8   | ubuntu        |
+-----------+-------------+---------------+---------------------+---------------+---------------+

Windows Users Information
*************************

.. csv-table::
    :file: _static/shire_users.csv
    :header-rows: 1

HELK User Information
*********************

You can update the HELK's password in the `HELK's paramaters file <https://github.com/hunters-forge/Blacksmith/blob/master/aws/mordor/mordor-shire-parameters/shire-parameters-helk.json>`_ used to deploy the environment.
This file is hosted by the project `Blacksmith <https://github.com/hunters-forge/Blacksmith>`_ since it is the official repo for all the templates used to deploy every mordor environment.

* Default Username: helk
* Default Password: hunt1ng!

Data Sources Collected
######################

The initial events that mordor is collecting to test level of visibility are the following:

+------------------------------------------------------------------------+------------------------------------------------------------+
| Log Name                                                               | Log Provider                                               |
+========================================================================+============================================================+
| Security                                                               | Microsoft-Windows-Security-Auditing                        |
+------------------------------------------------------------------------+------------------------------------------------------------+
| Microsoft-Windows-Sysmon/Operational                                   | Microsoft-Windows-Sysmon                                   |
+------------------------------------------------------------------------+------------------------------------------------------------+
| Microsoft-Windows-PowerShell/Operational                               | Microsoft-Windows-PowerShell                               |
+------------------------------------------------------------------------+------------------------------------------------------------+
| Windows PowerShell                                                     | PowerShell                                                 |
+------------------------------------------------------------------------+------------------------------------------------------------+
| Microsoft-Windows-WMI-Activity/Operational                             | Microsoft-Windows-WMI-Activity                             |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | Microsoft-Windows-Directory-Services-SAM                   |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | Service Control Manager                                    |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | Microsoft-Windows-GroupPolicy                              |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | Microsoft-Windows-Kernel-General                           |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | Microsoft-Windows-DistributedCOM                           |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | Microsoft-Windows-Winlogon                                 |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | Microsoft-Windows-DNS-Client                               |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | Microsoft-Windows-Ntfs                                     |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | Microsoft-Windows-WinRM                                    |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | e1iexpress                                                 |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | Microsoft-Windows-Kernel-Processor-Power                   |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | Microsoft-Windows-Power-Troubleshooter                     |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | Microsoft-Windows-Wininit                                  |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | User32                                                     |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | vmci                                                       |
+------------------------------------------------------------------------+------------------------------------------------------------+
| System                                                                 | vsepflt                                                    |
+------------------------------------------------------------------------+------------------------------------------------------------+
| Microsoft-Windows-Windows Firewall With Advanced Security/Firewall     | Microsoft-Windows-Windows Firewall With Advanced Security  |
+------------------------------------------------------------------------+------------------------------------------------------------+
| Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational | Microsoft-Windows-TerminalServices-RemoteConnectionManager |
+------------------------------------------------------------------------+------------------------------------------------------------+
| Microsoft-Windows-Bits-Client/Operational                              | Microsoft-Windows-Bits-Client                              |
+------------------------------------------------------------------------+------------------------------------------------------------+

Windows Security Auditing
*************************

.. csv-table::
    :file: _static/mordor-windows-security-mapping.csv
    :header-rows: 1

Sysmon Auditing
***************

Sysmon Configuration: https://github.com/hunters-forge/mordor/blob/master/environments/windows/configs/shire/shire_sysmon.xml
