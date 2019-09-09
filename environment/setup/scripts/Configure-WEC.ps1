# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# Referneces:
# https://www.ultimatewindowssecurity.com/webinars/watch_get.aspx?Attach=1&Type=SlidesPDF&ID=1426
# https://community.softwaregrp.com/dcvta86296/attachments/dcvta86296/arcsight-discussions/24729/1/Protect2015-WindowsEventForwarding.pdf
# https://docs.microsoft.com/en-us/biztalk/technical-guides/settings-that-can-be-modified-to-improve-network-performance

[CmdletBinding()]
param (
    [Parameter(Mandatory=$false)]
    [string]$SubscriptionsUrl = "https://github.com/Cyb3rWard0g/mordor/raw/master/environment/setup/wef-subscriptions/ShireSubscriptions.zip"
)

# Stand-alone service instead of shared
scconfig wecsvc type=own

# ********* Setting WinRM Configs for WEC ***********
winrm quickconfig -q
winrm quickconfig -transport:http

winrm set winrm/config '@{MaxEnvelopeSizekb="500"}'
winrm set winrm/config '@{MaxTimeoutms="60000"}'
winrm set winrm/config '@{MaxBatchItems="32000"}'
winrm set winrm/config/client '@{NetworkDelayms="5000"}'
winrm set winrm/config/service '@{MaxConcurrentOperations="4294967295"}'
winrm set winrm/config/service '@{MaxConcurrentOperationsPerUser="1500"}'
winrm set winrm/config/service '@{MaxConnections="500"}'
winrm set winrm/config/service '@{MaxPacketRetrievalTimeSeconds="120"}'
winrm set winrm/config/winrs '@{IdleTimeout="7200000"}'
winrm set winrm/config/winrs '@{MaxConcurrentUsers="10"}'
winrm set winrm/config/winrs '@{MaxShellRunTime="2147483647"}'
winrm set winrm/config/winrs '@{MaxProcessesPerShell="25"}'
winrm set winrm/config/winrs '@{MaxMemoryPerShellMB="1024"}'
winrm set winrm/config/winrs '@{MaxShellsPerUser="30"}'

winrm set winrm/config/service '@{AllowUnencrypted="true"}'
winrm set winrm/config/client '@{AllowUnencrypted="true"}'
winrm set winrm/config/service/auth '@{Basic="true"}'
winrm set winrm/config/client/auth '@{Basic="true"}'
winrm set winrm/config/listener?Address=*+Transport=HTTP '@{Port="5985"}'

Restart-Service WinRM

# ********** Updating ForwardedEvents log size *******
wevtutil sl ForwardedEvents /ms:8589934592

# ********** Starting WEC Service *************
Stop-Service wecsvc
Set-Service wecsvc -StartupType "Automatic"
# Stand-alone service instead of shared
# Powershell version of : sc config wecsvc type=own
$s = (Get-WmiObject win32_service -filter "Name='wecsvc'")
$s.Change($null, $null, 16)
Start-Service wecsvc

# ******** Importing WEF subscriptions *******
$OutputFile = Split-Path $Url -leaf
$ZipFile = "c:\cfn\scripts\$outputFile"

# Download Zipped File
write-Host "Downloading $OutputFile .."
$wc = new-object System.Net.WebClient
$wc.DownloadFile($Url, $ZipFile)

if (!(Test-Path $ZipFile))
{
    write-Host "File $ZipFile does not exists.. "
    break
}

# Unzip file
write-Host "Decompressing $ZipFile .."
$file = (Get-Item $ZipFile).Basename
expand-archive -path $Zipfile -DestinationPath "c:\cfn\scripts\"

if (!(Test-Path "c:\cfn\scripts\$file"))
{
    write-Host "$ZipFile could not be decompressed successfully.. "
    break
}

# Importing Subscriptions
if (Test-Path "c:\cfn\scripts\$file")
{
    write-Host "Importing WEF Subscriptions.. "
    Get-ChildItem "c:\cfn\scripts\$file" | ForEach-Object { wecutil cs $_.Name}
}
else {
    write-Host "c:\cfn\scripts\$file does not exist.."
    break
}

# ********** Additional Tunning ***************
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-ForwardedEvents" -Name "BufferSize" -Type "DWORD" -Value "2048"
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-ForwardedEvents" -Name "FlushTimer" -Type "DWORD" -Value "0"
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-ForwardedEvents" -Name "MaximumBuffers" -Type "DWORD" -Value "8192"
Set-ItemProperty -Path "HKLM\SYSTEM\CurrentControlSet\Control\WMI\Autologger\EventLog-ForwardedEvents" -Name "MinimumBuffers" -Type "DWORD" -Value "0"

# The TcpTimedWaitDelay value determines the length of time that a connection stays in the TIME_WAIT state when being closed
New-ItemProperty –Path "HKLM:\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" –Name "TcpTimedWaitDelay" –Type "Dword" –Value "30"

# Configure Event Collector
wecutil qc -quiet

Restart-Computer -Force