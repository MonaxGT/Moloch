FROM ubuntu:16.04
LABEL maintainer Makhinov Alex

# Install curl
RUN apt-get -qq update
# Install the packages
RUN apt-get install -yq curl
# Set the right npm repository for nodejs
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
# Update the repo and install packets
RUN apt update \
  && apt install -yq bison \
                     flex \
                     g++ \
                     gcc \
                     gettext \
                     git \
                     libbz2-dev \
                     libffi-dev \
                     libgeoip-dev \ 
                     libjson-perl \
                     libmagic-dev \
                     libpcap-dev \
                     libpcre3-dev \
                     libpng-dev \
                     libwww-perl \
                     libyaml-dev \
                     locales \
                     make \
                     net-tools \
                     nodejs \
                     phantomjs \
                     pkg-config \
                     python3 \
                     python3-pip \
                     sudo \
                     uuid-dev \
                     vim \
                     wget \
                     xz-utils \
                     yara \
                     zlib1g-dev \
  && rm -rf /var/cache/apt/* 

# add UTF-8 
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# add scripts
COPY /scripts /data
RUN chmod 755 /data/*.sh

# Start building Moloch
RUN /data/buildmoloch.sh /data/moloch-git  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# symlink nodejs for moloch viewer npm
#RUN ln -s /usr/bin/nodejs /data/moloch/bin/node
# Add moloch bin path
RUN ln -s /data/moloch/bin/moloch-capture /usr/bin/moloch-capture
RUN ln -s /data/moloch/bin/moloch-capture /usr/bin/capture
# Add moloch config
COPY /etc /data/moloch/etc
# Set volumes
VOLUME ["/data/moloch/logs","/data/moloch/data","/data/moloch/raw","/data/pcap"]
# Set expose port for moloch viewer
EXPOSE 8005

WORKDIR /data/moloch

ENTRYPOINT ["/data/startmoloch.sh"]
