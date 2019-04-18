# Remote File Copy

Files may be copied from one system to another to stage adversary tools or other files over the course of an operation. Files may be copied from an external adversary-controlled system through the Command and Control channel to bring tools into the victim network or through alternate protocols with another tool such as FTP. Files can also be copied over on Mac and Linux with native tools like scp, rsync, and sftp.

Adversaries may also copy files laterally between internal victim systems to support Lateral Movement with remote Execution using inherent file sharing protocols such as file sharing over SMB to connected network shares or with authenticated connections with Windows Admin Shares or Remote Desktop Protocol. [Reference](https://attack.mitre.org/techniques/T1105/)

## Technique Variations Table

| RT Platform | Network | Dataset | Updated |
| ----------- | ------- | --------- | ------- |
| empire |  shire | [empire_scm_dll_hijack_ikeext](./empire_scm_dll_hijack_ikeext.md) | 2019-04-03133337 |