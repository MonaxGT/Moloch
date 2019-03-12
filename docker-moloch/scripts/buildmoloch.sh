#!/bin/sh

mkdir -p /data/pcap

if [ -z $1 ]; then
	BUILDDIR=/data/moloch-git
else
	BUILDDIR=$1
fi

echo "git clone"
git clone --recursive https://github.com/aol/moloch.git $BUILDDIR
echo "cd to dir and build"
cd $BUILDDIR
USEPFRING=no ESMEM="4G" DONOTSTART=yes MOLOCHUSER=daemon GROUPNAME=daemon PASSWORD=${PASSWORD_MOLOCH_SHELL} INTERFACE=eth0 BATCHRUN=yes ./easybutton-build.sh
make
make install
cd /data/moloch/viewer
npm install
