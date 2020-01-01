Export Mordor Data
==================

You can create your own mordor datasets like the json files available in this repo.
The mordor style to do this is by exporting data from a kafka broker and writinng it to a JSON file while executing the simulated test.

Kafkacat Style
##############

In consumer mode, Kafkacat reads messages from a topic and prints them to standard output (stdout). You can also redirect it to a file (i.e. JSON)
This means that you can save all the data collected right before you start a simulated test from a Kafka broker.
You can stop the consumption when you are done performing the simulated test.
You can just grab the logs from this repo and re-play them as if they were being ingested in real-time.

Requirements
************

* `Kafka Broker <http://kafka.apache.org/>`_ : A distributed publish-subscribe messaging system that is designed to be fast, scalable, fault-tolerant, and durable  (``Installed by HELK``).
* `Kafkacat <https://github.com/edenhill/kafkacat>`_ : A generic non-JVM producer and consumer for Apache Kafka >=0.8, think of it as a netcat for Kafka.

.. image:: _static/kafkacat_export.png
    :alt: Kafkacat Consumption Infrastructure
    :scale: 35%

Export Logs
***********

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/kBe6-D1_ais" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Install Kafkacat following the `instructions from the official Kafkacat repo <https://github.com/edenhill/kafkacat#install>`_.

* If you are using a debian-based system, make sure you install the latest Kafkacat deb package.
* I recommend at least Ubuntu 18.04. You can check its `Kafkacat deb package version <https://packages.ubuntu.com/bionic/kafkacat>`_ and compare it with the latest one in the `Kafkacat GitHub repo <https://github.com/edenhill/kafkacat/releases>`_.
* You can also install it from source following the `Quick Build <https://github.com/edenhill/kafkacat#quick-build>`_ instructions.

Consume data being produced from a kafka broker with the following flags:

.. function:: -b

    Kafka Broker

.. function:: -t

    Topic in the Kafka Broker to consume the data from

.. function:: -C

    Consume mode

.. function:: -o

    Offset to start consuming from (i.e. end)

.. code-block:: console

    $ kafkacat -b <HELK IP>:9092 -t winlogbeat -C -o end > empire_dcsync_$(date +%F%H%M%S).json

That's it! You now can share that dataset with the community!
