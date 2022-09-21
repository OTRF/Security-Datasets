# Windows

You can create your own Windows security datasets by running a PowerShell script available in our scripts folder!
A script that leverages the System.Diagnostics.Eventing.Reader.EventLogSession class to collect event logs locally and remotely 

## Requirements

* [PowerShell v5](https://www.microsoft.com/en-us/download/details.aspx?id=54616)

## Import Export-WinEvents Script

You can import the script directly from GitHub with the following command

```Powershell
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/OTRF/Security-Datasets/master/scripts/data-collectors/Export-WinEvents.ps1')
```

## Clear Windows Events (Optional)

If you are working on a lab environment, you can first clear specific Windows event logs before run a simulation

```Powershell
@('Security','Microsoft-Windows-Sysmon/Operational') | Clear-WinEvents
```

## Collect Windows Event Logs

Before running any simulations, I recommend to save the current time to a variable in order to filter the event logs after the simulation.

```Powershell
$FromDate = get-date
```

Now you are ready to run a simulation! Run it!

After running a simulation on your Windows endpoint, you can select specific event logs you want to collect data from

```Powershell
@('Security','Microsoft-Windows-Sysmon/Operational') | Export-WinEvents -EndDate $FromDate -OutputFolder C:\ProgramData\ -Verbose

```

You can also try to collect every single event from every event log available in your system that was created right after you set the `$FromDate` variable (Most likley events related to your simulation)

```Powershell
$FilterLogs = @('Microsoft-Windows-UniversalTelemetryClient/Operational','Microsoft-Windows-Store/Operational','Microsoft-Windows-PushNotification-Platform/Operational','Microsoft-Client-Licensing-Platform/Admin','Microsoft-Windows-AppID/Operational','Microsoft-Windows-AppXDeployment/Operational','Microsoft-WindowsAzure-Diagnostics/Heartbeat','Microsoft-WindowsAzure-Diagnostics/GuestAgent','Microsoft-Windows-SystemDataArchiver/Diagnostic','Microsoft-Windows-DSC/Operational','Windows PowerShell','Microsoft-Windows-Kernel-IO/Operational','Microsoft-Windows-PowerShell/Operational')

Get-WinEvent -ListLog * | Where-Object {$_.LogName -notin $FilterLogs} |Where-Object {$_.RecordCount -gt 0} | Select-Object -ExpandProperty LogName | Export-WinEvents -EndDate $FromDate -OutputFolder C:\ProgramData\ -ErrorAction SilentlyContinue
```

That's it! Now, what I would highly recommend is to explore your events and validate the creation of events related to the adversary behavior through your own research. Once you are confident the dataset contains the events related to the adversary behavior, open a PR to the project and we would be happy to review the dataset and add it to our library!
