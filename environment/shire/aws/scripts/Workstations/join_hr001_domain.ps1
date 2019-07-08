$User = "shire.com\nmartha"
$Password = ConvertTo-SecureString -String "ShiRe012!" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $User, $Password

Add-Computer -DomainName "shire.com" -OUPath "OU=Workstations,DC=shire,DC=com" -Credential $Credential -Force -Restart