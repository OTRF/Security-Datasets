# Author: Roberto Rodriguez (@Cyb3rWard0g)
# License: GPL-3.0

# Referneces:
# https://github.com/EmpireProject/Empire/blob/master/Dockerfile

# image base
FROM ubuntu:16.04

# pull from BUILD
ARG empirversion

# extra metadata
LABEL maintainer="EmpireProject"
LABEL description="Dockerfile base for Empire server."
LABEL version=${empirversion}

# env setup
ENV STAGING_KEY=RANDOM
ENV DEBIAN_FRONTEND=noninteractive

# set the def shell for ENV
SHELL ["/bin/bash", "-c"]

# install basic build items
RUN apt-get update && apt-get install -qy \
    wget \
    curl \
    git \
    sudo \
    apt-utils \
    lsb-core \
    python2.7 \
    python-dev \
    python-pyftpdlib \
  && ln -sf /usr/bin/python2.7 /usr/bin/python \  
  && rm -rf /var/lib/apt/lists/*

# build empire from source
# TODO: When we merge to master set branch to master
RUN git clone --depth=1 -b dev https://github.com/EmpireProject/Empire.git /opt/Empire && \
    cd /opt/Empire/setup/ && \
    ./install.sh && \
    rm -rf /opt/Empire/data/empire*
RUN python2.7 /opt/Empire/setup/setup_database.py
WORKDIR /opt/Empire
CMD ["python2.7", "empire"]
