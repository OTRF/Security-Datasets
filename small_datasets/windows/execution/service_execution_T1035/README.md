# Service Execution

Adversaries may execute a binary, command, or script via a method that interacts with Windows services, such as the Service Control Manager. This can be done by either creating a new service or modifying an existing service. This technique is the execution used in conjunction with New Service and Modify Existing Service during service persistence or privilege escalation.

## Technique Variations Table

| Network | Dataset | Updated |
| ------- | --------- | ------- |
| shire | [empire_invoke_psexec](./empire_invoke_psexec.md) | 2019-05-18210652 |