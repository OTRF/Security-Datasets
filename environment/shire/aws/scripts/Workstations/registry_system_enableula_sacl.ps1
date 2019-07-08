$identity = "Everyone"
$AuditRules = "ReadKey, QueryValues, TakeOwnership"
$InheritFlags = "None"
$PropagationFlags = "None"
$AuditFlag = "Success"
$RegistryReadSuccessAudit = New-Object System.Security.AccessControl.RegistryAuditRule($identity,$AuditRules,$InheritFlags,$PropagationFlags,$AuditFlag)
$FilePath = "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System\"
$Acl = Get-Acl $FilePath -Audit
$Acl.SetAuditRule($RegistryReadSuccessAudit)
$Acl | Set-Acl | Out-Null