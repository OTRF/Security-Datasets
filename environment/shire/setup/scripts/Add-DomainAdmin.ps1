# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:
# https://aws.amazon.com/blogs/compute/optimizing-joining-windows-server-instances-to-a-domain-with-powershell-in-aws-cloudformation/
# https://github.com/aws-quickstart/quickstart-microsoft-activedirectory/blob/master/scripts/archive/Create-AdminUser.ps1

[CmdletBinding()]
param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$DomainAdminUser,

    [Parameter(Mandatory=$true, Position=1)]
    [string]$DomainDNSName,

    [Parameter(Mandatory=$true, Position=2)]
    [string]$DomainAdminPassword,

    [Parameter(Mandatory=$true, Position=3)]
    [string]$Server
)

# First Check: Verify if ADWS is still running. If not, start service.
write-host "Verifying if ADWS is still running.."
$s = Get-Service -Name ADWS
while ($s.Status -ne 'Running'){
    Start-Service ADWS; Start-Sleep 3
}
Start-Sleep 30

# Creating and Adding a user to Domain Admins
$timeoutInSeconds = 300
$elapsedSeconds = 0
$intervalSeconds = 1
$startTime = Get-Date
$running = $false

While (($elapsedSeconds -lt $timeoutInSeconds )) {
    try {
        # Second Check: Verify if the ADWS process is running
        $adws = Get-Process -Name Microsoft.ActiveDirectory.WebServices
        $UserPrincipalName = $DomainAdminUser+"@"+$DomainDNSName
        $ADServer = $Server+"."+$DomainDNSName
        if ($adws) {
            write-host "Creating user $UserPrincipalName .."
            New-ADUser -Name $DomainAdminUser -UserPrincipalName $UserPrincipalName -AccountPassword (ConvertTo-SecureString $DomainAdminPassword  -AsPlainText -Force) -Enabled $true -PasswordNeverExpires $true -Server $ADServer
            write-host "Successfully Created $UserPrincipalName..."
            $Groups = @('domain admins','schema admins','enterprise admins')
            $Groups | ForEach-Object{
                write-host "Adding user $DomainAdminUser to $_ .."
                Add-ADGroupMember -Identity $_ -Members $DomainAdminUser
            }
            break
        }
        else{
            Start-Service ADWS
        }           
    }
    catch {
        Start-Sleep -Seconds $elapsedSeconds
        $elapsedSeconds = ($(Get-Date) - $startTime).TotalSeconds
        echo "Elapse Seconds" $elapsedSeconds 
        
    }
    if ($elapsedSeconds -ge $timeoutInSeconds) {
        write-host "ADWS did not start or is unreachable in $timeoutInSeconds seconds..."
    }
}