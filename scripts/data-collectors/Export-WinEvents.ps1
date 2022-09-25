function Export-WinEvents
{
    <#
    .SYNOPSIS
       Exports events from one or more Windows event logs from a local or remote computer from a determined time range 
    .DESCRIPTION
       Script that leverages the System.Diagnostics.Eventing.Reader.EventLogSession class to collect event logs locally and remotely.
    .EXAMPLE
       PS> Export-WinEvents -Channel Security -TimeBucket 'Last 1 Minute' -OutputFolder C:\ProgramData\events -Verbose
    .EXAMPLE
       PS> @('Security','Microsoft-Windows-Sysmon/Operational') | Export-WinEvents -TimeBucket 'Last 1 Minute' -OutputFolder C:\ProgramData\events -Verbose
    .EXAMPLE
       PS> Export-WinEvents -Channel Security -EventID 4624,4625 -TimeBucket 'Last 1 Minute' -Verbose
    .EXAMPLE
       PS> Export-WinEvents -Channel Security -XPathQuery "*[System[EventID=4624]]"
    .EXAMPLE
       PS> $FromDate = Get-Date
       PS> $FilterLogs = @('Microsoft-WindowsAzure-Diagnostics/Heartbeat','Microsoft-WindowsAzure-Diagnostics/GuestAgent','Microsoft-Windows-SystemDataArchiver/Diagnostic','Microsoft-Windows-DSC/Operational','Windows PowerShell','Microsoft-Windows-Kernel-IO/Operational','Microsoft-Windows-PowerShell/Operational','Microsoft-Windows-Diagnosis-PCW/Operational')
       PS> $Events = Get-WinEvent -ListLog * |Where-Object {$_.LogName -notin $FilterLogs} |Where-Object {$_.RecordCount -gt 0} | ForEach-Object {Export-WinEvents -Channel $_.LogName -EndDate $FromDate -ErrorAction SilentlyContinue}
    .EXAMPLE
       PS> $FromDate = Get-Date
       PS> $FilterLogs = @('Microsoft-WindowsAzure-Diagnostics/Heartbeat','Microsoft-WindowsAzure-Diagnostics/GuestAgent','Microsoft-Windows-SystemDataArchiver/Diagnostic','Microsoft-Windows-DSC/Operational','Windows PowerShell','Microsoft-Windows-Kernel-IO/Operational','Microsoft-Windows-PowerShell/Operational','Microsoft-Windows-Diagnosis-PCW/Operational')
       PS> Get-WinEvent -ListLog * | Where-Object {$_.LogName -notin $FilterLogs} |Where-Object {$_.RecordCount -gt 0} | Select-Object -ExpandProperty LogName | Export-WinEvents -EndDate $FromDate -OutputFolder C:\ProgramData\events -ErrorAction SilentlyContinue
    .NOTES
        Author: Roberto Rodriguez (@Cyb3rWard0g)
        License: BSD 3-Clause
    .LINK
        https://github.com/OTRF/mordor
    #>

    [CmdletBinding(SupportsShouldProcess=$true, DefaultParameterSetName = 'QuickRange')]
    Param
    (
        # Event Log Channel to export
        [Parameter(ValueFromPipeline=$true,ValueFromPipelineByPropertyName=$true,Mandatory=$true)]
        [string[]]$Channel,

        # Event IDs to search for (String Array)
        [Parameter(ParameterSetName='QuickRange')]
        [Parameter(ParameterSetName='CustomRange')]
        [string[]]$EventID,

        # Quick Time Ranges
        [Parameter(ParameterSetName='QuickRange')]
        [ValidateSet('Last 1 Minute','Last 5 Minutes','Last 15 Minutes','Last 30 Minutes','Last 1 Hour','Last 12 Hours','Last 24 Hours')]
        [string]$TimeBucket,

        # Earliest date to collect logs from - last day by default
        [Parameter(ParameterSetName='CustomRange')]
        [datetime]$StartDate,

        # Latest date to collect logs from
        [Parameter(ParameterSetName='CustomRange')]
        [datetime]$EndDate,

        # XPATH Query
        [Parameter(ParameterSetName="XPATH-Query")]
        [string]$XPathQuery,

        # Output Folder
        [Parameter(Mandatory=$false)]
        [ValidateScript({
            if (Test-Path $_){$true}
            else {throw "Path $_ is not valid!"}
        })]
        [string]$OutputFolder
    )

    Begin {
        # Set Current Directory (PS Session Only)
        [Environment]::CurrentDirectory=(Get-Location -PSProvider FileSystem).ProviderPath

        function ConvertFrom-WinEventXml {
            [cmdletbinding()]
            Param (
                [parameter(ValueFromPipeline)]
                [System.Diagnostics.Eventing.Reader.EventLogRecord]$winEvent
            )
            Process {
                $eventXml = [xml]$winEvent.ToXML()
                $eventSystemKeys = $eventXml.Event.System
                $eventDataKeys = $eventXml.Event.EventData.Data
                $Properties = [ordered]@{}
                $Properties.EventSourceName = $eventSystemKeys.Provider.Name
                $Properties.Provider = $Properties.EventSourceName
                if ($eventSystemKeys.Provider.Guid)
                {
                    $Properties.ProviderGuid = $eventSystemKeys.Provider.Guid
                }
                $Properties.Level = $eventSystemKeys.Level
                $Properties.Keywords = $eventSystemKeys.Keywords
                $Properties.Channel = $eventSystemKeys.Channel
                $Properties.Computer = $eventSystemKeys.Computer
                $Properties.TimeCreated = $winEvent.TimeCreated.ToString("yyyy-MM-ddThh:mm:ss.fffZ")
                $Properties.TimeGenerated = ([System.TimeZoneInfo]::ConvertTimeToUtc($winEvent.TimeCreated)).ToString("yyyy-MM-ddThh:mm:ss.fffZ")
                $Properties.EventRecordID = $eventSystemKeys.EventRecordID
                $Properties.EventID = $winEvent.Id
                $Properties.Message = $winEvent.Message
                if ($eventXml.Event.EventData) {
                    $Properties.EventData = $eventXml.Event.EventData.OuterXml.ToString()
                }
                $Properties.Task = $winEvent.Task

                if ($eventDataKeys -and $eventDataKeys -is [array])
                {
                    For ($i=0; $i -lt $eventDataKeys.Count; $i++) {
                        if ($eventDataKeys[$i].GetType().Fullname -eq 'System.Xml.XmlElement')
                        {
                            $fieldValue = $winEvent.Properties[$i].value
                            if ($fieldValue -is [uint64]) {
                                $fieldValue = '0x' + ('{0:x}' -f $fieldValue)
                            }
                            elseif ($fieldValue -is [System.Security.Principal.SecurityIdentifier]) {
                                $fieldValue = $fieldValue.ToString()
                            }
                            $Properties[$eventDataKeys[$i].Name] = $fieldValue
                        }
                    }
                }

                [pscustomobject]$Properties
            }
        }

        function reverse {
            $arr = @($input)
            [array]::reverse($arr)
            $arr
        }

        Write-Verbose $PsCmdlet.ParameterSetName
        Write-Verbose "[+] Preparing XPATH Query"

        if ( $PsCmdlet.ParameterSetName -ne "XPATH-Query") {
            $XPathQuery = "*[System["
            if ($EventID)
            {
                $EventIDs = @()
                foreach($ID in $EventID){ $EventIDs += "EventID=$ID" }
                [string]$IDs = $EventIDs -join " or "
                $XPathQuery += "(" + $IDs + ') and '
            }

            if ( $PsCmdlet.ParameterSetName -eq "QuickRange")
            {
                Write-Verbose "[+] Time : Quick Range"
                $TimeDict = @{
                    "Last 1 Minute" = "60000";
                    "Last 5 Minutes" = "300000";
                    "Last 15 Minutes" = "900000";
                    "Last 30 Minutes" = "1800000";
                    "Last 1 Hour" = "3600000";
                    "Last 12 Hours" = "43200000";
                    "Last 24 Hours" = "86400000"
                }
                if(!($TimeBucket)) {
                    $TimeBucket = "Last 24 Hours"
                }
                Write-Verbose "[+] Time Bucket: $TimeBucket"
                $TimeFilter = "TimeCreated[timediff(@SystemTime) <= $($TimeDict[$TimeBucket])]]]"
                $XPathQuery += $TimeFilter
            }
            elseif ( $PsCmdlet.ParameterSetName -eq "CustomRange")
            {
                Write-Verbose "[+] Time : Custom Range"
                if ($StartDate -and $EndDate)
                {
                    Write-Verbose "[+] Time Window: From $StartDate to $EndDate"
                    $LTMS = [Xml.XmlConvert]::ToString(($StartDate).ToUniversalTime(), [System.Xml.XmlDateTimeSerializationMode]::Utc) 
                    $GTMS = [Xml.XmlConvert]::ToString(($EndDate).ToUniversalTime(), [System.Xml.XmlDateTimeSerializationMode]::Utc)
                    $CustomTimeFilter = "TimeCreated[@SystemTime >= $($GTMS) and @SystemTime <= $($LTMS)]]]"
                }
                elseif ($StartDate)
                {
                    Write-Verbose "[+] Time - Events before $StartDate"
                    $LTMS = [Xml.XmlConvert]::ToString(($StartDate).ToUniversalTime(), [System.Xml.XmlDateTimeSerializationMode]::Utc) 
                    $CustomTimeFilter = "TimeCreated[@SystemTime <= '$($LTMS)']]]"
                }
                else {
                    Write-Verbose "[+] Time - Events after $EndDate"
                    $GTMS = [Xml.XmlConvert]::ToString(($EndDate).ToUniversalTime(), [System.Xml.XmlDateTimeSerializationMode]::Utc)
                    $CustomTimeFilter = "TimeCreated[@SystemTime >= '$($GTMS)']]]"
                }
                Write-Verbose "[+] Custom Time Filter: $CustomTimeFilter"
                $XPathQuery += $CustomTimeFilter
            }
            else {
                Write-Verbose "[+] Time : Default to 1 minute"
                $TimeFilter = "TimeCreated[timediff(@SystemTime) <= 60000]]]"
                $XPathQuery += $TimeFilter
            }
        }
        $AllEvents = @{}
    }
    Process {
        Write-Verbose "[+] Collecting Windows Events"
        if ($PSCmdlet.ShouldProcess($Channel))
        {
            try
            {   
                Write-Verbose "[+] Exporting events from $Channel"
                Write-Verbose "[+] Running the following XPathQuery: $XPathQuery"
                $AllEvents["$Channel"] = Get-WinEvent -LogName $Channel -FilterXPath $XPathQuery | ConvertFrom-WinEventXml | reverse       
            }  
            catch
            { 
                write-warning $_.Exception         
            }
        }
    }
    End {
        $utf8NoBom = New-Object System.Text.UTF8Encoding $false

        foreach ($key in $AllEvents.keys) {
            if ($OutputFolder)
            {
                # Get hostname
                $computerName = [system.environment]::MachineName
                # Updating OutputPath
                $prefix = "$key".Replace('-','').Replace('\','').Replace('/','')
                $suffix = "$(get-date -format yyyy-MM-ddTHHmmssff).json"
                $fileName = -join("$computerName","_","Windows_","$prefix","_",$suffix)
                
                $newOutputPath =  Join-Path -Path "$OutputFolder" -ChildPath "$fileName"

                Write-Verbose "[+] Exporting all events to $newOutputPath"
                $JsonStrings = $AllEvents["$key"] | ConvertTo-Json -Compress
                if (!(Test-Path $newOutputPath)) {
                    [System.IO.File]::WriteAllLines($newOutputPath, $JsonStrings, $Utf8NoBom)
                }
                else {
                    [System.IO.File]::AppendAllLines($newOutputPath, $JsonStrings, $Utf8NoBom)
                }
            }
            else {
                Write-Verbose "[+] Returning All Events.."
                Write-Verbose "[+] Channel: $key"
                return $AllEvents["$key"]
            }   
        } 
    }
}

function Clear-WinEvents
{
    <#
    .SYNOPSIS
       Clear Windows Event Logs
    .DESCRIPTION
       Script that leverages the System.Diagnostics.Eventing.Reader.EventLogSession .NET class to clear Windows event logs.
    .EXAMPLE
       PS> Clear-WinEvents -Channel Security
    .EXAMPLE
       PS> @('Security','Microsoft-Windows-Sysmon/Operational') | Clear-WinEvents
    .NOTES
        Author: Roberto Rodriguez (@Cyb3rWard0g)
        License: BSD 3-Clause
    .LINK
        https://github.com/OTRF/mordor
    #>

    [CmdletBinding(SupportsShouldProcess=$true)]
    Param
    (
        # Event Log Channel to export
        [Parameter(ValueFromPipeline=$true,ValueFromPipelineByPropertyName=$true,Mandatory=$true)]
        [string[]]$Channel
    )

    Process
    {
        if ($PSCmdlet.ShouldProcess($Channel))
        {
            try
            {   
                (New-Object System.Diagnostics.Eventing.Reader.EventLogSession).ClearLog("$Channel")
            }  
            catch
            { 
                write-warning $_.Exception         
            }
        }
    }
}
