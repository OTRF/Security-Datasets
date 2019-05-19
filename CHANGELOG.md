# Changelog

## Verion 0.0.2
----------------------------------

[Full Changelog](https://github.com/Cyb3rWard0g/mordor/compare/0.0.1...0.0.2)

### Fixed:
**defense evesion**

* Process Injection
  * Empire PsInject

### Added:
**Credential Access**

* Credential Dumping
  * Empire Mimikatz Export Master Key
  * Empire Mimikatz Extract Tickets
  * Empire Mimikatz Lsadump
  * Empire Powerdump

**Defense Evasion**

* Modify Registry
  * Empire Enable RDP
  * Empire Wdigest Downgrade

* Process Injection
  * Empire Dll Injection

* Trusted Developer Utilities
  * Empire Invoke Msbuild

**Discovery**

* Account Discovery
  * Empire Find-LocalAdminAccess
  * Empire Net User Domain SPecific

* System Network Connections Discovery
  * Empire Get Session Local
  * Empire Get Session DC

* System Service Discovery
  * Empire Net Start
  * Empire Powerup All Checks

**Execution**

* PowerShell
  * Empire Invoke Psremoting
* Service Execution
  * Empire Invoke Psexec
* Windows Management Instrumentation
  * Empire Invoke wmi debugger
  * Empire wmic add user backdoor

**Lateral Movement**

* Distributed Component Object Model
  * Empire Invoke DCOM
* Trusted Developer Utilities
  * Empire Invoke Msbuild
* Windows Admin Shares
  * Empire Infoke Smbexec
* PowerShell
  * Empire Invoke Psremoting
* Service Execution
  * Empire Invoke Psexec
* Windows Management Instrumentation
  * Empire Invoke wmi debugger
  * Empire wmic add user backdoor

**Persistence**

* Registry Run
  * Empire Elevated Registry
* Scheduled Tasks
  * Empire Elevated Schtasks
* WMI Event Subscription
  * Empire Elevated WMI

**Privilege Escalation**

* Access Token Manipulation
  * Empire Invoke Runas
* Bypass UAC
  * Empire Ask

### Updated:
**Execution**

* Windows Management Instrumentation
  * Empire Invoke-Wmi

**Credential Access**

* Credential Dumping
  * Empire Mimikatz logonpasswords

**Discovery**

* Permissions Group Discovery
  * Empire Net Domain Admins

**Execution**

* Scripting
  * Empire Launcher Vbs