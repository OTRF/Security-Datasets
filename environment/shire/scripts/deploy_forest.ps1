# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:
# https://github.com/MicrosoftDocs/windowsserverdocs/blob/master/WindowsServerDocs/identity/ad-ds/deploy/Install-a-New-Windows-Server-2012-Active-Directory-Forest--Level-200-.md
# https://stackoverflow.com/a/4409448

$host_info = gwmi win32_computersystem

if (($host_info).partofdomain -eq $true) 
{
    $hostname = ($host_info).Name
    $domain_name = ($host_info).Domain

    write-host -fore red "$hostname is already part of the $domain_name domain"
    write-host -fore red "$hostname cannot be used to create a new forest"
} 
else 
{
    write-host -fore green "$hostname is not part of a domain yet.."
    write-host -fore green "Deploying a new forest and promoting $hostname to Domain Controller.."
    
    # Windows Features Installation
    Get-Command -module ServerManager
    write-host -fore green "Installing Windows features:"
    $windows_features = @("AD-Domain-Services", "DNS")
    $windows_features.ForEach({
        write-host -fore yello "Installing $_ Windows feature.."
        Install-WindowsFeature -name $_ -IncludeManagementTools
    })
    
    # Microsoft Windows Server 2016 Standard Evaluation
    # Creating New Forest
    Import-Module ADDSDeployment
    Install-ADDSForest `
    -SafeModeAdministratorPassword $(ConvertTo-SecureString 'S@lv@m3!M0d3' -AsPlainText -Force) `
    -CreateDnsDelegation:$false `
    -DatabasePath "C:\Windows\NTDS" `
    -DomainMode "WinThreshold" `
    -DomainName "shire.com" `
    -DomainNetbiosName "SHIRE" `
    -ForestMode "WinThreshold" `
    -InstallDns:$true `
    -LogPath "C:\Windows\NTDS" `
    -NoRebootOnCompletion:$true `
    -SysvolPath "C:\Windows\SYSVOL" `
    -Force:$true
}
