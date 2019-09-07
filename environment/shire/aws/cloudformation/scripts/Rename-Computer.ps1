# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:

[CmdletBinding()]
param (
    [Parameter(Mandatory=$true)]
    [string]$DomainNetBiosName
)

Rename-Computer -NewName $DomainNetBiosName -force -restart