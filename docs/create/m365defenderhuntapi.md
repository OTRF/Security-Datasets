# Microsoft 365 Defender

## Requirements

* [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
    * For Windows, you can use the following commands:

    ```PowerShell
    Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi
    Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'
    rm .\AzureCLI.msi
    ```

## Authenticate to Azure

Use the Azure CLI command `az login` to authenticate to Azure AD with an account to deploy resources in Azure.

```PowerShell
az login
```

## Import PowerShell Modules

```PowerShell
Invoke-Expression (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/OTRF/Security-Datasets/master/scripts/misc/New-AppRegistration.ps1')
Invoke-Expression (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/OTRF/Security-Datasets/master/scripts/data-collectors/Export-ALAM365DEvents.ps1')
```

## Register Azure AD Application

Register a new application and save the `client_id` (Application Id) and the secret value.

```PowerShell
New-AppRegistration -Name 'EventLogReader' -AddSecret
```

## Grant AppRole Permissions to Applications

```PowerShell
$appSPN = 'EventLogReader'
$parray = @(
    @{
        "Microsoft Threat Protection" =  @{
            "Application" = @(
                "AdvancedHunting.Read.All",
                "Incident.Read.All"
            )
        }
    }
)
Add-OAuthPermissions -AppSvcPrincipalName $appSPN -PermissionsArray $parray -verbose
```

## Get OAuth Access Token

```PowerShell
$appId = 'APPLICATION-ID'
$scope = 'https://api.security.microsoft.com/.default'
$tenantId = 'TENANT-ID'

$token = Get-OAuthAccessToken -ClientId $appId -Scope $scope -TenantId $tenantId -GrantType client_credentials -AppSecret $secret -Verbose
```

## Query Data from Microsoft 365 Defender

### Inline Query

```PowerShell
Export-M365DEvents -AccessToken $token -Query 'DeviceEvents | where DeviceName contains "adfs01" | limit 1' -verbose
```

```PowerShell
Export-M365DEvents -AccessToken $token -Query 'IdentityDirectoryEvents | where ActionType contains "replication" | limit 10' -verbose
```

### Multi-line Query

```PowerShell
$query = @"
CloudAppEvents
| where ActionType == "Add delegated permission grant."
| limit 10
| extend RawEventData = parse_json(RawEventData)
| where RawEventData.ResultStatus =~ "success"
| extend UserId = tostring(RawEventData.UserId)
| extend UserAgent = parse_json(replace('-','',tostring(RawEventData.ExtendedPRoperties[0].Value))).UserAgent
| extend properties = RawEventData.ModifiedProperties
| mvexpand properties
| extend Permissions = properties.NewValue
| where Permissions has_any ("Mail.Read", "Mail.ReadWrite")
| extend PermissionsAddedTo = tostring(RawEventData.Target[3].ID) // Get target of permissions
| project-away properties, RawEventData
"@
Export-M365DEvents -AccessToken $token -Query $query -verbose
```

### Query From File

```PowerShell
$query = [IO.File]::ReadAllText("C:\myQuery.txt")
Export-M365DEvents -AccessToken $token -Query $query -verbose
```