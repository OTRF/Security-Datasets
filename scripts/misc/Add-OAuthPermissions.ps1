function Add-OAuthPermissions {
    <#
    .SYNOPSIS
    A PowerShell wrapper around the Azure CLI and Microsoft Graph API to grant permissions to a service principal.
    
    Author: Roberto Rodriguez (@Cyb3rWard0g)
    License: MIT
    Required Dependencies: Azure CLI
    Optional Dependencies: None
    
    .DESCRIPTION
    Add-OAuthPermissions is a simple PowerShell wrapper around the Microsoft Graph API to grant permissions to a service principal. 

    .PARAMETER AppSvcPrincipalName
    Display name of the service principal backing up the Azure AD Application. It is usually the same name as the Azure AD application.

    .PARAMETER $SvcPrincipalId
    Service principal Id to use to add permissions directly. This helps to use service principals such as user assigned manage identities.

    .PARAMETER PermissionsArray
    Array of OAuth permissions.

    .PARAMETER PermissionsFile
    JSON file with permissions to grant to the service principal.

    .LINK
    https://docs.microsoft.com/en-us/graph/api/oauth2permissiongrant-post?view=graph-rest-1.0&tabs=http
    https://docs.microsoft.com/en-us/graph/api/serviceprincipal-post-approleassignments?view=graph-rest-1.0&tabs=http

    #>

    [cmdletbinding()]
    Param(
        [parameter(Mandatory = $false)]
        [String] $AppSvcPrincipalName,

        [parameter(Mandatory = $false)]
        [string] $SvcPrincipalId,

        [parameter(Mandatory = $False, ParameterSetName='Array')]
        [object] $PermissionsArray,

        [parameter(Mandatory = $False, ParameterSetName='File')]
        [string] $PermissionsFile
    )

    # Validate signed in user
    $signedInUser = az ad signed-in-user show --query '[displayName, mail]' | convertfrom-json
    if (!($signedInUser)){
        az login
    }
    else {
        Write-Host "[+] Using the following user context:"
        Write-Host "[+] UserName: $($SignedInUser[0])"
        Write-Host "[+] E-mail: $($SignedInUser[1])"
    }

    # Get Application service principal if service principal name is provided
    If ($AppSvcPrincipalName) {
        $SvcPrincipalId = az ad sp list --query "[?appDisplayName=='$($AppSvcPrincipalName)'].objectId" -o tsv --all
        if (!$SvcPrincipalId) {
            Write-Error "Error looking for Azure AD application service principal"
            return
        }
    }
    Write-Output "[+] Service principal ID: $SvcPrincipalId"

    # Process permissions fi;e
    if ( $PsCmdlet.ParameterSetName -eq "file") {
        Write-Output "[+] Reading permissions from file.."
        $PermissionsList = Get-Content $PermissionsFile | ConvertFrom-Json
    }

    # Process array
    if ( $PsCmdlet.ParameterSetName -eq "array") {
        Write-Output "[+] Reading permissions from array.."
        $PermissionsList = $PermissionsArray | ConvertTo-Json -Depth 10 | ConvertFrom-Json
    }
    
    Write-Output "[+] Processing permissions.."
    foreach ($PermissionObject in $PermissionsList) {
        $resource = $PermissionObject | get-member -MemberType NoteProperty | Select-Object -ExpandProperty Name
        Write-Output "[+] Resource: $resource"
        $roleSvcAppId = az ad sp list --query "[?appDisplayName=='$resource'].objectId" -o tsv --all
        if (!$roleSvcAppId) {
            Write-Error "Error looking for Service Principal to get roles from"
            return
        }
        Write-Output "[+] Found $resource service principal ID: $roleSvcAppId"

        # Process permissiontypes
        $permissionTypes = $PermissionObject."$resource" | get-member -MemberType NoteProperty | Select-Object -ExpandProperty Name

        Write-Output "[+] Processing permissions from $resource"
        foreach ($type in $permissionTypes) {
            $rolePropertyType = Switch ($type) {
                'Delegated' { 'oauth2Permissions'}
                'Application' { 'appRoles' }
            }

            Write-Output "[+] Getting $type Permissions from $resource"
            $permissions = az ad sp show --id $roleSvcAppId --query "$rolePropertyType" | ConvertFrom-Json

             # Get Role Assignments
            Write-Output "[+] Getting Role Assignments:"
            $roleAssignments = @()
            $RequiredPermissions = $PermissionObject."$resource"."$type"
            Foreach ($rp in $RequiredPermissions) {
                Write-Output "  [>>] $rp"
                $roleAssignment = $permissions | Where-Object { $_.Value -eq $rp}
                $roleAssignments += $roleAssignment
            }
            $roleAssignments

            # Getting Microsoft Graph token
            Write-Output "[+] Getting OAuth Microsoft Graph Token"
            $token=$(az account get-access-token --resource-type ms-graph --query accessToken --output tsv)
            $headers = @{
                "Authorization" = "Bearer $token"
                "Content-Type" = "application/json"
            }

            if ($type -eq 'Application') {
                # Process required permissions
                $resourceAccessObjects = @()
                Write-Output "[+] Creating Resource Access Object"
                foreach ($roleAssignment in $roleAssignments) {
                    $resourceAccessObjects += [PSCustomObject]@{
                        principalId = $SvcPrincipalId
                        resourceId = $roleSvcAppId
                        appRoleId = $roleAssignment.Id
                    }
                }
                write-verbose $($resourceAccessObjects | out-string)
            
                $Uri="https://graph.microsoft.com/v1.0/servicePrincipals/$SvcPrincipalId/appRoleAssignments"

                foreach ($role in $resourceAccessObjects) {
                    Write-Output "[+] Granting appRole to $SvcPrincipalId"
                    write-verbose $($role | ConvertTo-Json -Compress)
                    $params = @{ 
                        "Method" = "Post" 
                        "Uri" = $uri
                        "Body" = $role | ConvertTo-Json -Compress
                        "Headers" = $headers 
                    } 
                    $results = Invoke-WebRequest @params -usebasicparsing
                    if ($results.StatusCode -eq 201) {
                        Write-Host "Approle $role was assigned to application"
                    }

                    $results
                }
            }
            else {
                # Get PermissionGrants
                $params = @{
                    Method = "Get"
                    Uri = "https://graph.microsoft.com/v1.0/oauth2PermissionGrants"
                    Headers = $headers
                }
                
                $permissionGrants = (Invoke-RestMethod @params).Value
                $appPermissionsGrant = $permissionGrants | Where-Object {$_.ClientId -eq $SvcPrincipalId -and $_.resourceId -eq $roleSvcAppId}
                
                if ($appPermissionsGrant) {
                    Write-Output "[+] Found PermissionsGrant"
                    $permissionGrantId = $appPermissionsGrant.id

                    Write-Output "[+] Removing permission grant: $permissionGrantId"
                    $params = @{
                        Method = "Delete"
                        Uri = "https://graph.microsoft.com/v1.0/oauth2PermissionGrants/$permissionGrantId"
                        Headers = $headers
                    }
                    
                    $results = Invoke-WebRequest @params -usebasicparsing
                    if ($results.StatusCode -eq 204) {
                        Write-Output "OAuthPermissionsGrant was removed successfully!"
                    }
                }

                $body = @{
                    clientId = $SvcPrincipalId
                    consentType = "AllPrincipals"
                    principalId = $null
                    resourceId = $roleSvcAppId
                    scope = "$RequiredPermissions"
                } | ConvertTo-Json -compress

                $params = @{
                    Method = "Post"
                    Uri = 'https://graph.microsoft.com/v1.0/oauth2PermissionGrants'
                    Body = $body
                    Headers = $headers
                }
                Write-Output "[+] Granting OAuth permissions: $RequiredPermissions"
                Invoke-RestMethod @params
            }
        }
    }
}