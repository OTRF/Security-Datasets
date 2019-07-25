## Create Dataset: 
1. Get your attack ready inside of the Empire Server
2.  Create a Listener and already have an Agent on the machine you are attacking. The reason for this, is because we are collecting data for a specific attack technique, not the initial foothold that allowed entry into a machine. 
3.  Get the module ready for the attack you choose to perform. Do not press execute yet. 

4.  Migrate over to the HELK machine and prepare kafkacat to start collecting the data. To do so, follow the command examples below:

`kafkacat -b HELK-IP:9092 -t winlogbeat -C -o end > name_technique_$(date +%F%H%M%S).json`

#### For this exercise, the command will look like:

`kafkacat -b 172.18.39.6:9092 -t winlogbeat -C -o end > kerberoast_$(date +%F%H%M%S).json`

5.  Migrate back to the Empire Server and execute the attack technique. 


6.  After the attack was successful, migrate back to the HELK machine.
7. Wait 30-45 seconds so that kafkacat had time to ingest all the data from this attack, then press Control-C. This will stop the ingestion process. All of the data is now stored in a json format, and can be pulled down to your local machine to store or to a SIEM of your choice to start analyzing the data and building out a robust detection.

## Validate the dataset: 
Next, we are going to run uruk_hai_stats.py against the newly recorded dataset, to show us the log statistics that correlate with this attack. This script will sort out the data by log name, source name, task, and record number. This helps us understand how much data can be produced during an attack. Keep in mind not all of this data will be useful when it comes to detection efforts. 

#### To validate and our test data consumption worked properly, run:
`python3 uruk_hai_stats.py -f name_technique_$(date +%F%H%M%S).json`

#### For this exercise, the command will look like:
`python3 uruk_hai_stats.py -f /home/aragon/kerberoast_2019-07-14005430.json`


Uruk-Hai Stats result for the Kerberoast dataset that was just created.

*The uruk_hair_stats.py can be found in the /opt/mordor/scripts folder inside of the HELK machine or can be found at: https://github.com/Cyb3rWard0g/mordor/tree/master/scripts.*

If you want to run this outside of Mordor AWS in your own lab be sure to have pandas and python3 installed. Although this is already installed in Mordor AWS during the configuration process. 

## Pulling Dataset to local machine:

 Lastly, you could keep the dataset in the lab and analyze it in HELK, but you could also pull it down to your local machine using SCP. This would allow you to consume the dataset in any SIEM of your choosing, so that you can start building out your detection efforts. 
 
 To do so follow this command:

`sudo scp aragorn@public-ip:path/to/dataset/ /path/to/destination`

## Injest the dataset into SIEM with `kafkacat`:
*In this example we will be using the Mordor enviroments HELK instance. You can run this on SIEM of choice as long as you have a Kafka broker.*

1. Untar the dataset of choice:

` tar -xzvf empire_dcsync.tar.gz `

2. Use `kafkacat` to send dataset to Kafka broker:

` kafkacat -b <HELK IP>:9092 -t winlogbeat -P -l empire_dcsync_2019-03-01174830.json `

Give your Kafka broker about 30 seconds to injest the data. After this is done, you can start querying the data!
