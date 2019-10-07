The Shire
=========

.. image:: _static/network-erebor.jpeg
    :alt: The Shire
    :scale: 60%

This mordor environment was designed to replicate a very small network with the essential devices to colllect information from adversarial activities.
This environment is a Windows environment.

Network Design
##############

.. image:: _static/mordor-erebor-environment.png
    :alt: erebor Design
    :scale: 35%

Endpoints To Users
******************

+-----------+-------------+---------------+---------------------+---------------+---------------+
| Platform  | Version     | Purpose       | FQDN                | IP Address    | Main User     |
+===========+=============+===============+=====================+===============+===============+
| Windows   | Win 2019    | DC            | HFDC1.shire.com     | 192.168.1.5   | Administrator |
+-----------+-------------+---------------+---------------------+---------------+---------------+
| Windows   | Win 10      | Client        | HR001.shire.com     | 192.168.1.106 | bbaggins      |
+-----------+-------------+---------------+---------------------+---------------+---------------+
| Windows   | Win 10      | Client        | IT001.shire.com     | 192.168.1.105 | toakenshield  |
+-----------+-------------+---------------+---------------------+---------------+---------------+
| Windows   | Win 10      | Client        | ACCT001.shire.com   | 192.168.1.100 | kfili         |
+-----------+-------------+---------------+---------------------+---------------+---------------+
| Windows   | Win 2019    | Log Collector | WECServer.shire.com | 192.168.1.102 | wecserver     |
+-----------+-------------+---------------+---------------------+---------------+---------------+
| Linux     | Ubuntu 18   | Data Analysis | HELK                | 192.168.1.6   | ubuntu        |
+-----------+-------------+---------------+---------------------+---------------+---------------+
| Linux     | Ubuntu 18   | Red Team C2   | RTO                 | 192.168.1.8   | ubuntu        |
+-----------+-------------+---------------+---------------------+---------------+---------------+

Windows Users Information
*************************

.. csv-table::
    :file: _static/erebor_users.csv
    :header-rows: 1

HELK User Information
*********************

You can update the HELK's password in the `HELK's paramaters file <https://github.com/hunters-forge/Blacksmith/blob/master/aws/mordor/cfn-parameters/erebor/helk-server-parameters.json>`_ used to deploy the environment.
This file is hosted by the project `Blacksmith <https://github.com/hunters-forge/Blacksmith>`_ since it is the official repo for all the templates used to deploy every mordor environment.

* Default Username: helk
* Default Password: hunt1ng!

Data Sources Collected
######################

SilkETW Service Conifg: https://github.com/hunters-forge/Blacksmith/blob/master/aws/mordor/cfn-files/configs/erebor/erebor_SilkServiceConfig.xml

Environment Deployment
######################

The `Blacksmith Project <https://blacksmith.readthedocs.io/en/latest/>`_ is responsible for deploying this environment.
Therefore, you can follow the instructions provided in `here <https://blacksmith.readthedocs.io/en/latest/mordor_erebor.html>`_