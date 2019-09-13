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

# *********** Installing Docker ***************
if [ -x "$(command -v docker)" ]; then
    echo "$INFO_TAG Installing docker via convenience script.."
    curl -fsSL https://get.docker.com -o get-docker.sh >> $LOGFILE 2>&1
    chmod +x get-docker.sh >> $LOGFILE 2>&1
    ./get-docker.sh >> $LOGFILE 2>&1
fi

# *********** Installing Docker Compose ***************
if ! [ -x "$(command -v docker-compose)" ]; then
    echo "$INFO_TAG Installing docker-compose.."
    COMPOSE_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d\" -f4)
    curl -L https://github.com/docker/compose/releases/download/$COMPOSE_VERSION/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose >> $LOGFILE 2>&1
    chmod +x /usr/local/bin/docker-compose >> $LOGFILE 2>&1
fi

# *********** Installing Empire ***************
echo "$INFO_TAG Setting up Empire.."
curl -L https://raw.githubusercontent.com/Cyb3rWard0g/mordor/master/environment/setup/docker/empire/docker-compose-empire.yml -o /opt/docker-compose-empire.yml >> $LOGFILE 2>&1
echo "$INFO_TAG Empire not started by default.."

# *********** Installing Covenant ***************
echo "$INFO_TAG Setting up Covenant.."
git clone --recurse-submodules https://github.com/cobbr/Covenant /opt >> $LOGFILE 2>&1
cd /opt/Covenant/Covenant && docker build -t covenant . >> $LOGFILE 2>&1

echo "$INFO_TAG Standing up Covenant by default.."
docker run -it -p 7443:7443 -p 80:80 -p 443:443 --name covenant -v /opt/Covenant/Covenant/Data>:/app/Data covenant >> $LOGFILE 2>&1