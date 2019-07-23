#!/bin/bash
sudo apt-get -f install -y
apt-get purge python3-pip -y
apt-get purge python3.5 -y
apt-get install python3.5 -y
apt-get install python3-pip -y
pip install --upgrade pip 
pip3 install pandas
pip3 install tabulate
