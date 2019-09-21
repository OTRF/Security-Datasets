#!/bin/bash

# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# *********** Configuring Caldera **************
echo "Processing Caldera environment variables.."

if [[ -z "$CALDERA_IP" ]]; then
  CALDERA_IP=0.0.0.0
fi
echo "Setting Caldera IP to $CALDERA_IP"

if [[ -z "$CALDERA_PORT" ]]; then
  CALDERA_PORT=8888
fi
echo "Setting Caldera port to $CALDERA_PORT"

if [[ -z "$CALDERA_EXFIL_DIR" ]]; then
  CALDERA_EXFIL_DIR=/tmp
fi
echo "Setting Caldera exfil directory to $CALDERA_EXFIL_DIR"

if [[ -z "$CALDERA_MEMORY" ]]; then
  CALDERA_MEMORY=True
fi
echo "Setting Caldera memory to $CALDERA_MEMORY"

if [[ -z "$CALDERA_UNTRUSTED_TIMER" ]]; then
  CALDERA_UNTRUSTED_TIMER=180
fi
echo "Setting Caldera untrusted timer to $CALDERA_UNTRUSTED_TIMER"

if [[ -z "$CALDERA_DEBUG" ]]; then
  CALDERA_DEBUG=False
fi
echo "Setting Caldera debug to $CALDERA_DEBUG"

if [[ -z "$CALDERA_ADMIN_NAME" ]]; then
  CALDERA_ADMIN_NAME=admin
fi
echo "Setting Caldera admin user to $CALDERA_ADMIN_NAME"

if [[ -z "$CALDERA_ADMIN_PASSWORD" ]]; then
  CALDERA_ADMIN_PASSWORD=admin
fi
echo "Setting Caldera admin password to $CALDERA_ADMIN_PASSWORD"

echo "Updating properties of the caldera local conf file .."
sed -i "s/^host\:.*$/host\: ${CALDERA_IP}/g" /opt/Caldera/conf/local.yml
sed -i "s/^port\:.*$/port\: ${CALDERA_PORT}/g" /opt/Caldera/conf/local.yml
sed -i "s/^exfil_dir\:.*$/exfil_dir\: \\${CALDERA_EXFIL_DIR}/g" /opt/Caldera/conf/local.yml
sed -i "s/^memory\:.*$/memory\: ${CALDERA_MEMORY}/g" /opt/Caldera/conf/local.yml
sed -i "s/^untrusted_timer\:.*$/untrusted_timer: ${CALDERA_UNTRUSTED_TIMER}/g" /opt/Caldera/conf/local.yml
sed -i "s/^debug\:.*$/debug\: ${CALDERA_DEBUG}/g" /opt/Caldera/conf/local.yml
sed -i "s/  admin\: admin/  ${CALDERA_ADMIN_NAME}\: ${CALDERA_ADMIN_PASSWORD}/g" /opt/Caldera/conf/local.yml

echo "Final local conf file .."
cat /opt/Caldera/conf/local.yml
echo " "

exec "$@"