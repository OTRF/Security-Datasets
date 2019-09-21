# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:
# https://aws.amazon.com/blogs/compute/optimizing-joining-windows-server-instances-to-a-domain-with-powershell-in-aws-cloudformation/
# https://github.com/aws-quickstart/quickstart-microsoft-activedirectory/blob/master/scripts/archive/Create-AdminUser.ps1
# http://woshub.com/new-aduser-create-active-directory-users-powershell/
# https://blog.netwrix.com/2018/06/07/how-to-create-new-active-directory-users-with-powershell/
# https://stackoverflow.com/questions/30617758/splitting-a-string-into-separate-variables

[CmdletBinding()]
param(
    [Parameter(Mandatory=$true, Position=1)]
    [string]$DomainDNSName,

    [Parameter(Mandatory=$true, Position=2)]
    [string]$Server,

    [Parameter(Mandatory=$true, Position=3)]
    [string]$CSVFile
)

write-host "Verifying if ADWS is still running.."
$s = Get-Service -Name ADWS
while ($s.Status -ne 'Running'){
    Start-Service ADWS; Start-Sleep 5
}
Start-Sleep 10

$ADServer = $Server+"."+$DomainDNSName
$DomainName1,$DomainName2 = $DomainDNSName.split('.')

write-host "Importing domain users from $CSVFile .."
Import-Csv $CSVFile | ForEach-Object {
    $UserPrincipalName = $_.SamAccountName + "@" + $DomainDNSName
    $DisplayName = $_.LastName + " " + $_.FirstName
    $OUPath = "OU="+$_.UserContainer+",DC=$DomainName1,DC=$DomainName2"
    $SamAccountName = $_.SamAccountName
    $ServiceName = $_.FirstName

    write-host "Checking if user $SamAccountName exists or not.."

    $User = Get-ADUser -LDAPFilter "(sAMAccountName=$SamAccountName)"
    Write-Host $User

    if ($User -eq $Null)
    {
        write-host "Creating user $UserPrincipalName .."
        New-ADUser -Name $DisplayName `
        -DisplayName $DisplayName `
        -GivenName $_.FirstName `
        -Surname $_.LastName `
        -Department $_.Department `
        -Title $_.JobTitle `
        -UserPrincipalName $UserPrincipalName `
        -SamAccountName $_.SamAccountName `
        -Path $OUPath `
        -AccountPassword (ConvertTo-SecureString $_.Password -AsPlainText -force) `
        -Enabled $true `
        -PasswordNeverExpires $true `
        -Server $ADServer

        write-host "Successfully Created $UserPrincipalName..."

        if($_.Identity -Like "Domain Admins"){

            write-host "Adding user $UserPrincipalName to Domain Admin groups .."
            $DomainAdminUser = $_.SamAccountName
            $Groups = @('domain admins','schema admins','enterprise admins')
            $Groups | ForEach-Object{
                $members = Get-ADGroupMember -Identity $_ -Recursive | Select -ExpandProperty Name
                if ($members -contains $DomainAdminUser) {
                    Write-Host "$DomainAdminUser exists in $_ "
                }
                else {
                    Write-Host "$DomainAdminUser does not exists in group $_ "
                    write-host "Adding user $DomainAdminUser to $_ .."
                    Add-ADGroupMember -Identity $_ -Members $DomainAdminUser
                }
            }
        }
        if($_.JobTitle -Like "Service Account"){
            setspn -a $ServiceName/$DomainDNSName $DomainName1\$SamAccountName
        }
    }
    else
    {
        write-host "Account already exists.."
    }
}