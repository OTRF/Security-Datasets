#Author Jonathan Johnson
#License: GPL-3.0

#Resources -
#Microsoft-Docs:https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/rename-computer?view=powershell-6
#Microsoft-Docs: https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-credential?view=powershell-6
$User = "User"
$Password = ConvertTo-SecureString -String "S@lv@m3!M0d3" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $User, $Password
Rename-computer –computername ("DESKTOP-7MOT5CD") -newname ("HR001") -DomainCredential $Credential -Force -Restart
