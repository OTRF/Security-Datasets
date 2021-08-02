function New-AppRegistration {
    <#
    .SYNOPSIS
    A PowerShell wrapper around the Azure CLI to create/register a new Azure AD application and its respective service principal.
    
    Author: Roberto Rodriguez (@Cyb3rWard0g)
    License: MIT
    Required Dependencies: Azure CLI
    Optional Dependencies: None
    
    .DESCRIPTION
    New-AppRegistration is a simple PowerShell wrapper around the Azure CLI to create/register a new Azure AD application and its respective service principal.

    .PARAMETER Name
    The name of the new Azure AD Application and service principal.

    .PARAMETER NativeApp
    Switch to register an application which can be installed on a user's device or computer.

    .PARAMETER IdentifierUris
    Space-separated unique URIs that Azure AD can use for this app.

    .PARAMETER ReplyUrls
    Space-separated URIs to which Azure AD will redirect in response to an OAuth 2.0 request. The value does not need to be a physical endpoint, but must be a valid URI.

    .PARAMETER AddSecret
    Switch to create add credentials to the application.

    .PARAMETER DisableImplicitGrantFlowOAuth2
    Switch to update the application by specifying the property oauth2AllowIdTokenImplicitFlow and value false.

    .PARAMETER UseV2AccessTokens
    Switch to set application to use V2 access tokens.

    .PARAMETER RequireAssignedRole
    Switch to require assigned role to use the application. This restricts who can access your application. Only users that have the role assigned.

    .PARAMETER AssignAppRoleToUser
    Use thisparameter to assign an app role to a service principal. Example: wardog@domain.onmicrosoft.com.

    .LINK
    https://docs.microsoft.com/en-us/cli/azure/ad/app?view=azure-cli-latest#az_ad_app_create
    https://github.com/Azure/SimuLand/blob/main/2_deploy/_helper_docs/registerAADAppAndSP.md
    #>

    [cmdletbinding()]
    Param(
        [parameter(Mandatory = $True)]
        [String] $Name,

        [Parameter(Mandatory=$false)]
        [switch] $NativeApp,

        [Parameter(Mandatory=$false)]
        [string] $IdentifierUris,

        [Parameter(Mandatory=$false)]
        [string] $ReplyUrls,

        [Parameter(Mandatory=$false)]
        [switch] $AddSecret,

        [Parameter(Mandatory=$false)]
        [switch] $DisableImplicitGrantFlowOAuth2,

        [Parameter(Mandatory=$false)]
        [switch] $UseV2AccessTokens,

        [Parameter(Mandatory=$false)]
        [switch] $RequireAssignedRole,

        [Parameter(Mandatory=$false)]
        [string] $AssignAppRoleToUser
    )

    # Validate signed in user
    $signedInUser = az ad signed-in-user show --query '[displayName, mail]' | convertfrom-json
    if (!($signedInUser)) {
        az login
    }
    else {
        Write-Host "[+] Using the following user context:"
        Write-Host "[+] UserName: $($SignedInUser[0])"
        Write-Host "[+] E-mail: $($SignedInUser[1])"
    }

    # Registering a new Azure AD Application
    $registeredApp = $(az ad app list --query "[?displayName=='$Name']" --all | ConvertFrom-Json)[0]
    if ($registeredApp){
        Write-Host "[!] Azure AD application $Name already exists!"
    }
    else {
        Write-Host "[+] Registering new Azure AD application: $Name"
        if ($NativeApp) {
            $registeredApp = $(az ad app create --display-name $Name --native-app | ConvertFrom-Json)
        }
        else {
            $registeredApp = $(az ad app create --display-name $Name | ConvertFrom-Json)
        }

        # Sleep
        Start-Sleep -s 15
    }

    if ($IdentifierUris) {
        Write-Host "[+] Updating $Name application: Adding unique identifier URIs that Azure AD can use for this app"
        az ad app update --id $registeredApp.AppId --identifier-uris $IdentifierUris | Out-Null
    }
    if ($ReplyUrls) {
        Write-Host "[+] Updating $Name application: Adding URIs to which Azure AD will redirect in response to an OAuth 2.0 request"
        az ad app update --id $registeredApp.AppId --reply-urls $ReplyUrls | Out-Null
    }

    # Creating the new Azure AD application service principal
    $spExists = $(az ad sp list --query "[?appDisplayName=='$Name']" --all  | ConvertFrom-Json)[0]
    if ($spExists){
        Write-Host "[!] Azure AD application $Name already has a service principal"
    }
    else {
        Write-Host "[+] Creating Azure AD service principal for $Name application"
        az ad sp create --id $registeredApp.appId

        # Sleep
        Start-Sleep -s 15
    }

    #Add credentials to application
    if ($AddSecret) {
        Write-Host "[+] Getting MS Graph access token with current security context"
        $token=$(az account get-access-token --resource-type ms-graph --query accessToken --output tsv)
        write-verbose "Using the following MS Graph token: $token"
        $headers = @{
            "Authorization" = "Bearer $token"
            "Content-Type" = "application/json"
        }
        $pwdCredentialName = 'CloudKatanaSecret'
        $body = @{
            passwordCredential = @{ displayName = "$($pwdCredentialName)" }
        } | ConvertTo-Json -Compress
        $params = @{
            "Method"  = "Post"
            "Uri"     = "https://graph.microsoft.com/v1.0/applications/$($registeredApp.objectId)/addPassword"
            "Body"    = $body
            "Headers" = $headers
        }
        Write-Host "[+] Adding credentials to $Name application"
        $credentials = Invoke-RestMethod @params
        if (!($credentials)){
            Write-Error "Error adding credentials to $Name"
            return
        }
        
        Write-Host "[+] Extracting secret text from results. Save it for future operations"
        $secret = $credentials.secretText
    }

    if ($DisableImplicitGrantFlowOAuth2){
        Write-Host "[+] Updating $Name application: Disabling implicit grant flow for OAuth2"
        az ad app update --id $registeredApp.AppId --set oauth2AllowIdTokenImplicitFlow=false *>&1 | Out-Null
    }

    if ($UseV2AccessTokens){
        # Set application to use V2 access tokens
        $Body = @{
            api = @{
                requestedAccessTokenVersion = 2
            }
        } | ConvertTo-Json -Compress | ConvertTo-Json
        # Pipe to ConvertTo-Json twice to escape all quotes, or az cli will remove them when parsing
        Write-Host "[+] Updating $Name application: Setting application to use V2 access tokens"
        az rest --method PATCH --uri "https://graph.microsoft.com/v1.0/applications/$($registeredApp.objectId)" --body $Body --headers "Content-Type=application/json"
    }

    if($RequireAssignedRole){
        Write-Host "[+] Updating $Name application: Setting application to require users being assigned a role "
        az ad sp update --id $registeredApp.AppId --set appRoleAssignmentRequired=true | Out-Null
        # Sleep
        Start-Sleep -s 10
    }

    if($AssignAppRoleToUser){
        Write-Host "[+] Granting app role assignment to $AssignAppRoleToUser "
        $AppSp = az ad sp show --id $registeredApp.AppId | ConvertFrom-Json
        $principalId = az ad user show --id $AssignAppRoleToUser --query 'objectId' -o tsv

        $Body = @{
            appRoleId = [Guid]::Empty.Guid
            principalId = $principalId
            resourceId = $AppSp.objectId
        } | ConvertTo-Json -Compress | ConvertTo-Json

        $AssignAppRoleResult = az rest --method post --uri "https://graph.microsoft.com/v1.0/users/$AssignAppRoleToUser/appRoleAssignments" --body $Body --headers "Content-Type=application/json"
        if (!$AssignAppRoleResult) {
            Write-Error "Error granting app role assignment to user $AssignAppRoleToUser"
            return
        }
    }

    # Output the Application for use later
    Write-Host "[+] Application: $Name"
    $registeredApp
    Write-Host "[+] Application ID: $($registeredApp.AppId)"

    if ($AddSecret){
        Write-Host "[+] New Client Secret: $pwdCredentialName "
        $credentials
        Write-Host "[+] Secret Text: "
        $secret
    }
}