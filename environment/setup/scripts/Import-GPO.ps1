# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:

[CmdletBinding()]
param (
    [Parameter(Mandatory=$false)]
    [string]$Url = "https://github.com/Cyb3rWard0g/mordor/raw/master/environment/setup/gpos/ShireGPOBackup.zip",

    [Parameter(Mandatory=$false)]
    [string]$DomainNetBIOSName = "shire"
)

$OutputFile = Split-Path $Url -leaf
$ZipFile = "c:\cfn\scripts\$outputFile"

# Download Zipped File
$wc = new-object System.Net.WebClient
$wc.DownloadFile($Url, $ZipFile)

if (!(Test-Path $ZipFile))
{
    write-Host "File $ZipFile does not exists.. "
    break
}

# Unzip file
$file = (Get-Item $ZipFile).Basename
expand-archive -path $Zipfile -DestinationPath "c:\cfn\scripts\"
if (!(Test-Path "c:\cfn\scripts\$file"))
{
    write-Host "$ZipFile could not be decompressed successfully.. "
    break
}

$GPOFolder = "c:\cfn\scripts\$file"
$GPOLocations = Get-ChildItem $GPOFolder | % {$_.BaseName}
$DCOU = "OU=Domain Controllers,DC=$DomainNetBIOSName,DC=com"
$WorkstationOU = "OU=Workstations,DC=$DomainNetBIOSName,DC=com"
$WEC = "OU=Servers,DC=$DomainNetBIOSName,DC=com"

foreach($GPO in $GPOLocations)
{
    $GPOName = $GPO.Replace("_"," ")
    write-Host "Creating GPO named: $GPOName "
    Import-GPO -BackupGpoName $GPOName -Path "$GPOFolder\$GPO" -TargetName $GPOName -CreateIfNeeded

    if(($GPOName -like "*controllers*") -or ($GPOName -like "*sam*"))
    {
        $gpLinks = $null
        $gPLinks = Get-ADOrganizationalUnit -Identity $DCOU -Properties name,distinguishedName, gPLink, gPOptions
        $GPO = Get-GPO -Name $GPOName
        If ($gPLinks.LinkedGroupPolicyObjects -notcontains $gpo.path)
        {
            write-Host "Linking GPO $GPOName to $DCOU "
            New-GPLink -Name $GPOName -Target $DCOU -Enforced yes
        }
        else
        {
            Write-Host "GpLink $GPOName already linked on $DCOU. Moving On."
        }

    }
    elseif($GPOName -like "*workstation*")
    {
        $gpLinks = $null
        $gPLinks = Get-ADOrganizationalUnit -Identity $WorkstationOU -Properties name,distinguishedName, gPLink, gPOptions
        $GPO = Get-GPO -Name $GPOName
        If ($gPLinks.LinkedGroupPolicyObjects -notcontains $gpo.path)
        {
            write-Host "Linking GPO $GPOName to $WorkstationOU "
            New-GPLink -Name $GPOName -Target $WorkstationOU -Enforced yes
        }
        else
        {
            Write-Host "GpLink $GPOName already linked on $WorkstationOU. Moving On."
        }

    }
    else{
        $OUS = @($DCOU, $WorkstationOU, $WEC)
        foreach($OU in $OUS)
        {
            $gpLinks = $null
            $gPLinks = Get-ADOrganizationalUnit -Identity $OU -Properties name,distinguishedName, gPLink, gPOptions
            $GPO = Get-GPO -Name $GPOName
            If ($gPLinks.LinkedGroupPolicyObjects -notcontains $gpo.path)
            {
                write-Host "Linking GPO $GPOName to $OU "
                New-GPLink -Name $GPOName -Target $OU -Enforced yes
            }
            else
            {
                Write-Host "GpLink $GPOName already linked on $OU. Moving On."
            }
        }

    }

}