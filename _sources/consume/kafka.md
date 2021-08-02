# Kafka

Apache Kafka is a community distributed event streaming platform capable of handling trillions of events a day. Initially conceived as a messaging queue, Kafka is based on an abstraction of a distributed commit log

In order to consume `Security Datasets` the Kafka way, I recommend to use a tool named Kafkacat to act as a Kafka producer and send data to Kafka brokers.
In producer mode, Kafkacat reads messages from standard input (stdin) or a file. This means that you can send data back to any other Kafka broker that you are using as part of your pipeline.
You can just grab the logs from this repo and re-play them as if they were being ingested in real-time.

![](../images/kafka-kafkacat.png)

## Requirements

* [Kafka Broker](http://kafka.apache.org/) : A distributed publish-subscribe messaging system that is designed to be fast, scalable, fault-tolerant, and durable

## Install Kafkacat

Install Kafkacat following the [instructions from the official Kafkacat repo](https://github.com/edenhill/kafkacat#install)

* If you are using a debian-based system, make sure you install the latest Kafkacat deb package.
* I recommend at least Ubuntu 18.04. You can check its [Kafkacat deb package version](https://packages.ubuntu.com/bionic/kafkacat) and compare it with the latest one in the [Kafkacat GitHub repo](https://github.com/edenhill/kafkacat/releases).
* If you are using Ubuntu 19, you might need to run the following commands (Thank you [Jason Yee](https://github.com/jwsy))
    * `wget http://security.ubuntu.com/ubuntu/pool/main/o/openssl1.0/libssl1.0-dev_1.0.2n-1ubuntu5.3_amd64.deb`
    * `sudo dpkg -i libssl1.0.0_1.0.2n-1ubuntu6_amd64.deb`
* You can also install it from source following the [Quick Build](https://github.com/edenhill/kafkacat#quick-build) instructions.

## Download Security Datasets

Download the `Security-Datasets` repo and choose your technique:

```bash
$ curl -LJO https://raw.githubusercontent.com/OTRF/Security-Datasets/master/datasets/small/windows/lateral_movement/host/covenant_wmi_wbemcomn_dll_hijack.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  605k  100  605k    0     0  3522k      0 --:--:-- --:--:-- --:--:-- 3522k
```


Decompress the specific security dataset

```bash
$ unzip covenant_wmi_wbemcomn_dll_hijack.zip 
Archive:  covenant_wmi_wbemcomn_dll_hijack.zip
  inflating: covenant_wmi_wbemcomn_dll_hijack_2020-10-09173318.json
```


## Ship Data to Kafka Broker

Send the data to your own kafka broker via Kafcakat with the following flags:

* **-b**: Kafka Broker
* **-t**: Topic in the Kafka Broker to send the data to
* **-P**: Producer mode
* **-l**: Send messages from a file separated by delimiter, as with stdin. (only one file allowed)

```bash
$ kafkacat -b <Kafka Broker IP>:9092 -t mordortopic -P -l covenant_wmi_wbemcomn_dll_hijack_2020-10-09173318.json
```