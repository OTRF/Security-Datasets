#!/bin/bash

# Mordor script: install-terraform-packer.sh
# Mordor script description: Install Terraform for Linux or Mac
# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

SYSTEM_KERNEL="$(uname -s)"

if ! [ -x "$(command -v wget)" ]; then
    echo "[MORDOR-TERRAFORM-INFO] Installing Wget for $SYSTEM_KERNEL"
    if [ "$SYSTEM_KERNEL" == "Linux" ]; then
        apt-get install -y --no-install-recommends wget
    elif [ "$SYSTEM_KERNEL" == "Darwin" ]; then
        brew install wget
    fi
fi

if ! [ -x "$(command -v unzip)" ]; then
    echo "[MORDOR-TERRAFORM-INFO] Installing Unzip for $SYSTEM_KERNEL"
    if [ "$SYSTEM_KERNEL" == "Linux" ]; then
        apt-get install -y --no-install-recommends unzip
    elif [ "$SYSTEM_KERNEL" == "Darwin" ]; then
        brew install unzip
    fi
fi

if ! [ -x "$(command -v awscli)" ]; then
    if [ -x "$(command -v python3)" ]; then
        echo "[MORDOR-TERRAFORM-INFO] Installing awscli for $SYSTEM_KERNEL via pip"
        python3 -m pip install -U awscli
    else
        echo "[MORDOR-TERRAFORM-INFO] python3 is needed for this step.."
        exit 1
    fi
fi

if ! [ -x "$(command -v awsebcli)" ]; then
    if [ -x "$(command -v python3)" ]; then
        echo "[MORDOR-TERRAFORM-INFO] Installing awsebcli for $SYSTEM_KERNEL via pip"
        python3 -m pip install -U awsebcli
    else
        echo "[MORDOR-TERRAFORM-INFO] python3 is needed for this step.."
        exit 1
    fi
fi

TERRAFORM_VERSION=0.12.2

if [ "$SYSTEM_KERNEL" == "Linux" ]; then 
    OPERATING_SYSTEM=linux
elif [ "$SYSTEM_KERNEL" == "Darwin" ]; then
    OPERATING_SYSTEM=darwin
fi

TERRAFORM_DOWNLOAD=https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_${OPERATING_SYSTEM}_amd64.zip

echo "[MORDOR-TERRAFORM-INFO] Installing Terraform & Packer for $SYSTEM_KERNEL"

if ! [ -x "$(command -v /usr/local/bin/terraform)" ]; then
    echo "[MORDOR-TERRAFORM-INFO] Installing Terraform.."
    wget $TERRAFORM_DOWNLOAD -P /tmp/
    unzip -j /tmp/*.zip -d /usr/local/bin/
    rm /tmp/*.zip
fi
