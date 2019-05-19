# Persistence via Scheduled Tasks

Utilities such as at and schtasks, along with the Windows Task Scheduler, can be used to schedule programs or scripts to be executed at a date and time. A task can also be scheduled on a remote system, provided the proper authentication is met to use RPC and file and printer sharing is turned on. Scheduling a task on a remote system typically required being a member of the Administrators group on the the remote system.

## Technique Variations Table

| Network | Dataset | Updated |
| ------- | --------- | ------- |
| shire | [empire_userland_schtasks](./empire_userland_schtasks.md) | 2019-03-19024742 |
| shire | [empire_elevated_schtasks](./empire_userland_schtasks.md) | 2019-05-18184109 |