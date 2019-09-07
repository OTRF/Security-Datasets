# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:

[CmdletBinding()]
param (
    [Parameter(Mandatory=$true)]
    [string]$ADServer1NetBIOSName
)

Rename-Computer -NewName $ADServer1NetBIOSName -force -restart