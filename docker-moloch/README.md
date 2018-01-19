

Docker Moloch v0.20.20 container

## Docker image usage

First start elasticsearch 5.2.2

```
docker run -d --name es elasticsearch:5.2.2-alpine
```

Then start moloch
```
docker run --name moloch -p 8005:8005 -d --link es:elasticsearch danielguerra/moloch
```

Open your browser and open

http://<dockerhost ip>:8005/

Use the following Username/Password

admin THEPASSWORD

## Examples

Run capture on docker container eth0 interface:

```
docker run --link es:elasticsearch danielguerra/moloch moloch-capture
```

Run viewer and import pcap to analyze:

```
docker run -d --name moloch --link es:elasticsearch -v /path/to/host/pcap:/data/pcap:rw danielguerra/moloch
docker exec moloch capture -r /data/pcap/sniff.pcap -t mysniff
```
