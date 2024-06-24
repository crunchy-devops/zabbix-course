# install kind
```shell
sudo snap install go --classic
go install sigs.k8s.io/kind@latest
kind create cluster --name=kube --config kind-config.yml --image kindest/node:v1.30.0
```