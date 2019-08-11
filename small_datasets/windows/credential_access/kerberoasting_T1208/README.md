# Kerberoasting

An adversary can use domain credentials captured on any user to request kerberos service tickets for accounts that are associated with the SPN records in Active Directory (AD). The service tickets are signed with the targeted user's NTLM hash, which can then be cracked offline. 

## Technique Variations Table

| Network | Dataset | Updated |
| ------- | --------- | ------- |
| shire | [empire_kerberoast](./empire_kerberoast.md) | 2019-07-14005430 |
