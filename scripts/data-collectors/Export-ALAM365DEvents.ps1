function Export-ALAEvents {
    <#
    .SYNOPSIS

    Export-ALAEvents exports security events to the console or as JSON files from a Log Analytics Workspace backing up an Azure Sentinel instance.

    Author: Robert Rodriguez (@Cyb3rWard0g)
    License: MIT
    Required Dependencies: None
    Optional Dependencies: None

    .DESCRIPTION

    Export-ALAEvents is a simple PowerShell wrapper for the Log Analytics API to export security events
    and alerts as JSON files to share the telemetry generated after simulating adversary techniques.

    .PARAMETER AccessToken

    OAuth access token to access the https://api.loganalytics.io API.

    .PARAMETER Query

    The KQL query to run and filter data to export.

    .PARAMETER WorkspaceId

    ID of the workspace. This is Workspace ID from the Properties blade in the Azure portal.

    .PARAMETER OutputPath

    The path or name of the file to export events to.

    .LINK

    https://dev.loganalytics.io/
    https://docs.microsoft.com/en-us/rest/api/loganalytics/dataaccess/query/get
    #>

    [CmdletBinding()]
    Param (
        [Parameter(Mandatory=$true)]
        [String] $AccessToken,

        [Parameter(Mandatory=$true)]
        [String] $WorkspaceId,

        [Parameter(Mandatory=$true)]
        [String] $Query,

        [Parameter(Mandatory=$false)]
        [String] $Timespan,

        [Parameter(Mandatory=$false)]
        [String] $OutputPath
    )

    BEGIN {
        # Set Current Directory (PS Session Only)
        [Environment]::CurrentDirectory=(Get-Location -PSProvider FileSystem).ProviderPath

        # Set API URL
        #$resource = 'https://api.loganalytics.io'
        #$apiUri = "$resource/v1/workspaces/$WorkspaceId/query"
        $apiUri = "https://api.loganalytics.io/v1/workspaces/$WorkspaceId/query"
        $queryProperty = "query"

    }
    PROCESS {
        Write-Host "[+] Setting HTTP Request.."
        # HTTP Body
        $Querybody = @{
            $queryProperty = $Query
        }

        if ($Timespan) {
            $Querybody['timespan'] = "PT$($Timespan.ToUpper())"
        }

        # HTTP Headers
        $HttpHeaders = @{
            "Content-Type" = "application/json"
            "Authorization" = "Bearer $AccessToken"
        }
        
        # HTTP Params
        $HTTPParams = @{
            Method = 'Post'
            Uri = $apiUri
            Body = $($QueryBody | ConvertTo-Json -Compress)
            Headers = $HttpHeaders
        }

        # Send HTTP Request
        Write-Host "[+] Sending HTTP Request.."
        $QueryResponse = $(Invoke-RestMethod @HTTPParams)
        $EventsCount = $QueryResponse.tables[0].rows.Length
        if ($EventsCount -eq 0) {
            Write-Warning "[!] No events found"
            Exit
        }
        else {
            Write-Host "[+] Found $EventsCount events"
        }

        Write-Host "[+] Processing response.."
        $AllEvents = @()
        $headerRow = $null
        $headerRow = $QueryResponse.tables.columns | Select-Object name
        $columnsCount = $headerRow.Count

        foreach ($row in $QueryResponse.tables[0].rows) {
            $data = new-object PSObject
            for ($i = 0; $i -lt $columnsCount; $i++) {
                if ($row[$i]) {
                    $data | add-member -membertype NoteProperty -name $headerRow[$i].name -value $row[$i]
                }
            }
            $AllEvents += $data
            $data = $null
        }
    }
    END {
        if ($OutputPath)
        {
            Write-Host "[+] Exporting all events to $OutputPath"
            $utf8NoBom = New-Object System.Text.UTF8Encoding $false
            $AllEvents | ForEach-Object {
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
        else {
            write-Host "[+] Returning all events"
            return $AllEvents
        }
    }
}

function Export-M365DEvents {
    <#
    .SYNOPSIS

    Export-M365DEvents exports security events to the console or as JSON files from the Microsoft 365 Defender Advanced Hunting platform.

    Author: Robert Rodriguez (@Cyb3rWard0g)
    License: MIT
    Required Dependencies: None
    Optional Dependencies: None

    .DESCRIPTION

    Export-M365DEvents is a simple PowerShell wrapper for the Microsoft 365 Defender Advanced Hunting API to export security events
    and alerts as JSON files to share the telemetry generated after simulating adversary techniques.

    .PARAMETER AccessToken

    OAuth access token to access the https://api.security.microsoft.com API.

    .PARAMETER Query

    The KQL query to run and filter data to export.

    .PARAMETER OutputPath

    The path or name of the file to export events to.

    .LINK

    https://docs.microsoft.com/en-us/microsoft-365/security/defender/api-advanced-hunting?view=o365-worldwide
    https://docs.microsoft.com/en-us/microsoft-365/security/defender/advanced-hunting-overview?view=o365-worldwide
    https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/exposed-apis-create-app-webapp?view=o365-worldwide
    https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/run-advanced-query-api?view=o365-worldwide
    https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/apis-intro?view=o365-worldwide
    #>

    [CmdletBinding()]
    Param (
        [Parameter(Mandatory=$true)]
        [String] $AccessToken,

        [Parameter(Mandatory=$true)]
        [String] $Query,

        [Parameter(Mandatory=$false)]
        [String] $OutputPath
    )

    BEGIN {
        # Set Current Directory (PS Session Only)
        [Environment]::CurrentDirectory=(Get-Location -PSProvider FileSystem).ProviderPath

        # Set API URL
        Write-Host "[+] Setting API variables.."
        #$resource = "https://api.securitycenter.microsoft.com"
        #$apiUri = "$resource/api/advancedqueries/run"
        $apiUri = "https://api.security.microsoft.com/api/advancedhunting/run"
        $queryProperty = "Query"
    }
    PROCESS {
        Write-Host "[+] Setting HTTP Request.."
        # HTTP Body
        $Querybody = @{
            $queryProperty = $Query 
        }

        # HTTP Headers
        $HttpHeaders = @{
            'Content-Type' = 'application/json'
            Authorization = "Bearer $AccessToken"
        }

        # HTTP Params
        $HTTPParams = @{
            Method = 'Post'
            Uri = $apiUri
            Body = $($QueryBody | ConvertTo-Json -Compress)
            Headers = $HttpHeaders
        }

        # Send HTTP Request
        Write-Host "[+] Sending HTTP Request.."
        $QueryResponse = $(Invoke-RestMethod @HTTPParams)
        $AllEvents = @()
        $AllEvents += $QueryResponse.Results

        if (!$AllEvents){
            Write-Warning "[!] No events found"
            Exit
        }
        else {
            Write-Host "[+] Found $($AllEvents.Length) events"
        }
    }
    END {
        if ($OutputPath)
        {
            Write-Host "[+] Exporting all events to $OutputPath"
            $utf8NoBom = New-Object System.Text.UTF8Encoding $false
            $AllEvents | ForEach-Object {
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
        else {
            write-verbose "[+] Returning all events"
            return $AllEvents
        }
    }
}

function Get-OAuthAccessToken {
    <#
    .SYNOPSIS
    A PowerShell script to get an OAuth access token with a specific grant type and OAuth application.
    
    Author: Roberto Rodriguez (@Cyb3rWard0g)
    License: MIT
    Required Dependencies: None
    Optional Dependencies: None

    .DESCRIPTION
    Get-OAuthAccessToken is a simple PowerShell wrapper to obtain an OAuth access token. 

    .PARAMETER ClientId
    The Application (client) ID assigned to the Azure AD application.

    .PARAMETER Scope
    A space-separated list of scopes that you want the user to consent to. For the /authorize leg of the request, this can cover multiple resources, allowing your app to get consent for multiple web APIs you want to call.

    .PARAMETER TenantId
    Tenant ID. Can be /common, /consumers, or /organizations. It can also be the directory tenant that you want to request permission from in GUID or friendly name format.

    .PARAMETER GrantType
    The type of token request.

    .PARAMETER Username
    Username used for Password grant type.

    .PARAMETER Password
    Password used for Password grant type.

    .PARAMETER SamlToken
    SAML token used for SAML token grant type.

    .PARAMETER DeviceCode
    The device_code returned in the device authorization request.

    .PARAMETER AppSecret
    if the application requires a client secret, then use this parameter.

    .LINK
    https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-overview

    #>

    [cmdletbinding()]
    Param(
        [Parameter(Mandatory = $true)]
        [String] $ClientId,

        [Parameter(Mandatory = $false)]
        [String] $Scope = 'https://graph.microsoft.com/.default',

        [Parameter(Mandatory = $false)]
        [string] $TenantId,

        [Parameter(Mandatory=$true)]
        [ValidateSet("client_credentials","password","saml_token", "device_code")]
        [string] $GrantType,

        [Parameter(Mandatory=$false)]
        [AllowEmptyString()]
        [string] $AppSecret
    )
    DynamicParam {
        if ($GrantType) {
            # Adding Dynamic parameters
            if ($GrantType -eq 'password') {
                $ParamOptions = @(
                    @{
                    'Name' = 'Username';
                    'Mandatory' = $true
                    },
                    @{
                    'Name' = 'Password';
                    'Mandatory' = $true
                    }
                )
            }
            elseif ($GrantType -eq 'saml_token') {
                $ParamOptions = @(
                    @{
                    'Name' = 'SamlToken';
                    'Mandatory' = $true
                    }
                )  
            }
            elseif ($GrantType -eq 'device_code') {
                $ParamOptions = @(
                    @{
                    'Name' = 'DeviceCode';
                    'Mandatory' = $true
                    }
                )  
            }

            # Adding Dynamic parameter
            $RuntimeParamDic = New-Object System.Management.Automation.RuntimeDefinedParameterDictionary
            foreach ($Param in $ParamOptions) {
                $RuntimeParam = New-DynamicParam @Param
                $RuntimeParamDic.Add($Param.Name, $RuntimeParam)
            }
            return $RuntimeParamDic
        }
    }
    begin {
        # Force TLS 1.2
        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

        # Process Tenant ID
        if (!$TenantId) {
            $TenantId = 'organizations'
        }

        # Process Dynamic parameters
        $PsBoundParameters.GetEnumerator() | ForEach-Object { New-Variable -Name $_.Key -Value $_.Value -ea 'SilentlyContinue'}
    }
    process {
        # Initialize Headers dictionary
        $headers = @{
            'Content-Type' = 'application/x-www-form-urlencoded'
        }

        if ($GrantType -eq 'client_credentials') {
            $body = @{
                client_id = $ClientId
                scope = $Scope
                grant_type = 'client_credentials'
            }
        }
        elseif ($GrantType -eq 'password') {
            $body = @{
                client_id = $ClientId
                scope = $Scope
                username = $Username
                password = $Password
                grant_type = 'password'
            }
        }
        elseif ($GrantType -eq 'saml_token') {
            $encodedSamlToken= [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($SamlToken))
            $body = @{
                client_id = $ClientId
                scope = $Scope
                assertion = $encodedSamlToken
                grant_type = 'urn:ietf:params:oauth:grant-type:saml1_1-bearer'
            }
        }
        elseif ($GrantType -eq 'device_code') {
            $body = @{
                client_id = $ClientId
                grant_type = 'urn:ietf:params:oauth:grant-type:device_code'
                code = $DeviceCode
            }
        }
        if (![string]::IsNullOrEmpty($AppSecret))
        {
            $body.Add('client_secret', $AppSecret)
        }
        write-verbose $body

        $Params = @{
            Headers = $headers
            uri     = "https://login.microsoftonline.com/$TenantId/oauth2/v2.0/token"
            Body    = $body
            method  = 'Post'
        }
        $request  = Invoke-RestMethod @Params
    
        # Process authentication request
        if($null -eq $request) {
            throw "Token never received from AAD"
        }
        else {
            $request.access_token
        }
    }
}

function New-DynamicParam {
    [CmdletBinding()]
    [OutputType('System.Management.Automation.RuntimeDefinedParameter')]
    param (
        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$Name,
        [Parameter(Mandatory=$false)]
        [array]$ValidateSetOptions,
        [Parameter()]
        [switch]$Mandatory = $false,
        [Parameter()]
        [switch]$ValueFromPipeline = $false,
        [Parameter()]
        [switch]$ValueFromPipelineByPropertyName = $false
    )

    $Attrib = New-Object System.Management.Automation.ParameterAttribute
    $Attrib.Mandatory = $Mandatory.IsPresent
    $Attrib.ValueFromPipeline = $ValueFromPipeline.IsPresent
    $Attrib.ValueFromPipelineByPropertyName = $ValueFromPipelineByPropertyName.IsPresent

    # Create AttributeCollection object for the attribute
    $Collection = new-object System.Collections.ObjectModel.Collection[System.Attribute]
    # Add our custom attribute
    $Collection.Add($Attrib)
    # Add Validate Set
    if ($ValidateSetOptions)
    {
        $ValidateSet= new-object System.Management.Automation.ValidateSetAttribute($Param.ValidateSetOptions)
        $Collection.Add($ValidateSet)
    }

    # Create Runtime Parameter
    $DynParam = New-Object System.Management.Automation.RuntimeDefinedParameter($Param.Name, [string], $Collection)
    $DynParam
}