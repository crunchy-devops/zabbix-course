# Zabbix Proxy

## Install from packages
```shell
cd
sudo apt update
wget https://repo.zabbix.com/zabbix/6.1/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.1-1+ubuntu20.04_all.deb
sudo dpkg -i zabbix-release_6.1-1+ubuntu20.04_all.deb
sudo apt update
sudo apt install -y zabbix-sql-scripts build-essential postgresql-server-dev-all zlib1g zlib1g-dev libevent-dev libpcre3 libpcre3-dev

```

## Get zabbix proxy source 
```shell
wget https://cdn.zabbix.com/zabbix/sources/stable/6.0/zabbix-6.0.5.tar.gz
tar -zxvf zabbix-6.0.5.tar.gz
cd zabbix-6.0.5

```


## Install database
```shell
sudo apt install -y postgresql postgresql-contrib
sudo vi /etc/postgresql/14/main/postgresql.conf
# change listen_addresses to  listen_addresses = "*"
sudo vi /etc/postgresql/14/main/pg_hba.conf
# add a line in IPV4 block 
# host    all             all             90.100.22.20/32         md5
# 90.xx. is your internet provider IP address
sudo systemctl stop postgresql
sudo systemctl start postgresql

```


### Psql and create proxy database
```shell

sudo -s
cd  /usr/share/doc/zabbix-sql-scripts/postgresql 
su postgres
psql
CREATE DATABASE zabbix_proxy;

CREATE ROLE zabbix_proxy WITH LOGIN ENCRYPTED PASSWORD 'zabbix';
\c zabbix_proxy
\i proxy.sql
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO zabbix_proxy;
exit
exit
```


### Compile zabbix proxy
```angular2html
cd ~
cd zabbix-6.0.5
./configure --prefix=/opt/zabbix --enable-proxy --with-postgresql=/usr/lib/postgresql/14/bin/pg_config
make
```



