# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:

$SysmonURL = "https://download.sysinternals.com/files/Sysmon.zip"

$OutputFile = Split-Path $SysmonURL -leaf
$ZipFile = "c:\cfn\scripts\$outputFile"

# Download Zipped File
write-Host "Downloading $OutputFile .."
$wc = new-object System.Net.WebClient
$wc.DownloadFile($SysmonUrl, $ZipFile)
if (!(Test-Path $ZipFile)){ write-Host "File $ZipFile does not exists.. "; break }

# Unzip file
write-Host "Decompressing $OutputFile .."
$file = (Get-Item $ZipFile).Basename
expand-archive -path $Zipfile -DestinationPath "c:\cfn\scripts\$file"
if (!(Test-Path "c:\cfn\scripts\$file")){ write-Host "$ZipFile could not be decompressed successfully.. "; break }

write-Host "Downloading Sysmon config.."
$SysmonFile = "c:\cfn\scripts\shire_sysmon.xml"
$SysmonConfigUrl = "https://raw.githubusercontent.com/Cyb3rWard0g/mordor/master/environment/setup/configs/shire_sysmon.xml"
$wc.DownloadFile($SysmonConfigUrl, $SysmonFile)
if (!(Test-Path $SysmonFile)){ write-Host "File $SysmonFile does not exists.. "; break }

try {
    write-Host "Installing Sysmon.."
    & c:\cfn\scripts\Sysmon\Sysmon.exe -i c:\cfn\scripts\shire_sysmon.xml -accepteula -h md5,sha256,imphash -l -n
    
    write-Host "Setting Sysmon to start automatically.."
    & sc.exe config Sysmon start= auto

    write-Host "Setting up Channel Access permissions for Microsoft-Windows-Sysmon/Operational "
    New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-Sysmon/Operational" -Name "ChannelAccess" -PropertyType String -Value "O:BAG:SYD:(A;;0xf0005;;;SY)(A;;0x5;;;BA)(A;;0x1;;;S-1-5-32-573)(A;;0x1;;;NS)" -Force
    
    write-Host "Restarting Sysmon .."
    Restart-Service -Name Sysmon
    
    write-Host "Verifying if Sysmon is running.."
    $s = Get-Service -Name Sysmon
    while ($s.Status -ne 'Running'){Start-Service Sysmon; Start-Sleep 3}
    Start-Sleep 5
    write-Host "Sysmon is running.."

}
catch {
    $ErrorMessage = $_.Exception.Message
    write-Host "Sysmon installation failed with ERROR: $ErrorMessage "
    break
}
