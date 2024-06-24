# Zabbix-agent on ubuntu

## Install the Zabbix-agent
```shell
# ubuntu 24.04
wget https://repo.zabbix.com/zabbix/7.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_7.0-1+ubuntu22.04_all.deb
sudo dpkg -i zabbix-release_7.0-1+ubuntu22.04_all.deb
sudo apt update 
sudo apt -y install zabbix-agent postgresql-client postgresql-contrib
sudo systemctl restart zabbix-agent
sudo systemctl enable zabbix-agent 
```


### Rappel Docker
install docker   
```shell
sudo apt install -y docker.io unzip
sudo usermod -aG docker ubuntu 





## Install a database 
```shell
# Test database airport
docker volume create data
docker volume ls
docker run -d \
	--name db \
	--restart=always \
	-e POSTGRES_PASSWORD=password \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v data:/var/lib/postgresql/data \
	-p 32432:5432 \
      postgres
```
### install portainer 
```shell
docker volume create portainer_data
docker run -d -p 32125:8000 -p 32126:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock \
 -v portainer_data:/data portainer/portainer-ce:latest
```

## Add database user 
```sql
CREATE USER zbx_monitor WITH PASSWORD 'zabbix';
GRANT pg_monitor TO zbx_monitor;
ALTER USER zbx_monitor WITH SUPERUSER;
```

## install Zabbix template postgresql monitoring
```shell
git clone https://github.com/zabbix/zabbix.git
cd zabbix/
cd templates/
cd db
cd postgresql
sudo apt install postgresql-client postgresql-contrib
psql
sudo mkdir -p  /var/lib/zabbix
sudo cp -r postgresql/ /var/lib/zabbix
ll /var/lib
sudo chown zabbix:zabbix  /var/lib/zabbix
ll /var/lib
sudo cp template_db_postgresql.conf /etc/zabbix/zabbix_agentd.d
sudo systemctl restart zabbix-agent
```

## install extension pg_stat_statements
```sql
# in postgresql.conf
shared_preload_libraries = 'pg_stat_statements'
  
pg_stat_statements.track = all
pg_stat_statements.max = 10000
track_io_timing = on
```
restart postgresql
and 
```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```
Check 
```sql
SELECT count(*) FROM pg_stat_statements;  # return 41
```

Load
```sql
psql -U db_user db_name < dump_file.sql
```