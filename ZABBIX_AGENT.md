# Zabbix-agent

## Install the Zabbix-agent ubuntu 22.04
```shell
wget https://repo.zabbix.com/zabbix/7.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_7.0-1+ubuntu24.04_all.deb
sudo dpkg -i zabbix-release_7.0-1+ubuntu24.04_all.deb
sudo apt update 
sudo apt -y install zabbix-agent
sudo systemctl restart zabbix-agent
sudo systemctl enable zabbix-agent 


```
## Commands for simulating some workload
```shell
# Memory available
egrep 'MemFree' /proc/meminfo | awk '{print $2}'
fallocate -l 1G
load_disk.sh
df --output=used /dev/vda1 | tail -n 1   # used disk size
df --output=size /dev/vda1 | tail -n 1   # total disk size
#
```



## Install zabbix-agent on ubuntu 
```shell
cd
sudo apt update
wget https://repo.zabbix.com/zabbix/6.1/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.1-1+ubuntu20.04_all.deb
sudo dpkg -i zabbix-release_6.1-1+ubuntu20.04_all.deb
sudo apt update
sudo apt install -y  zabbix-agent
```