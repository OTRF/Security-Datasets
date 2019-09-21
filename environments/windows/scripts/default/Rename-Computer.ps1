# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:

[CmdletBinding()]
param (
    [Parameter(Mandatory=$true)]
    [string]$NewComputerName,

    [Parameter(Mandatory=$false)]
    [switch]$reboot
)
write-host "Renaming computer to $NewComputerName .."
if($reboot)
{
    Rename-Computer -NewName $NewComputerName -force -restart
}
else
{
    Rename-Computer -NewName $NewComputerName -force
}