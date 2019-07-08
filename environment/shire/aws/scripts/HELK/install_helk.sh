#Created by Jonathan Johnson
#Only supports Ubuntu 16.04

#!/bin/bash

#Checking to see if user is running as root
if [[ $EUID -ne 0 ]]; then
   echo "You need to be root to run this script."
   exit 1
fi

cd /opt/HELK/docker

./helk_install.sh << EOF
3



hunting
EOF