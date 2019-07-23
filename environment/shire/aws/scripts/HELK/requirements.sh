#!/bin/bash
apt-get purge python3-pip -y
apt-get purge python-pip -y
apt-get autoremove -y
apt-get purge python3.5 -y
apt-get purge python3 -y
apt-get -f install -y
apt-get install python3.5 -y
apt-get install python3-pip -y
pip3 install --upgrade pip
pip install pandas
pip install tabulate
