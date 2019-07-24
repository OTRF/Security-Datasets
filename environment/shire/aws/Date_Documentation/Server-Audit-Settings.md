# Server System Audit Polcies
### Registry Audit Rules are going to be pulled from [Set-AuditRule](https://github.com/hunters-forge/Set-AuditRule)

|	Category/Subcategory: | Setting: |
|	----------------	|	----------------	|
|	<strong>[System:](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)</strong>	|
|	[Securtiy System Extension](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-security-system-extension)	|	 Success and Failure	|		
|	[System Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-system-integrity)	|	Success and Failure	|	
|	[IPsec Driver](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-ipsec-driver)	|	Success and Failure	|		
|	[Other System Events](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-system-events) |	Success and Failure	|		
|	[Security State Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-security-state-change)	|	Success and Failure	|
|<strong>[Logon/Logoff:](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)</strong>|		
|[Logon](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-logon)|Success and Failure|		
|[Logoff](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-logonlogoff-events)|Success and Failure|		
|[Account Lockout](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-account-lockout)|Success and Failure|			
|[IPsec Main Mode](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-ipsec-main-mode) |Success and Failure|		
|[IPsec Quick Mode](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-ipsec-quick-mode)|Success and Failure|	
|[IPsec Extended Mode](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-ipsec-quick-mode)|Success and Failure|	
|[Special Logon](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-special-logon)|Success and Failure|		
|[Other Logon/Logoff Events](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-logonlogoff-events)|Success and Failure|	
|[Network Policy Server](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-network-policy-server)|No Auditing|			
|[User / Device Claims](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-user-device-claims)|Success and Failure|			
|[Group Membership](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-group-membership)|Success and Failure|				
|<strong>[Object Access:](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)</strong>|					
|[File System](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-file-system)|Success and Failure|	
|[Registry](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-registry)|Success and Failure|	
|[Kernel Object](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-kernel-object)|Success and Failure|			
|[SAM](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-sam)|Success and Failure|
|[Certification Services](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-certification-services)|No Auditing|
|[Application Generated](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-application-generated)|Success and Failure|
|[Handle Manipulation](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-handle-manipulation)|Success and Failure|
|[File Share](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-file-share)|Success and Failure|
|[Filtering Platform Packet Drop](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-filtering-platform-packet-drop)|No Auditing|
|[Filtering Platform Connection](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-filtering-platform-connection)|Success and Failure|
|[Other Object Access Events](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-object-access-events)|Success and Failure|
|[Detailed File Share](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-detailed-file-share)|Success and Failure|
|[Removable Storage](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-removable-storage)|Success and Failure|
|[Central Policy Staging](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-central-access-policy-staging)|Success and Failure|	
|<strong>[Privilege Use:](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)</strong>|	
|[Non Sensitive Privilege Use](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-non-sensitive-privilege-use)|Success and Failure|		
|[Other Privilege Use Events](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-privilege-use-events)|Success and Failure|		
|[Sensitive Privilege Use](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-sensitive-privilege-use)|Success and Failure|				
|<strong>[Detailed Tracking:](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)</strong>|			
|[Process Creation](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-process-creation)|Success and Failure|		
|[Process Termination](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-process-termination)|Success and Failure|			
|[DPAPI Activity](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-dpapi-activity)|Success and Failure|		
|[RPC Events](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-rpc-events)|Success and Failure|	
|[Plug and Play Events](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-pnp-activity)|Success and Failure|		
|[Token Right Adjusted Events](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4703)|Success and Failure|						
|<strong>[Policy Change:](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)</strong>|		
|[Audit Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-audit-policy-change)|Success and Failure|		
|[Authentication Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-authentication-policy-change)|Success and Failure|		
|[Authorization Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-authorization-policy-change)|Success and Failure|		
|[MPSSVC Rule-Level Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-mpssvc-rule-level-policy-change)|Success and Failure|		
|[Filtering Platform Policy Change](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-filtering-platform-policy-change)|Success and Failure|		
|[Other Policy Change Events](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-policy-change-events)|Success and Failure	|			
|<strong>[Account Management:](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)</strong>|			
|[Computer Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-computer-account-management)|Success and Failure|		
|[Security Group Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-security-group-management)|Success and Failure|		
|[Distribution Group Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-distribution-group-management)|Success and Failure|		
|[Application Group Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-application-group-management)|Success and Failure|		
|[Other Account Management Events](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-account-management-events)|Success and Failure|		
|[User Account Management](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-user-account-management)|Success and Failure|			
|<strong>[DS Access:](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)</strong>|
|[Directory Service Access](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-directory-service-access)|Success and Failure|			
|[Directory Service Changes](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-directory-service-changes)|Success and Failure|		
|[Directory Service Replication](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-directory-service-replication)|Success and Failure|		
|[Detailed Directory Service Replication](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-detailed-directory-service-replication)|Success and Failure|			
|<strong>[Account Logon:](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)</strong>|		
|[Kerberos Service Ticket Operations](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-kerberos-service-ticket-operations)|Success and Failure|		
|[Other Account Logon Events](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-logonlogoff-events)|Success and Failure|	
|[Kerberos Authentication Service](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-kerberos-authentication-service)|Success and Failure|		
|[Credential Validation](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-credential-validation)|Success and Failure|		
