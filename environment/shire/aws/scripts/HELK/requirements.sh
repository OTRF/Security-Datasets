#!/bin/bash

apt-get purge python3.5 -y
apt-get install python3.5 -y
apt-get install python3-pip
pip3 install pandas
pip3 install tabulate

