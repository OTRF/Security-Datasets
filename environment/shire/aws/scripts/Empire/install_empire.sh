#Created by Jonathan Johnson


#!/bin/bash

#Checking to see if user is running as root
if [[ $EUID -ne 0 ]]; then
   echo "You need to be root to run this script."
   exit 1
fi
cd /opt/Empire/setup
sudo pip install -r requirements.txt
sudo ./install.sh << EOF

EOF
echo "Installation complete"
