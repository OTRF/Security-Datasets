# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:

[CmdletBinding()]
param (
    [Parameter(Mandatory=$true)]
    [string]$SecurityGroup,

    [Parameter(Mandatory=$true)]
    [string]$DomainNetBIOSName
)

$ParentPath = "DC=$DomainNetBIOSName,DC=com"

write-host "Creating Security Group $SecurityGroup on $ParentPath .." 
New-ADGroup -Name $SecurityGroup -GroupCategory Security -GroupScope Global `
    -DisplayName $SecurityGroup -Path "CN=Users,$ParentPath" `
    -Description "Security group $SecurityGroup" -PassThru