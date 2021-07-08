# Suricata

Suricata is a free and open source, mature, fast and robust network threat detection engine.

The Suricata engine is capable of real time intrusion detection (IDS), inline intrusion prevention (IPS), network security monitoring (NSM) and offline pcap processing.

Suricata inspects the network traffic using a powerful and extensive rules and signature language, and has powerful Lua scripting support for detection of complex threats.

## Install Suricata

Install Suricata (OSX)

https://redmine.openinfosecfoundation.org/projects/suricata/wiki/Mac_OS_X_10_11

Download open Emerging Threat rules

```bash
wget https://rules.emergingthreats.net/open/suricata/emerging.rules.zip
tar zxvf emerging.rules.tar.gz
sudo mkdir /var/lib/suricata/
sudo mv rules /var/lib/suricata/
```


Update Suricata config to point to that folder `/etc/suricata/suricata.yaml`

```
default-rule-path: /var/lib/suricata/rules

rule-files:
  - emerging*
```


## Download Mordor Pcaps

Clone Project and change directories

```bash
git clone https://github.com/OTRF/mordor && cd mordor/datasets/large
```


Decompress every PCAP in the same folder (Password Protected: `infected`)

```bash
find apt29/day*/pcaps -name '*.zip' -execdir unzip -P infected {} \;
```


## Run Suricata

Run Suricata on every single PCAP and append results from every PCAP to `fast.log` and `eve.json` files in their respective directories.

```bash
find apt29/day*/pcaps -name '*cap' -execdir suricata -r {} -k none \;
```


Stack count the alers generated

```bash
jq 'select((.event_type == "alert") and .alert.category != "Generic Protocol Command Decode") | .alert.signature' apt29/day1/pcaps/eve.json | sort | uniq -c
```
