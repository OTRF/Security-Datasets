function Export-WinEvents
{
    <#
    .SYNOPSIS
       Exports events from one or more Windows event logs from a local or remote computer from a determined time range 
    .DESCRIPTION
       Script that leverages the System.Diagnostics.Eventing.Reader.EventLogSession class to collect event logs locally and remotely.
    .EXAMPLE
       PS> Export-WinEvents -Channel Security -TimeBucket 'Last 1 Minute' -OutputPath "MordorDataset_$(get-date -format yyyy-MM-ddTHHmmssff).json" -Verbose
    .EXAMPLE
       PS> @('Security','Microsoft-Windows-Sysmon/Operational') | Export-WinEvents -TimeBucket 'Last 1 Minute' -OutputPath "MordorDataset_$(get-date -format yyyy-MM-ddTHHmmssff).json" -Verbose
    .EXAMPLE
       PS> Export-WinEvents -Channel Security -EventID 4624,4625 -TimeBucket 'Last 1 Minute' -Verbose
    .EXAMPLE
       PS> Export-WinEvents -Channel Security -FilterXPath "*[System[EventID=4624]"
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
        [string[]]$Channel = 'Security',

        # Event IDs to search for (String Array)
        [Parameter(ParameterSetName='QuickRange')]
        [Parameter(ParameterSetName='CustomRange')]
        [string[]]$EventID,

        # Quick Time Ranges
        [Parameter(ParameterSetName='QuickRange')]
        [ValidateSet('Last 1 Minute','Last 5 Minutes','Last 15 Minutes','Last 30 Minutes','Last 1 Hour','Last 12 Hours','Last 24 Hours')]
        [string]$TimeBucket = "Last 1 Minute", 

        # Earliest date to collect logs from - last day by default
        [Parameter(ParameterSetName='CustomRange')]
        [datetime]$StartDate,

        # Latest date to collect logs from
        [Parameter(ParameterSetName='CustomRange')]
        [datetime]$EndDate,

        # XPATH Query
        [Parameter(ParameterSetName="XPATH-Query")]
        [string]$XPathQuery,

        # Output File
        [Parameter()]
        [string]$OutputPath="MordorDataset.json"
    )

    Begin
    {
        # Set Current Directory (PS Session Only)
        [Environment]::CurrentDirectory=(Get-Location -PSProvider FileSystem).ProviderPath
        # Remote File if it exists already
        if((Test-Path $OutputPath -ErrorAction SilentlyContinue)) {
            Remove-Item -Force:$Force $OutputPath -ErrorAction Stop
        }

        function Parse-XML {
            [cmdletbinding()]
            Param (
                [parameter(ValueFromPipeline)]
                $event
            )
            Process {
                $eventXml = [xml]$event.ToXML()
                $eventSystemKeys = $eventXml.Event.System
                $eventDataKeys = $eventXml.Event.EventData.Data
                $Properties = @{}
                $Properties.Channel = $eventSystemKeys['Channel'].'#text'
                $Properties.SourceName = $eventSystemKeys['Provider'].Name
                if ($eventSystemKeys['Provider'].Guid)
                {
                    $Properties.ProviderGuid = $eventSystemKeys['Provider'].Guid
                }
                $Properties.Level = $eventSystemKeys['Level'].'#text'
                $Properties.Keywords = $eventSystemKeys['Keywords'].'#text'
                $Properties.Hostname = $eventSystemKeys['Computer'].'#text'
                $Properties.TimeCreated = $event.TimeCreated.ToString("yyyy-MM-ddThh:mm:ss.fffZ")
                $Properties['@timestamp'] = $Properties.TimeCreated
                $Properties.EventID = $event.Id
                $Properties.Message = $event.Message
                $Properties.Task = $eventSystemKeys['Task'].'#text'

                if ($eventDataKeys -and $eventDataKeys -is [array])
                {
                    For ($i=0; $i -lt $eventDataKeys.Count; $i++) {
                        if ($eventDataKeys[$i].GetType().Fullname -eq 'System.Xml.XmlElement')
                        {
                            $Properties[$eventDataKeys[$i].Name] = $eventDataKeys[$i].'#text'
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

        Write-Verbose "Handling XPATH Query"
        if ( $PsCmdlet.ParameterSetName -ne "XPATH-Query")
        {
            $XPathQuery = "*[System["
            if ($EventID)
            {
                $EventIDs = @()
                foreach($ID in $EventID){ $EventIDs += "EventID=$ID" }
                [string]$IDs = $EventIDs -join " or "
                $XPathQuery += "(" + $IDs + ') and '
            }
            if ($TimeBucket)
            {
                $TimeDict = @{
                    "Last 1 Minute" = "60000";
                    "Last 5 Minutes" = "300000";
                    "Last 15 Minutes" = "900000";
                    "Last 30 Minutes" = "1800000";
                    "Last 1 Hour" = "3600000";
                    "Last 12 Hours" = "43200000";
                    "Last 24 Hours" = "86400000"
                }
                $TimeFilter = "TimeCreated[timediff(@SystemTime) <= $($TimeDict[$TimeBucket])]]]"
                $XPathQuery += $TimeFilter
            }
            if ($StartDate -and $EndDate)
            {
               $LTMS = ((Get-Date) - $StartDate).TotalMilliseconds
               $GTMS = ((Get-Date) - $EndDate).TotalMilliseconds
               $CustomTimeFilter = "TimeCreated[@SystemTime>=$($GTMS) and @SystemTime<=$($LTMS)]]]"
               $XPathQuery + $CustomTimeFilter
            }
        }

        $AllEvents = @()
    }
    Process
    {
        Write-Verbose "Collecting Windows Events"
        if ($PSCmdlet.ShouldProcess($Channel))
        {
            try
            {   
                Write-Verbose "Exporting events from $Channel"
                $AllEvents += Get-WinEvent -LogName $Channel -FilterXPath $XPathQuery | Parse-XML | reverse       
            }  
            catch
            { 
                write-warning $_.Exception         
            }
        }
    }
    End
    {
        Write-Verbose "Exporting all events to $OutputPath"
        $utf8NoBom = New-Object System.Text.UTF8Encoding $false
        $AllEvents | % {
            $line = ConvertTo-Json $_ -Compress
            if (!(Test-Path $OutputPath))
            {
                [System.IO.File]::WriteAllLines($OutputPath, $line, [System.Text.UTF8Encoding]($False))
            }
            else
            {
                [System.IO.File]::AppendAllLines($OutputPath, [string[]]$line, [System.Text.UTF8Encoding]($False))
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
        [string[]]$Channel = 'Security'
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
Export-ModuleMember -Function * -Alias *