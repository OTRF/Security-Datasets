#!/bin/bash

# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# *********** log tagging variables ***********
INFO_TAG="[INSTALLATION-INFO]"
ERROR_TAG="[INSTALLATION-ERROR]"
DATE_TIME=`date "+%Y-%m-%d %H:%M:%S"`

# *********** Set Log File ***************
LOGFILE="/var/log/C2s-install.log"
echoerror() {
    printf "${RC} * ERROR${EC}: $@\n" 1>&2;
}

# *********** helk function ***************
usage(){
    echo " "
    echo "Usage: $0 [option...]" >&2
    echo
    echo "   -r         run a specific C2 server (empire or covenant or caldera)"
    echo "   -h         help menu"
    echo
    echo "Examples:"
    echo " $0 -r caldera"
    echo " "
    exit 1
}

# ************ Command Options **********************
while getopts r:h option
do
    case "${option}"
    in
        r) RUN_C2=$OPTARG;;
        h) usage;;
        \?) usage;;
        :  ) echo "Missing option argument for -$OPTARG" >&2; exit 1;;
        *  ) echo "Unimplemented option: -$OPTARG" >&2; exit 1;;
    esac
done

if ((OPTIND == 1))
then
    echo "$ERROR_TAG No options specified"
    usage
fi

# *********** Validating Input ***************
case $RUN_C2 in
    empire);;
    covenant);;
    caldera);;
    *)
        echo "$ERROR_TAG Not a valid C2 option. Valid Options: empire or covenant or caldera"
        usage
    ;;
esac

# *********** Installing Docker Compose ***************
if ! [ -x "$(command -v docker-compose)" ]; then
    echo "$INFO_TAG Installing docker-compose.."
    COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d\" -f4)
    curl -L https://github.com/docker/compose/releases/download/$COMPOSE_VERSION/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose >> $LOGFILE 2>&1
    chmod +x /usr/local/bin/docker-compose >> $LOGFILE 2>&1
fi

# *********** Installing Empire ***************
echo "$INFO_TAG Setting up Empire.."
mkdir /opt/Empire
curl -L https://raw.githubusercontent.com/Cyb3rWard0g/mordor/master/environments/windows/docker/empire/docker-compose-empire.yml -o /opt/Empire/docker-compose-empire.yml >> $LOGFILE 2>&1

# *********** Installing Covenant ***************
echo "$INFO_TAG Setting up Covenant.."
git clone --recurse-submodules https://github.com/cobbr/Covenant /opt/Covenant >> $LOGFILE 2>&1
cd /opt/Covenant/Covenant && docker build -t covenant . >> $LOGFILE 2>&1

# *********** Installing Caldera ***************
echo "$INFO_TAG Setting up Caldera.."
mkdir /opt/Caldera
mkdir /opt/Caldera/config
curl -L https://raw.githubusercontent.com/Cyb3rWard0g/mordor/master/environments/windows/docker/caldera/docker-compose-caldera.yml -o /opt/Caldera/docker-compose-caldera.yml >> $LOGFILE 2>&1
curl -L https://raw.githubusercontent.com/Cyb3rWard0g/mordor/master/environments/windows/docker/caldera/config/facts/a93f6915-a9b8-4a6b-ad46-c072963b32c1.yml -o /opt/Caldera/config/a93f6915-a9b8-4a6b-ad46-c072963b32c1.yml >> $LOGFILE 2>&1
# **** FIX *******
curl -L https://raw.githubusercontent.com/Cyb3rWard0g/mordor/master/environments/windows/docker/caldera/config/fix/defense-evasion/03afada1-1714-408f-bde5-f528b91dc89d.yml -o /opt/Caldera/config/03afada1-1714-408f-bde5-f528b91dc89d.yml >> $LOGFILE 2>&1

# *********** Running default C2 Selected ***********
if [[ $RUN_C2 == "covenant" ]]; then
    echo "$INFO_TAG Running Covenant by default.."
    docker run -d -it -p 7443:7443 -p 80:80 -p 443:443 --name covenant -v /opt/Covenant/Covenant/Data:/app/Data covenant >> $LOGFILE 2>&1  
elif [[ $RUN_C2 == "empire" ]]; then
    echo "$INFO_TAG Running Empire by default.."
    docker-compose -f /opt/Empire/docker-compose-empire.yml up --build -d
else
    echo "$INFO_TAG Running Caldera by default.."
    docker-compose -f /opt/Caldera/docker-compose-caldera.yml up --build -d
fi