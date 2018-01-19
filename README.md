Moloch on Docker-compose version with some fix.
I took Dockerfile from danielguerra

Start moloch 

``` 
sudo docker-compose up -d 
```

After run you can see to container:
```
CONTAINER ID        IMAGE                         COMMAND                  CREATED             STATUS              PORTS                              NAMES
6b16fb0e6fc6        moloch_docker-moloch          "/data/startmoloch.sh"   21 minutes ago      Up 21 minutes       0.0.0.0:8005->8005/tcp             moloch
682602deee97        elasticsearch:5.2.2-alpine    "/docker-entrypoint.s"   21 minutes ago      Up 21 minutes       0.0.0.0:9200->9200/tcp, 9300/tcp   esmoloch
```

Open your browser and open http://<dockerhost ip>:8005/

Login/Password
 
admin/moloch

Moloch use utils moloch-capture to read pcap to elasticsearch view. 
Compose mount directory /tmp/dump to /data/pcap directory with pcap.
You should run capture and give 2 arguments: name of pcap and tag of dump (if you want filtering soma pcap files to one find "process")

I wrote some bash script, this one take pcap files with path and tag how second argv

```
sudo /bin/bash moloch-eat /data/pcap/c2_cpe2.pcap c2
```

Stop moloch 

```
sudo docker-compose down
```

Delete moloch

```
sudo docker-compose stop
sudo docker-compose rm
```


