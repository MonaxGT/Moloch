FROM ubuntu:18.04
LABEL maintainer Natalia Nizhevyasova

# Install curl
RUN apt-get -qq update
# Install the packages
RUN apt-get install -yq lsb-release \
                        ruby-dev \
                        make \
                        python-pip \
                        git \
                        vim \
                        libtest-differences-perl \
                        sudo \
                        wget \
                        curl \
                        node-gyp \
                        && rm -rf /var/lib/apt/lists/*

RUN gem install --no-ri --no-rdoc fpm \
                                  && pip install awscli


# Install NODE
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
# Clone and install MOLOCH
RUN git clone https://github.com/aol/moloch
RUN cd /moloch && ./easybutton-build.sh --install

# Add moloch bin path
RUN ln -s /data/moloch/bin/npm /usr/bin/npm
RUN cd /moloch && make install
# Add and run moloch config
COPY /etc /data/moloch/etc
RUN cd /moloch && make config < /data/moloch/etc/config.ini
RUN mkdir /data/script

# Download and install new version NodeJS
RUN cd /moloch \
    && wget https://nodejs.org/dist/v8.15.0/node-v8.15.0-linux-x64.tar.xz
RUN cd /moloch/ && tar xf node-v8.15.0-linux-x64.tar.xz
RUN cp /moloch/node-v8.15.0-linux-x64/bin/* /usr/bin/

# Set volumes
VOLUME ["/data/moloch/logs","/data/moloch/data","/data/moloch/raw","/data/pcap"]

# Set expose port for moloch viewer
EXPOSE 8005

WORKDIR /data/moloch/bin

ENTRYPOINT ["/data/script/startmoloch.sh"]
