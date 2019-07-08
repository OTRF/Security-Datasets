#Jonathan Johnson
#github:https://github.com/jsecurity101

Write-Output "
 _____                           _          _     _____ ___________ 
|_   _|                         | |        | |   |  _  |_   _| ___ \
  | | _ __ ___  _ __   ___  _ __| |_ ______| |   | | | | | | | |_/ /
  | || '_ ` _ \| '_ \ / _ \| '__| __|______| |   | | | | | | |    / 
 _| || | | | | | |_) | (_) | |  | |_       | |___\ \_/ / | | | |\ \ 
 \___/_| |_| |_| .__/ \___/|_|   \__|      \_____/\___/  \_/ \_| \_|
               | |                                                  
               |_|                                                                                               
"  

Function Import-LOTR()


{

Import-Module activedirectory
  
#Update the path to where the .csv file is stored. 

$ADUsers = Import-csv C:\mordor\environment\shire\scripts\DC\shire_users.csv

foreach ($User in $ADUsers)

{
    #Read in data from .csv and assign it to the variable. This is done to import attributes in the New-ADUser.
        
    $username     = $User.username
    $password     = $User.password
    $firstname     = $User.firstname
    $lastname     = $User.lastname
    $ou         = $User.ou 
    $identity   = $User.identity
    $password = $User.Password


    #Runs check against AD to verify User doesn't already exist inside of Active Directory

    if (Get-ADUser -F {SamAccountName -eq $Username })
    {
         Write-Warning "$Username already exists."
    }


#If User doesn't exist, New-ADUser will add $Username to AD based on the objects specified specified in the .csv file. 

    else


    {
        #Update to UserPrincipalName to match personal domain. Ex: If domain is: example.com. Should read as - $Username@example.com
        
        New-ADUser `
            -SamAccountName $Username `
            -UserPrincipalName "$Username@shire.com" `
            -Name "$firstname $lastname" `
            -GivenName $firstname `
            -Surname $lastname `
            -Enabled $True `
            -DisplayName "$firstname $lastname" `
            -Path $ou `
            -AccountPassword (convertto-securestring $password -AsPlainText -Force) -PasswordNeverExpires $True
            

        Add-ADGroupMember `
            -Identity $identity `
            -Members $Username `
        }
        Write-Output "$username has been added to the $identity group"
    }
setspn -a glamdring/shire.com shire\gandolf
}
Import-LOTR
