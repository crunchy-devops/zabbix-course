# Zabbix-course

## Pre-requis installation
```shell
wget https://repo.zabbix.com/zabbix/7.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_7.0-1+ubuntu22.04_all.deb
sudo dpkg -i zabbix-release_7.0-1+ubuntu22.04_all.deb
sudo apt update 
sudo apt -y install zabbix-server-pgsql zabbix-frontend-php php8.1-pgsql zabbix-apache-conf zabbix-sql-scripts zabbix-agent
```
### Rappel Docker
install docker   
```shell
sudo apt install -y docker.io
sudo usermod -aG docker ubuntu
# reload jetbrains

docker volume create data
docker volume ls
docker run -d \
	--name db \
	-e POSTGRES_PASSWORD=password \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v data:/var/lib/postgresql/data \
	-p 32432:5432 \
	-p 5432:5432 \
	postgres

docker volume create portainer_data
docker run -d -p 32125:8000 -p 32126:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock \
 -v portainer_data:/data portainer/portainer-ce:latest

# in portainer container db 
apt update
apt -y install sudo vim
sudo -u postgres createuser --pwprompt zabbix
sudo -u postgres createdb -O zabbix zabbix
 
 # on the vm 
 cd /usr/share/zabbix-sql-scripts/postgresql
 docker cp server.sql.gz db:/tmp
 
 # change postgresql connection  
 cd /var/lib/postgresql/data/pgdata/
 vi pg_hba.conf
 #add in pg_hba.conf
 host zabbix  zabbix   0.0.0.0/0   trust
 # in the db container
 sudo adduser zabbix
 # in portainer 
su zabbix
cd /tmp 
 zcat server.sql.gz |  psql zabbix 
 
```
## Changer le password pour le daemon zabbix_server
```shell
sudo vi /etc/zabbix/zabbix_server.conf
# change 
DBPassword=zabbix
```
## restart all processes
```shell
sudo systemctl restart zabbix-server zabbix-agent apache2
sudo systemctl enable zabbix-server zabbix-agent apache2

## install python3 in virtualenv 

### Useful packages  
```shell
   sudo apt-get update  # update links to repos
   sudo apt-get -y install git wget htop iotop iftop # install git and monitoring tools
   sudo apt-get -y install python3 python3-venv # install python3 and virtualenv
   sudo apt-get -y install build-essential   # need for installing docker-compose
   sudo apt-get -y install python3-dev libxml2-dev libxslt-dev libffi-dev # need for installing docker-compose
   htop  # check your vm config
   Crtl-c  # exit 
``` 
### install this repo and docker    
```shell script
cd   # go back the home directory
python3 -m venv venv  # set up the module venv in the directory venv
source venv/bin/activate  # activate the virtualenv python
pip3 install wheel  # set for permissions purpose
pip3 install --upgrade pip # update pip3
pip3 install requests # extra packages














## install proxy
```shell
sudo apt update
wget https://repo.zabbix.com/zabbix/6.1/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.1-1+ubuntu20.04_all.deb
sudo dpkg -i zabbix-release_6.1-1+ubuntu20.04_all.deb
sudo apt update
sudo apt install -y zabbix-proxy-sqlite3 zabbix-sql-scripts
sudo mkdir –p /var/lib/sqlite/
sudo sqlite3 /var/lib/sqlite/zabbix.db < /usr/share/doc/zabbix-sql-scripts/sqlite3/proxy.sql
sudo chmod -R 777  /var/lib/sqlite
```

## Change zabbix_proxy.conf
```shell
vi /etc/zabbix/zabbix_proxy.conf
# change Zabbix-server ip address
```





