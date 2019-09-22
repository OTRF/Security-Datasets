# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:
# https://www.elastic.co/downloads/beats/winlogbeat
# https://github.com/fireeye/SilkETW
# https://docs.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#version_table

$Url = "https://github.com/fireeye/SilkETW/releases/download/v0.8/SilkETW_SilkService_v8.zip"

$OutputFile = Split-Path $Url -leaf
$ZipFile = "c:\cfn\scripts\$OutputFile"

# Download Zipped File
write-Host "Downloading $OutputFile .."
$wc = new-object System.Net.WebClient
$wc.DownloadFile($Url, $ZipFile)
if (!(Test-Path $ZipFile)){ write-Host "File $ZipFile does not exists.. "; break }

# Unzip file
write-Host "Decompressing $OutputFile .."
expand-archive -path $Zipfile -DestinationPath "c:\cfn\scripts\SilkETW"
if (!(Test-Path "c:\cfn\scripts\SilkETW")){ write-Host "$ZipFile could not be decompressed successfully.. "; break }

#Installing Dependencies
#.NET Framework 4.5	All Windows operating systems: 378389
$DotNetDWORD = 378388
$DotNet_Check = Get-ChildItem "hklm:SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full\" | Get-ItemPropertyValue -Name Release | % { $_ -ge $DotNetDWORD }
if(!$DotNet_Check)
{
    write-Host "NET Framework 4.5 or higher not installed.."
    & C:\cfn\scripts\SilkETW\v8\Dependencies\dotNetFx45_Full_setup.exe /q /passive /norestart
}
$MVC_Check = Get-ItemProperty HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | where {$_.displayname -like "Microsoft Visual C++*"} | Select-Object DisplayName, DisplayVersion
if (!$MVC_Check)
{
    write-Host "Microsoft Visual C++ not installed.."
    & C:\cfn\scripts\SilkETW\v8\Dependencies\vc2015_redist.x86.exe /q /passive /norestart
}

# Download SilkServiceConfig.xml
$SilkServiceConfigUrl = "https://raw.githubusercontent.com/Cyb3rWard0g/mordor/master/environments/windows/configs/erebor/erebor_SilkServiceConfig.xml"

$OutputFile = Split-Path $SilkServiceConfigUrl -leaf
$SilkServiceConfigPath = "C:\cfn\scripts\SilkETW\v8\SilkService\SilkServiceConfig.xml"

# Download Config File
write-Host "Downloading $OutputFile .."
$wc = new-object System.Net.WebClient
$wc.DownloadFile($SilkServiceConfigUrl, $SilkServiceConfigPath)
if (!(Test-Path $SilkServiceConfigPath)){ write-Host "SilkServiceConfig.xml does not exists.. "; break }

# Installing Service
write-host "Creating the new SilkETW service.."
New-Service -name SilkETW `
-displayName SilkETW `
-binaryPathName "C:\cfn\scripts\SilkETW\v8\SilkService\SilkService.exe" `
-StartupType Automatic `
-Description "This is the SilkETW service to consume ETW events."

Start-Sleep -s 5

# Restarting Service
write-host "Restarting SilkETW service.."
Restart-Service -Name SilkETW -Force