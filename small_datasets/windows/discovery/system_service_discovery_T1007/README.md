# System Service Discovery

Adversaries may try to get information about registered services. Commands that may obtain information about services using operating system utilities are "sc," "tasklist /svc" using Tasklist, and "net start" using Net, but adversaries may also use other tools as well.

## Technique Variations Table

| Network | Dataset | Updated |
| ------- | --------- | ------- |
| shire | [empire_net_start](./empire_net_start.md) | 2019-05-18220124 |
| shire | [empire_powerup_al_checks](./empire_powerup_all_checks.md) | 2019-05-18182927 |