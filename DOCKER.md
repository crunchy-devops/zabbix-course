# Docker lab

## Pre-requis virtualenv, Ansible and Docker on  Ubuntu 20.04
```shell
sudo apt update   # update all packages
sudo apt -y install sshpass # allow using ssh with a password
sudo apt -y install python3-venv

#fork and clone ---> git clone https://github.com/crunchy-devops/ansible-course.git
cd zabbix-course
python3 -m venv venv # set up the module venv in the directory venv
source venv/bin/activate # activate the python virtualenv
pip3 install wheel # set for permissions purpose
pip3 install ansible # install ansible
pip3 install sqlalchemy # install access to a postgres database from python
pip3 install psycopg2-binary # driver for postgres 
pip3 install natsort # for sorting alphanum 
pip3 install requests # extra packages 
ansible --version  # check version number , should be the latest 2.12.6+
ansible-playbook -i inventory  playbook.yml  # run a playbook
# Close your IDE
cd zabbix-course 
source venv/bin/activate # activate the python virtualenv
docker ps
```
## Build 
```shell
docker build -t zabbix-agent .
```

## Run
```shell
 docker run -d --name agent -p 10050:10050 \
 -v $PWD/zabbix_agentd.conf:/etc/zabbix/zabbix_agentd.conf \
 -v /opt/zabbix/log:/log \
 zabbix-agent
```