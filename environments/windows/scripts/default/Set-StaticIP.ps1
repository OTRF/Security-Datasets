# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:
# https://aws.amazon.com/blogs/compute/optimizing-joining-windows-server-instances-to-a-domain-with-powershell-in-aws-cloudformation/

[CmdletBinding()]
param (
    [Parameter(Mandatory=$false)]
    [string]$ServerAddresses
)

$netip = Get-NetIPConfiguration
$ipconfig = Get-NetIPAddress | ?{$_.IpAddress -eq $netip.IPv4Address.IpAddress}
Get-NetAdapter | Set-NetIPInterface -DHCP Disabled
Get-NetAdapter | New-NetIPAddress -AddressFamily IPv4 -IPAddress $netip.IPv4Address.IpAddress -PrefixLength $ipconfig.PrefixLength -DefaultGateway $netip.IPv4DefaultGateway.NextHop
if($ServerAddresses)
{
    Get-NetAdapter | Set-DnsClientServerAddress -ServerAddresses $ServerAddresses

}
else{
    Get-NetAdapter | Set-DnsClientServerAddress -ServerAddresses $netip.DNSServer.ServerAddresses
}