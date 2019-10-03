# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:
# https://www.elastic.co/downloads/beats/winlogbeat
# https://github.com/fireeye/SilkETW
# https://docs.microsoft.com/en-us/dotnet/framework/migration-guide/how-to-determine-which-versions-are-installed#version_table
# https://medium.com/@cosmin.ciobanu/enhanced-endpoint-detection-using-sysmon-and-wef-3b65d491ff95

[CmdletBinding()]
param (
    [Parameter(Mandatory=$true)]
    [ValidateSet("Sysmon","SilkETW")]
    [string]$EndpointAgent
)

write-host "Installing $EndpointAgent .."

if($EndpointAgent -eq "Sysmon")
{
    $URL = "https://download.sysinternals.com/files/Sysmon.zip"
}
else
{
    $Url = "https://github.com/fireeye/SilkETW/releases/download/v0.8/SilkETW_SilkService_v8.zip"
}

$OutputFile = Split-Path $Url -leaf
$ZipFile = "c:\cfn\scripts\$OutputFile"

# Download Zipped File
write-Host "Downloading $OutputFile .."
$wc = new-object System.Net.WebClient
$wc.DownloadFile($Url, $ZipFile)
if (!(Test-Path $ZipFile)){ write-Host "File $ZipFile does not exists.. "; break }

# Unzip file
write-Host "Decompressing $OutputFile .."
$file = (Get-Item $ZipFile).Basename
expand-archive -path $Zipfile -DestinationPath "c:\cfn\scripts\$file"
if (!(Test-Path "c:\cfn\scripts\$file")){ write-Host "$ZipFile could not be decompressed successfully.. "; break }

if($EndpointAgent -eq "Sysmon")
{
    # Downloading Sysmon Configuration
    write-Host "Downloading Sysmon config.."
    $SysmonFile = "c:\cfn\scripts\shire_sysmon.xml"
    $SysmonConfigUrl = "https://raw.githubusercontent.com/Cyb3rWard0g/mordor/master/environments/windows/configs/shire/shire_sysmon.xml"
    $wc.DownloadFile($SysmonConfigUrl, $SysmonFile)
    if (!(Test-Path $SysmonFile)){ write-Host "File $SysmonFile does not exists.. "; break }

    # Installing Sysmon
    write-Host "Installing Sysmon.."
    & c:\cfn\scripts\Sysmon\Sysmon.exe -i c:\cfn\scripts\shire_sysmon.xml -accepteula -h md5,sha256,imphash -l -n
    
    write-Host "Setting Sysmon to start automatically.."
    & sc.exe config Sysmon start= auto

    # Setting Sysmon Channel Access permissions
    write-Host "Setting up Channel Access permissions for Microsoft-Windows-Sysmon/Operational "
    New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-Sysmon/Operational" -Name "ChannelAccess" -PropertyType String -Value "O:BAG:SYD:(A;;0xf0005;;;SY)(A;;0x5;;;BA)(A;;0x1;;;S-1-5-32-573)(A;;0x1;;;NS)" -Force
    
    write-Host "Restarting Log Services .."
    $LogServices = @("Sysmon", "Windows Event Log")

    # Restarting Log Services
    foreach($LogService in $LogServices)
    {
        write-Host "Restarting $LogService .."
        Restart-Service -Name $LogService -Force

        write-Host "Verifying if $LogService is running.."
        $s = Get-Service -Name $LogService
        while ($s.Status -ne 'Running'){Start-Service $LogService; Start-Sleep 3}
        Start-Sleep 5
        write-Host "$LogService is running.."
    }
}
else
{
    #Installing Dependencies
    #.NET Framework 4.5	All Windows operating systems: 378389
    $DotNetDWORD = 378388
    $DotNet_Check = Get-ChildItem "hklm:SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full\" | Get-ItemPropertyValue -Name Release | % { $_ -ge $DotNetDWORD }
    if(!$DotNet_Check)
    {
        write-Host "NET Framework 4.5 or higher not installed.."
        & C:\cfn\scripts\$file\v8\Dependencies\dotNetFx45_Full_setup.exe /q /passive /norestart
        start-sleep -s 5
    }
    $MVC_Check = Get-ItemProperty HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | where {$_.displayname -like "Microsoft Visual C++*"} | Select-Object DisplayName, DisplayVersion
    if (!$MVC_Check)
    {
        write-Host "Microsoft Visual C++ not installed.."
        & C:\cfn\scripts\$file\v8\Dependencies\vc2015_redist.x86.exe /q /passive /norestart
        start-sleep -s 5
    }

    # Download SilkServiceConfig.xml
    $SilkServiceConfigUrl = "https://raw.githubusercontent.com/Cyb3rWard0g/mordor/master/environments/windows/configs/erebor/erebor_SilkServiceConfig.xml"

    $OutputFile = Split-Path $SilkServiceConfigUrl -leaf
    $SilkServiceConfigPath = "C:\cfn\scripts\$file\v8\SilkService\SilkServiceConfig.xml"

    # Download Config File
    write-Host "Downloading $OutputFile .."
    $wc = new-object System.Net.WebClient
    $wc.DownloadFile($SilkServiceConfigUrl, $SilkServiceConfigPath)
    if (!(Test-Path $SilkServiceConfigPath)){ write-Host "SilkServiceConfig.xml does not exists.. "; break }

    # Installing Service
    write-host "Creating the new SilkETW service.."
    New-Service -name SilkETW `
    -displayName SilkETW `
    -binaryPathName "C:\cfn\scripts\$file\v8\SilkService\SilkService.exe" `
    -StartupType Automatic `
    -Description "This is the SilkETW service to consume ETW events."

    Start-Sleep -s 10

    # Restarting Service
    write-host "Restarting SilkETW service.."
    Restart-Service -Name SilkETW -Force
}