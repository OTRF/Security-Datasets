## Create Dataset: 
1. Get your attack ready inside of the Empire Framework or Covenant Framework.
#### To start/stop the Empire Framework follow these commands:

    sudo docker start mordor-empire
 
    sudo docker exec -ti mordor-empire bash
    
    cd /opt/Empire
    
     ./empire
     
     exit
     
     exit
     
     sudo docker stop Mordor-empire

#### To start the Covenant Framework follow these commands:

```sudo docker run -it -p 7443:7443 -p 80:80 -p 443:443 --name covenant -v /opt/Covenant/Covenant/Data:/app/Data covenant```

Once Covenant has been started, you can disconnect from the interactive interface at any time by pressing `Ctrl+p` and `Ctrl+q` consecutively.

#### To stop the container, you can run:

```docker stop covenant```

#### To restart Covenant interactively (with all data saved), you can run:

```docker start covenant -ai```


2.  Seat yourself access on the machine of choice
            
* Create a listener and then put the agent on the machine you are attacking. The reason for this, is because we are collecting data for a specific attack technique, not the initial foothold that allowed entry into a machine. If you don't know how to do this check out the Empire's documentation here: https://www.powershellempire.com/ OR Covenant's documentation here: https://github.com/cobbr/Covenant/wiki.

3.  Get the module ready for the attack you choose to perform. <strong> Do not press execute yet. </strong>

4.  Migrate over to the HELK machine and prepare kafkacat to start collecting the data. To do so, follow the command examples below:

`kafkacat -b HELK-IP:9092 -t winlogbeat -C -o end > name_technique_$(date +%F%H%M%S).json`

<strong> NOTE: </strong> you will need `root` permissions to perform this. 

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

![uruk-haistats](https://github.com/jsecurity101/jsecurity101.github.io/blob/master/images/MordorAWS/uruk-haistats.png)

<p align="center"><strong> Uruk-Hai Stats result for the Kerberoast dataset that was just created.</strong> </p>

*The uruk_hair_stats.py can be found in the /opt/mordor/scripts folder inside of the HELK machine or can be found at: https://github.com/Cyb3rWard0g/mordor/tree/master/scripts.*

If you want to run this outside of Mordor AWS in your own lab be sure to have pandas and python3 installed. Although this is already installed in Mordor AWS during the configuration process. 

## Pulling Dataset to local machine:

 Lastly, you could keep the dataset in the lab and analyze it in HELK, but you could also pull it down to your local machine using SCP. This would allow you to consume the dataset in any SIEM of your choosing, so that you can start building out your detection efforts. 
 
 To do so follow this command:

`sudo scp aragorn@public-ip:path/to/dataset/ /path/to/destination`

## Injest the dataset into SIEM with kafkacat:
*In this example we will be using the Mordor enviroments HELK instance. You can run this on SIEM of choice as long as you have a Kafka broker.*

1. Untar the dataset of choice:

` tar -xzvf empire_kerberoast.tar.gz `

2. Use `kafkacat` to send dataset to Kafka broker:

` kafkacat -b <HELK IP>:9092 -t winlogbeat -P -l kerberoast_2019-07-25200422.json `

Give your Kafka broker about 30 seconds to injest the data. After this is done, you can start querying the data!

[![kerberoast](https://img.youtube.com/vi/YsEr8tNxVgI/hqdefault.jpg)](https://www.youtube.com/watch?v=YsEr8tNxVgI)
