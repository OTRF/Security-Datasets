# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# References:
# https://docs.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-deploy-wps

$host_info = gwmi win32_computersystem
$hostname = ($host_info).Name
$domain_name = ($host_info).Domain
$host_fqdn = ([System.Net.DNS]::GetHostByName($env:ComputerName)).HostName
$net_adapter = (get-netadapter).Name

# Configure Static IP
write-host -fore green "Configuring static ip on $hostname to 10.0.10.3 .."
New-NetIPAddress -IPAddress 10.0.10.3 -InterfaceAlias $net_adapter -DefaultGateway 10.0.10.1 -AddressFamily IPv4 -PrefixLength 24

# Windows Features Installation
Get-Command -module ServerManager
write-host -fore green "Installing Windows features:"
write-host -fore yello "Installing DHCP Windows feature.."
Install-WindowsFeature -name "DHCP" -IncludeManagementTools

# DHCP Security Group
write-host -fore green "Creating DHCP security group.."
netsh dhcp add securitygroups
Restart-service dhcpserver

# Authorize the DHCP server in Active Directory
write-host -fore green "Authorizing DHCP server in AD.."
Add-DhcpServerInDC -DnsName $host_fqdn -IPAddress 10.0.0.3
Get-DhcpServerInDC

# Notify Server Manager that post-install DHCP configuration is complete
write-host -fore green "Notifying server manager that post-install DHCP config is complete.."
Set-ItemProperty –Path registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ServerManager\Roles\12 –Name ConfigurationState –Value 2

# Set up DHCP scope
write-host -fore green "Setting up DHCP scope.."
Add-DhcpServerv4Scope -name "Comarca" -StartRange 10.0.10.1 -EndRange 10.0.10.254 -SubnetMask 255.255.255.0 -State Active
Add-DhcpServerv4ExclusionRange -ScopeID 10.0.10.0 -StartRange 10.0.10.1 -EndRange 10.0.10.20
Set-DhcpServerv4OptionValue -OptionID 3 -Value 10.0.10.1 -ScopeID 10.0.10.0 -ComputerName $host_fqdn
Set-DhcpServerv4OptionValue -DnsDomain $domain_name -DnsServer 10.0.10.3