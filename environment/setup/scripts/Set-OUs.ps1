# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:
# https://www.itprotoday.com/windows-78/create-large-number-ous-set-structure-and-delegation

[CmdletBinding()]
param (
    [Parameter(Mandatory=$true)]
    [string]$DomainNetBiosName
)
$ParentPath = "DC=$DomainNetBIOSName,DC=com"
$OUS = @(("Workstations","Workstations in the domain"),("Servers","Servers in the domain"),("DomainUsers","Users in the domain"))

foreach($OU in $OUS)
{
    #Check if exists, if it does skip
    [string] $Path = "OU=$($OU[0]),$ParentPath"
    if(![adsi]::Exists("LDAP://$Path"))
    {
        write-host "Creating OU $OU .." 
        $NewOU = New-ADOrganizationalUnit -Name $OU[0] -Path $ParentPath `
            -Description $OU[1] `
            -ProtectedFromAccidentalDeletion $false -PassThru
    }
}