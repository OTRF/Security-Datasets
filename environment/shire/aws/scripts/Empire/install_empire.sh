#Created by Jonathan Johnson


#!/bin/bash

#Checking to see if user is running as root
if [[ $EUID -ne 0 ]]; then
   echo "You need to be root to run this script."
   exit 1
fi
pip install urllib3
pip install requests
pip install setuptools
pip install iptools
pip install pydispatcher
pip install flask
pip install macholib
pip install dropbox
pip install pyOpenSSL
pip install pyinstaller
pip install zlib_wrapper
pip install netifaces
pip install M2Crypto
pip install jinja2
pip install cryptography
pip install pyminifier
pip install xlutils
pip install pycrypto 

cd /opt/Empire/setup

sudo ./install.sh << EOF

EOF

echo "Installation complete"