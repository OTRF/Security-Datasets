# Persistence via WMI Subscriptions

Windows Management Instrumentation (WMI) can be used to install event filters, providers, consumers, and bindings that execute code when a defined event occurs. Adversaries may use the capabilities of WMI to subscribe to an event and execute arbitrary code when that event occurs, providing persistence on a system.

## Technique Variations Table

| Network | Dataset | Updated |
| ------- | --------- | ------- |
| shire | [empire_elevated_wmi](./empire_elevated_wmi.md) | 2019-05-18184306 |