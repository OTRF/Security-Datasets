# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:

[CmdletBinding()]
param (
    [Parameter(Mandatory=$true)]
    [string]$NewComputerName
)
write-host "Renaming computer to $NewComputerName to $_ .."
Rename-Computer -NewName $NewComputerName -force -restart