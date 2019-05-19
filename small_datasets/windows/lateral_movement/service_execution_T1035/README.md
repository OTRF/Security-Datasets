# Service Execution

Adversaries may execute a binary, command, or script via a method that interacts with Windows services, such as the Service Control Manager. This can be done by either creating a new service or modifying an existing service. This technique is the execution used in conjunction with New Service and Modify Existing Service during service persistence or privilege escalation.

## Technique Variations Table

| RT Platform | Network | Dataset | Updated |
| ----------- | ------- | --------- | ------- |
| empire |  shire | [empire_invoke_psexec](../../execution/service_execution_T1035/empire_invoke_psexec.md) | 2019-05-18210652 |