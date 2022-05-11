function Send-AzMonitorCustomLogs
{
    <#
    .SYNOPSIS
    Sends custom logs to a specific table in Azure Monitor.
    
    .DESCRIPTION
    Script to send data to a data collection endpoint which is a unique connection point for your subscription.
    The payload sent to Azure Monitor must be in JSON format. A data collection rule is needed in your Azure tenant that understands the format of the source data, potentially filters and transforms it for the target table, and then directs it to a specific table in a specific workspace.
    You can modify the target table and workspace by modifying the data collection rule without any change to the REST API call or source data.
    
    .PARAMETER LogPath
    Path to the log file or folder to read logs from and send them to Azure Monitor.
    
    .PARAMETER appId
    Azure Active Directory application to authenticate against the API to send logs to Azure Monitor data collection endpoint.
    This script supports the Client Credential Grant Flow.

    .PARAMETER appSecret
    Secret text to use with the Azure Active Directory application to authenticate against the API for the Client Credential Grant Flow.

    .PARAMETER TenantId
    ID of Tenant
    
    .PARAMETER DcrImmutableId
    Immutable ID of the data collection rule used to process events flowing to an Azure Monitor data table.
    
    .PARAMETER DceURI
    Uri of the data collection endpoint used to host the data collection rule.

    .PARAMETER StreamName
    Name of stream to send data to before being procesed and sent to an Azure Monitor data table.
    
    .PARAMETER TimestampField
    Specific field available in your custom log to select as the main timestamp. This will be the TimeGenerated field in your table. By default, this script uses a current timestamp.
    
    .PARAMETER ShowProgressBar
    Show a PowerShell progress bar. Disabled by default.

    .EXAMPLE
    PS> . .\Send-AzMonitorCustomLogs.ps1
    PS> Send-AzMonitorCustomLogs -LogPath C:\WinEvents.json -appId 'XXXX' -appSecret 'XXXXXX' -TenantId 'XXXXXX' -DcrImmutableId 'dcr-XXXX' -DceURI 'https://XXXX.westus2-1.ingest.monitor.azure.com' -StreamName 'Custom-WindowsEvent' -TimestampField 'TimeCreated'
    
    .EXAMPLE
    PS> . .\Send-AzMonitorCustomLogs.ps1
    PS> Send-AzMonitorCustomLogs -LogPath C:\WinEvents.json -appId 'XXXX' -appSecret 'XXXXXX' -TenantId 'XXXXXX' -DcrImmutableId 'dcr-XXXX' -DceURI 'https://XXXX.westus2-1.ingest.monitor.azure.com' -StreamName 'Custom-WindowsEvent' -TimestampField 'TimeCreated' -Debug
    
    .EXAMPLE
    PS> . .\Send-AzMonitorCustomLogs.ps1
    PS> Send-AzMonitorCustomLogs -LogPath C:\WinEventsFolder\ -appId 'XXXX' -appSecret 'XXXXXX' -TenantId 'XXXXXX' -DcrImmutableId 'dcr-XXXX' -DceURI 'https://XXXX.westus2-1.ingest.monitor.azure.com' -StreamName 'Custom-WindowsEvent' -TimestampField 'TimeCreated' -Debug
    
    .NOTES
    # Author: Roberto Rodriguez (@Cyb3rWard0g)
    # License: MIT

    # Reference:
    # https://docs.microsoft.com/en-us/azure/azure-monitor/logs/custom-logs-overview
    # https://docs.microsoft.com/en-us/azure/azure-monitor/logs/tutorial-custom-logs-api#send-sample-data
    # https://securitytidbits.wordpress.com/2017/04/14/powershell-and-gzip-compression/

    # Custom Logs Limit
    # Maximum size of API call: 1MB for both compressed and uncompressed data
    # Maximum data/minute per DCR: 1 GB for both compressed and uncompressed data. Retry after the duration listed in the Retry-After header in the response.
    # Maximum requests/minute per DCR: 6,000. Retry after the duration listed in the Retry-After header in the response.

    .LINK
    https://github.com/OTRF/Security-Datasets
    #>
    [CmdletBinding()]
    param (
        [Parameter(Mandatory=$true)]
        [ValidateScript({
            foreach ($f in $_)
            {
                if( -Not ($f | Test-Path) ){
                    throw "File or folder does not exist"
                }
            }
            return $true
        })]
        [string[]]$LogPath,

        [Parameter(Mandatory=$true)]
        [string]$appId,

        [Parameter(Mandatory=$true)]
        [string]$appSecret,

        [Parameter(Mandatory=$true)]
        [string]$TenantId,

        [Parameter(Mandatory=$true)]
        [string]$DcrImmutableId,

        [Parameter(Mandatory=$true)]
        [string]$DceURI,

        [Parameter(Mandatory=$true)]
        [string]$StreamName,

        [Parameter(Mandatory=$false)]
        [string]$TimestampField,

        [Parameter(Mandatory=$false)]
        [switch]$ShowProgressBar
    )

    If ($PSBoundParameters['Debug']) {
        $DebugPreference = 'Continue'
    }

    @("
_________                    .____________                  __                   .____              ____          
/   _____/  ____    ____    __| _/\_   ___ \  __ __  _______/  |_  ____    _____  |    |     ____   / ___\  ______ 
\_____  \ _/ __ \  /    \  / __ | /    \  \/ |  |  \/  ___/\   __\/  _ \  /     \ |    |    /  _ \ / /_/  >/  ___/ 
/        \\  ___/ |   |  \/ /_/ | \     \____|  |  /\___ \  |  | (  <_> )|  Y Y  \|    |___(  <_> )\___  / \___ \  
/_______  / \___  >|___|  /\____ |  \______  /|____//____  > |__|  \____/ |__|_|  /|_______ \\____//_____/ /____  > 
        \/      \/      \/      \/         \/            \/                     \/         \/                   \/                                                                                                            
___________         _____                                     _____                   .__   __                      
\__    ___/____    /  _  \  ________ __ __ _______   ____    /     \    ____    ____  |__|_/  |_  ____ _______      
  |    |  /  _ \  /  /_\  \ \___   /|  |  \\_  __ \_/ __ \  /  \ /  \  /  _ \  /    \ |  |\   __\/  _ \\_  __ \     
  |    | (  <_> )/    |    \ /    / |  |  / |  | \/\  ___/ /    Y    \(  <_> )|   |  \|  | |  | (  <_> )|  | \/     
  |____|  \____/ \____|__  //_____ \|____/  |__|    \___  >\____|__  / \____/ |___|  /|__| |__|  \____/ |__|        
                        \/       \/                    \/         \/              \/                          V0.2

Creator: Roberto Rodriguez @Cyb3rWard0g
License: MIT
    ")

    $ErrorActionPreference = "Stop"

    # Aggregate files from input paths
    $all_datasets = @()
    foreach ($file in $LogPath){
        if ((Get-Item $file) -is [system.io.fileinfo]){
            $all_datasets += (Resolve-Path -Path $file)
        }
        elseif ((Get-Item $file) -is [System.IO.DirectoryInfo]){
            $folderfiles = Get-ChildItem -Path $file -Recurse -Include *.json
            $all_datasets += $folderfiles
        }
    }

    write-Host "*******************************************"
    Write-Host "[+] Obtaining access token.."
    ## Obtain a bearer token used to authenticate against the data collection endpoint
    $scope = [System.Net.WebUtility]::UrlEncode("https://monitor.azure.com//.default")   
    $body = "client_id=$appId&scope=$scope&client_secret=$appSecret&grant_type=client_credentials";
    $headers = @{"Content-Type" = "application/x-www-form-urlencoded"};
    $uri = "https://login.microsoftonline.com/$tenantId/oauth2/v2.0/token"
    $bearerToken = (Invoke-RestMethod -Uri $uri -Method "Post" -Body $body -Headers $headers).access_token
    Write-Debug $bearerToken

    Function Send-DataToDCE($payload, $size){
        write-debug "############ Sending Data ############"
        write-debug "JSON array size: $($size/1mb) MBs"
        
        # Initialize Headers and URI for POST request to the Data Collection Endpoint (DCE)
        $headers = @{"Authorization" = "Bearer $bearerToken"; "Content-Type" = "application/json"}
        $uri = "$DceURI/dataCollectionRules/$DcrImmutableId/streams/$StreamName`?api-version=2021-11-01-preview"
        
        # Showing payload for troubleshooting purposes
        Write-Debug ($payload | ConvertFrom-Json | ConvertTo-Json)
        
        # Sending data to Data Collection Endpoint (DCE) -> Data Collection Rule (DCR) -> Azure Monitor table
        Invoke-RestMethod -Uri $uri -Method "Post" -Body (@($payload | ConvertFrom-Json | ConvertTo-Json)) -Headers $headers | Out-Null
    }

    # Maximum size of API call: 1MB for both compressed and uncompressed data
    $APILimitBytes = 1mb

    foreach ($dataset in $all_datasets){
        $total_file_size = (get-item -Path $dataset).Length
        $json_records = @()
        $json_array_current_size = 0
        $event_count = 0
        $total_size = 0
 
        # Create ReadLines Iterator and get total number of lines
        $readLineIterator = [System.IO.File]::ReadLines($dataset)
        $numberOfLines = [Linq.Enumerable]::Count($readLineIterator)

        write-Host "*******************************************"
        Write-Host "[+] Processing $dataset"
        Write-Host "[+] Dataset Size: $($total_file_size/1mb) MBs"
        Write-Host "[+] Number of events to process: $numberOfLines"
        
        # Read each JSON object from file
        foreach($line in $readLineIterator){
            # Increase event number
            $event_count += 1

            # Update progress bar with current event count
            if ($ShowProgressBar){ Write-Progress -Activity "Processing files" -status "Processing $dataset" -percentComplete ($event_count / $numberOfLines * 100) }

            write-debug "############ Event $event_count ###############"
            if ($TimestampField){
                $Timestamp = $line | Convertfrom-json | Select-Object -ExpandProperty $TimestampField
            }
            else {
                $Timestamp = Get-Date ([datetime]::UtcNow) -Format O
            }

            # Creating Dictionary for Log entry
            $log_entry = [ordered]@{
                Timestamp = $Timestamp
                RawEventData = $line
            }

            # Processing Log entry as a compressed JSON object
            $message = $log_entry | ConvertTo-Json -Compress
            Write-Debug "Processing log entry: $($message.Length) bytes"
            
            # Getting proposed and current JSON array size
            $json_array_current_size = ([System.Text.Encoding]::UTF8.GetBytes(@($json_records | Convertfrom-json | ConvertTo-Json))).Length
            $json_array_proposed_size = ([System.Text.Encoding]::UTF8.GetBytes(@(($json_records + $message) | Convertfrom-json | ConvertTo-Json))).Length
            Write-Debug "Current size of JSON array: $json_array_current_size bytes"

            if ($json_array_proposed_size -le $APILimitBytes){
                $json_records += $message
                $json_array_current_size = $json_array_proposed_size
                write-debug "New size of JSON array: $json_array_current_size bytes"
            }
            else {
                write-debug "Sending current JSON array before processing more log entries.."
                Send-DataToDCE -payload $json_records -size $json_array_current_size
                # Keeping track of how much data we are sending over
                $total_size += $json_array_current_size

                # There are more events to process..
                write-debug "######## Resetting JSON Array ########"
                $json_records = @($message)
                $json_array_current_size = ([System.Text.Encoding]::UTF8.GetBytes(@($json_records | Convertfrom-json | ConvertTo-Json))).Length
                Write-Debug "Starting JSON array with size: $json_array_current_size bytes"
            }
           
            if($event_count -eq $numberOfLines){
                write-debug "##### Last log entry in $dataset #######"
                Send-DataToDCE -payload $json_records -size $json_array_current_size
                # Keeping track of how much data we are sending over
                $total_size += $json_array_current_size
            }
        }
        Write-Host "[+] Finished processing dataset"
        Write-Host "[+] Number of events processed: $event_count"
        Write-Host "[+] Total data sent: $($total_size/1mb) MBs"
        write-Host "*******************************************"
    }
}