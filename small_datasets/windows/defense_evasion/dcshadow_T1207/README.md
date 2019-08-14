# DCShadow

Advesaries might attempt to modify or maninpulate Active Directory(AD) data, this can be object and schema changes inside of the AD Infrastructure. 

Example: An advesary has Domain Admin (DA) credentials and wants to avoid being caught in an environment, the advesary can push a user into the Domain Administrators group, then use that user account to move around in the environment/modify other objects and attributes in the AD infrastructure. 

## Technique Variations Table

| Sub-techinque | Author | Updated |
| ----------- | ------- | --------- | 
| [dcshadow](mimikatz_dcshadow.md) | Jonathan Johnson [@jsecurity101](https://twitter.com/jsecurity101) | 2019-08-11202357 |