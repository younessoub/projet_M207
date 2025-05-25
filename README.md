## - Linux Vm

Create a linux vm (lets call it vm1) and run 
	sudo apt update && sudo apt upgrade -y 

## - Clone the repositry
in vm1 run:

	git clone https://github.com/younessoub/projet_M207.git

## - Install docker
in vm1 install docker :

	https://docs.docker.com/engine/install/ubuntu/
	
## - Pull Onos Image 
	sudo docker pull onosproject/onos

## - Pull Containernet Image
	sudo  docker pull containernet/containernet

## - Change Directory to our project
	cd projet_M207
	    
## - Run docker-compose.yaml file
	docker compose up

## - Access Onos web GUI
http://localhost:8181/onos/ui/
Username : onos, Password : rocks

## - Activate applications in onos
	
In onos web gui go to the main menu -> Applications
	
Activate the following applications : 

	OpenFlow Base Provider (org.onosproject.openflow-base)  

	Proxy ARP/NDP (org.onosproject.proxyarp)

	LLDP Link Provider (org.onosproject.lldpprovider)

	Host Location Provider (org.onosproject.hostprovider)

	Reactive Forwarding (org.onosproject.fwd)


## - Create a custom ubuntu vm image using the Dockerfile
	sudo docker build -t ubuntuvm .

## - Create two vms for Kubernetes
Create two vms one as a master node or the control plane and the second as a worker node and install Kubeadm
	https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/

## - Deploy services in Kubernetes
After installing and running kubeadm create three yaml files in the master node for: http, samba and mysql (The files are provided in the repositry). And then run the follwing commands:
	`kubectl apply -f http.yaml`
 	`kubectl apply -f mysql.yaml`
  	`kubectl apply -f samba.yaml`
Check if the services are running and their ports by typing:
	`kubectl get svc`

## - Access the containernet container and create a new python file
	sudo docker exec -it containernet bash
	
	touch mytopo.py
	
	apt install nano
	
	nano mytopo.py

copy and paste mytopo.py file from the repositry and run :
	
	mn -c
	python mytopo.py	
