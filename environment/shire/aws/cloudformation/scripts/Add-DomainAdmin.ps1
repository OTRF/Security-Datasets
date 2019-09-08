# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:
# https://aws.amazon.com/blogs/compute/optimizing-joining-windows-server-instances-to-a-domain-with-powershell-in-aws-cloudformation/

[CmdletBinding()]
param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$DomainAdminUser,

    [Parameter(Mandatory=$true, Position=1)]
    [string]$DomainDNSName,

    [Parameter(Mandatory=$true, Position=2)]
    [string]$DomainAdminPassword
)

# Verify if ADWS is still running. If not, it is started.
write-host "Verifying if ADWS is still running.."
$s = Get-Service -Name ADWS
while ($s.Status -ne 'Running'){
    Start-Service ADWS; Start-Sleep 3
}
Start-Sleep 60

# Add User
write-host "Creating user $DomainAdminUser .."
$u = New-ADUser -Name $DomainAdminUser -UserPrincipalName "$DomainAdminUser@$DomainDNSName" -AccountPassword (ConvertTo-SecureString $DomainAdminPassword -AsPlainText -Force) -Enabled $true -PasswordNeverExpires $true -PassThru

# Add User to Domain Admins
$timeoutInSeconds = 300
$elapsedSeconds = 0
$intervalSeconds = 1
$startTime = Get-Date
$running = $false

While (($elapsedSeconds -lt $timeoutInSeconds )) {
    try {
        $Groups = @('domain admins','schema admins','enterprise admins')
        $Groups | ForEach-Object{
            write-host "Adding user $DomainAdminUser to $_ .."
            Add-ADGroupMember -Identity $_ -Members $DomainAdminUser
        }
        break         
    }
    catch {
        Start-Sleep -Seconds $elapsedSeconds
        $elapsedSeconds = ($(Get-Date) - $startTime).TotalSeconds
        echo "Elapse Seconds" $elapsedSeconds 
        
    }
    if ($elapsedSeconds -ge $timeoutInSeconds) {
        Throw "ADWS did not start or is unreachable in $timeoutInSeconds seconds..."
    }
}