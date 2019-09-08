# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:
# https://www.itprotoday.com/windows-78/create-large-number-ous-set-structure-and-delegation

$OUS = @(("Workstations","Workstations in Shire"),("Servers","Servers in Shire"),("ShireUsers","Users in Shire"))
$ParentPath = "DC=shire,DC=com"

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