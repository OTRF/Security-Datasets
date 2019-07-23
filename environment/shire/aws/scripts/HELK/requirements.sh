#!/bin/bash

apt-get purge python3.5 -y
apt-get purge python3 -y
apt-get install python3 -y
apt-get install python3.5 -y
apt-get install python3-pip -y
pip3 install pandas
pip3 install tabulate

