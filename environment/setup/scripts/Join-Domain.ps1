# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:
# https://github.com/aws-quickstart/quickstart-microsoft-activedirectory/blob/master/templates/Template_1_AD_2012R2.template
# https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/add-computer?view=powershell-5.1
# https://github.com/clong/DetectionLab/blob/9c2710c808d0167ff535fc46015d0aac639c0ee7/Vagrant/scripts/join-domain.ps1

[CmdletBinding()]
param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$ComputerName,

    [Parameter(Mandatory=$true, Position=1)]
    [string]$OU,

    [Parameter(Mandatory=$true, Position=2)]
    [string]$DomainAdminUser,

    [Parameter(Mandatory=$true, Position=3)]
    [string]$DomainAdminPassword,

    [Parameter(Mandatory=$true, Position=4)]
    [string]$DomainNetBiosName,

    [Parameter(Mandatory=$true, Position=5)]
    [string]$DefaultLogonUser,

    [Parameter(Mandatory=$true, Position=6)]
    [string]$DefaultLogonPassword,

    [Parameter(Mandatory=$true, Position=7)]
    [string]$DomainDNSName
)

write-host "Setting $DefaultLogonUser as the default automatic logon user .."

if ($DefaultLogonUser -like "Administrator")
{
    Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name AutoAdminLogon -Value 1
    Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name DefaultUserName -Value $DefaultLogonUser
    Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name DefaultPassword -Value $DefaultLogonPassword
}
else
{
    Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name AutoAdminLogon -Value 1
    Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name DefaultDomainName -Value $DomainDNSName
    Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name DefaultUserName -Value $DefaultLogonUser
    Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" -Name DefaultPassword -Value $DefaultLogonPassword
}


# Stop Windows Update
Write-Host "Disabling Windows Updates and Windows Module Services"
Set-Service wuauserv -StartupType Disabled
Stop-Service wuauserv
Set-Service TrustedInstaller -StartupType Disabled
Stop-Service TrustedInstaller

$OUPath = "OU=$OU,DC=$DomainNetBIOSName,DC=com"

write-host "Adding $ComputerName to $OU in domain $DomainDNSName .."
Add-Computer `
-DomainName $DomainDNSName `
-Credential (New-Object System.Management.Automation.PSCredential("$DomainNetBIOSName\$DomainAdminUser", (ConvertTo-SecureString $DomainAdminPassword -AsPlainText -Force))) `
-OUPath $OUPath `
-Restart