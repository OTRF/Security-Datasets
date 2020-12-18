# Kafka

In consumer mode, Kafkacat reads messages from a topic and prints them to standard output (stdout). You can also redirect it to a file (i.e. JSON)
This means that you can save all the data collected right before you start a simulated test from a Kafka broker.
You can stop the consumption when you are done performing the simulated test.
You can just grab the logs from this repo and re-play them as if they were being ingested in real-time.

## Requirements

* [Kafka Broker](http://kafka.apache.org/) : A distributed publish-subscribe messaging system that is designed to be fast, scalable, fault-tolerant, and durable  (**Installed by HELK**).

![](images/kafkacat_export.png)

## Install Kafkacat

Install Kafkacat following the [instructions from the official Kafkacat repo](https://github.com/edenhill/kafkacat#install)

* If you are using a debian-based system, make sure you install the latest Kafkacat deb package.
* I recommend at least Ubuntu 18.04. You can check its [Kafkacat deb package version](https://packages.ubuntu.com/bionic/kafkacat) and compare it with the latest one in the [Kafkacat GitHub repo](https://github.com/edenhill/kafkacat/releases).
* You can also install it from source following the [Quick Build](https://github.com/edenhill/kafkacat#quick-build) instructions.

## Export Security Events

Consume data being produced from a kafka broker with the following flags:

* **-b**: Kafka Broker
* **-t**: Topic in the Kafka Broker to consume the data from
* **-C**: Consumer mode
* **-o**: Offset to start consuming from (i.e. end)

```bash
$ kafkacat -b <Kafka-Broker-IP>:9092 -t winlogbeat -C -o end > empire_dcsync_$(date +%F%H%M%S).json
```

That's it! You now can share that dataset with the community!
