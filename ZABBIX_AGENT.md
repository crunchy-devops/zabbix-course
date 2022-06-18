# Zabbix-agent

## Install the Zabbix-agent on centos 8
```shell
curl 'http://mirror.centos.org/centos/8-stream/BaseOS/x86_64/os/Packages/centos-gpg-keys-8-3.el8.noarch.rpm' --output key.rpm
sudo rpm -i key.rpm 
sudo dnf -y --disablerepo '*' --enablerepo=extras swap centos-linux-repos centos-stream-repos
sudo yum -y update
sudo reboot
sudo rpm -Uvh https://repo.zabbix.com/zabbix/6.0/rhel/8/x86_64/zabbix-release-6.0-1.el8.noarch.rpm
sudo dnf clean all 
sudo dnf install -y zabbix-agent 
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