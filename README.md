# Zabbix-course

## Pre-requis installation
```shell
cd
sudo apt update
wget https://repo.zabbix.com/zabbix/6.1/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.1-1+ubuntu20.04_all.deb
sudo dpkg -i zabbix-release_6.1-1+ubuntu20.04_all.deb
sudo apt update
sudo apt install -y zabbix-server-pgsql zabbix-frontend-php php7.4-pgsql zabbix-apache-conf zabbix-sql-scripts zabbix-agent
```
### Rappel Docker
install docker   
```shell
sudo apt install -y docker.io
sudo usermod -aG docker ubuntu
# reload jetbrains
docker run -d --name db -e POSTGRES_PASSWORD=password  -v /opt/postgres:/var/lib/postgresql/data \
 -p 5432:5432 postgres:13.6
docker run -d -p 9000:9000 --name portainer -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer -H unix:///var/run/docker.sock
``` 
### Postgresql 13
Run portainer  
```shell
su postres
psql
CREATE DATABASE zabbix;
CREATE ROLE zabbix WITH LOGIN ENCRYPTED PASSWORD 'zabbix';
```
#### Load the zabbix database 
```shell
cd /usr/share/doc/zabbix-sql-scripts/postgresql

sudo -s
docker cp server.sql.gz db:/tmp/server.sql.gz
#docker cp timescaledb.sql db:/tmp/timescaledb.sql NOTE: not compatible with zabbix proxy

adduser zabbix 
su - zabbix 
cd /tmp
zcat server.sql.gz | psql zabbix 
```
### Partionning 


### TimescaleDB yes or no 