# Azure Log Analytics

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
Invoke-Expression (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/OTRF/Security-Datasets/master/scripts/data-collectors/Export-ALAM365Events.ps1')
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
        "Log Analytics API" =  @{
            "Application" = @(
                "Data.Read"
            )
        }
    }
)
Add-OAuthPermissions -AppSvcPrincipalName $appSPN -PermissionsArray $parray -verbose
```

## Link Log Analytics Workspace
1. Navigate to your Azure portal, and select or search for Log Analytics.
2. Select your workspace from the list of available options, or search for it.
3. From the left menu that opens, select `Access Control (IAM)`. Click Add, and select `Log Analytics Reader` for the Role in the blade that appears. Search for your AAD App by name, and then click save.

## Get OAuth Access Token

```PowerShell
$appId = 'APPLICATION-ID'
$scope = 'https://api.loganalytics.io/.default'
$tenantId = 'TENANT-ID'

$token = Get-OAuthAccessToken -ClientId $appId -Scope $scope -TenantId $tenantId -GrantType client_credentials -AppSecret $secret -Verbose
```

## Query the Azure Log Analytics Workspace

### Inline Query

```PowerShell
$workspaceId = 'WORKSPACE-ID'

Export-ALAEvents -AccessToken $token -WorkspaceId $workspaceId -Query 'AuditLogs | limit 10' -verbose
```

### Multi-line Query

```PowerShell
$workspaceId = 'WORKSPACE-ID'

$query = @"
AuditLogs
  | where Category =~ "ApplicationManagement"
  | where ActivityDisplayName has_any ("Update application")
  | where Result =~ "success"
  | where tostring(InitiatedBy.user.userPrincipalName) has "@" or tostring(InitiatedBy.app.displayName) has "@"
  | extend UserAgent = tostring(AdditionalDetails[0].value)
  | extend InitiatingUser = tostring(parse_json(tostring(InitiatedBy.user)).userPrincipalName)
  | extend InitiatingIpAddress = tostring(parse_json(tostring(InitiatedBy.user)).ipAddress)
  | extend ModifiedApplication = tostring(TargetResources[0].displayName)
  | extend ModifiedApplicationObjectId = tostring(TargetResources[0].id)
  | extend ModifiedProperties = parse_json(tostring(TargetResources[0].modifiedProperties))
  | extend ModifiedPropertyName = tostring(ModifiedProperties[0].displayName)
  | extend ResourceAppId = parse_json(tostring(ModifiedProperties[0].newValue))[0].ResourceAppId
  | where ModifiedPropertyName =~ "RequiredResourceAccess"
  | extend Type = tostring(TargetResources[0].type)
  | project-away ModifiedProperties
  | project-reorder TimeGenerated, OperationName, InitiatingUser, InitiatingIpAddress, UserAgent, ModifiedApplication, ModifiedApplicationObjectId, CorrelationId, TenantId
  | extend timestamp = TimeGenerated, AccountCustomEntity = InitiatingUser, IPCustomEntity = InitiatingIpAddress
"@
Export-ALAEvents -AccessToken $token -WorkspaceId $workspaceId -Query $query -verbose
```