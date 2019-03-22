Network Design
==============

The mordor environment was designed to replicate a very small network with the essential devices to colllect information from adversarial activities.

Network Devices
###############

.. image:: _static/mordor-environment.png
    :alt: Catapult
    :scale: 35%

+-----------+-------------+---------------+-----------+---------------+---------------+
| Platform  | Version     | Purpose       | Name      | IP Address    | Main User     |
+===========+=============+===============+===========+===============+===============+
| Windows   | Win 2016    | DC            | HFDC1     | 172.18.39.5   | Administrator |
+-----------+-------------+---------------+-----------+---------------+---------------+
| Windows   | Win 10      | Client        | HR001     | 172.18.39.106 | nnmartha      |
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
