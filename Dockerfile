FROM ubuntu:20.04

RUN apt update && \
    apt install -y wget vim  && \
    wget https://repo.zabbix.com/zabbix/6.1/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.1-1+ubuntu20.04_all.deb && \
    dpkg -i zabbix-release_6.1-1+ubuntu20.04_all.deb && \
    apt update && \
    apt install -y zabbix-agent

EXPOSE 10050
VOLUME ["/log"]
CMD ["/usr/sbin/zabbix_agentd","--foreground", "-c", "/etc/zabbix/zabbix_agentd.conf"]