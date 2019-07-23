#!/bin/bash
sudo apt-get -f install -y
apt-get purge python3-pip -y
apt-get autoremove -y
apt-get purge python3.5 -y
apt-get install python3.5 -y
apt-get install python-pip -y
pip install --upgrade pip 
pip install pandas
pip install tabulate
