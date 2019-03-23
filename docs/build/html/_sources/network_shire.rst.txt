The Shire
=========

.. image:: _static/network-shire.png
    :alt: The Shire
    :scale: 60%

This mordor environment was designed to replicate a very small network with the essential devices to colllect information from adversarial activities.

Network Design
##############

.. image:: _static/mordor-environment.png
    :alt: The Shire Design
    :scale: 35%

+-----------+-------------+---------------+-----------+---------------+---------------+
| Platform  | Version     | Purpose       | Name      | IP Address    | Main User     |
+===========+=============+===============+===========+===============+===============+
| Windows   | Win 2016    | DC            | HFDC1     | 172.18.39.5   | Administrator |
+-----------+-------------+---------------+-----------+---------------+---------------+
| Windows   | Win 10      | Client        | HR001     | 172.18.39.106 | nmartha       |
+-----------+-------------+---------------+-----------+---------------+---------------+
| Windows   | Win 10      | Client        | IT001     | 172.18.39.105 | pgustavo      |
+-----------+-------------+---------------+-----------+---------------+---------------+
| Windows   | Win 10      | Client        | ACCT001   | 172.18.39.100 | lrodriguez    |
+-----------+-------------+---------------+-----------+---------------+---------------+
| Windows   | Win 2016    | Win Collector | WECServer | 172.18.39.102 | wecserver     |
+-----------+-------------+---------------+-----------+---------------+---------------+
| Linux     | HELK 0.1.7  | Log Collector | helk      | 10.0.10.102   | helk          |
+-----------+-------------+---------------+-----------+---------------+---------------+
| Linux     | Kali 2018.4 | Red Team C2   | kali      | 10.0.10.106   | wardog        |
+-----------+-------------+---------------+-----------+---------------+---------------+
| macOS     | coming soon | coming soon.. | ..        | ..            | ..            |
+-----------+-------------+---------------+-----------+---------------+---------------+

Data Sources Collected
######################

The initial events that mordor is collecting to test level of visibility are the following:

+----------+-------------------------------------+--------------------------------------------+
| Type     | Log Provider                        | Log Name                                   |
+==========+=====================================+============================================+
| winevent | Microsoft-Windows-Security-Auditing | Security                                   |
+----------+-------------------------------------+--------------------------------------------+
| winevent | Microsoft-Windows-Sysmon            | Microsoft-Windows-Sysmon/Operational       |
+----------+-------------------------------------+--------------------------------------------+
| winevent | Microsoft-Windows-PowerShell        | Microsoft-Windows-PowerShell/Operational   |
+----------+-------------------------------------+--------------------------------------------+
| winevent | Powershell                          | Windows PowerShell                         |
+----------+-------------------------------------+--------------------------------------------+
| winevent | Microsoft-Windows-WMI-Activity      | Microsoft-Windows-WMI-Activity/Operational |
+----------+-------------------------------------+--------------------------------------------+

Windows Security Auditing
#########################

.. csv-table::
    :file: _static/mordor-windows-security-mapping.csv
    :header-rows: 1

Sysmon Auditing
###############

Sysmon Configuration: https://gist.github.com/Cyb3rWard0g/136481552d8845e52962534d1a4b8664