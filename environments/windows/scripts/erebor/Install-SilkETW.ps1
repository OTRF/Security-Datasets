# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:
# https://www.elastic.co/downloads/beats/winlogbeat
# https://github.com/fireeye/SilkETW

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

# Installing Service
try
{
    write-host "Creating the new SilkETW service.."
    New-Service -name SilkETW `
    -displayName SilkETW `
    -binaryPathName "C:\cfn\scripts\SilkETW\v8\SilkService\SilkService.exe" `
    -StartupType Manual `
    -Description "This is the SilkETW service to consume ETW events."
 
    #Installing Dependencies
    Start-Process -FilePath "C:\cfn\scripts\SilkETW\v8\Dependencies\dotNetFx45_Full_setup.exe" -ArgumentList "/Q" -Wait
    Start-Process -FilePath "C:\cfn\scripts\SilkETW\v8\Dependencies\vc2015_redist.x86.exe" -ArgumentList "/Q" -Wait

    # Download SilkServiceConfig.xml
    $SilkServiceConfigUrl = "https://raw.githubusercontent.com/Cyb3rWard0g/mordor/master/environments/windows/configs/erebor/erebor_SilkServiceConfig.xml"

    $OutputFile = Split-Path $SilkServiceConfigUrl -leaf
    $SilkServiceConfigPath = "C:\cfn\scripts\SilkETW\v8\SilkService\$OutputFile"

    # Download Config File
    write-Host "Downloading $OutputFile .."
    $wc = new-object System.Net.WebClient
    $wc.DownloadFile($SilkServiceConfigUrl, $SilkServiceConfigPath)
    if (!(Test-Path $SilkServiceConfigPath)){ write-Host "File $OutputFile does not exists.. "; break }

    # Starting Service
    $s = Get-Service -Name SilkETW
    while ($s.Status -ne 'Running'){
        Start-Service SilkETW; Start-Sleep 5
    }
catch {
    $ErrorMessage = $_.Exception.Message
    write-Host "SilkETW service installation failed with ERROR: $ErrorMessage "
    break
}