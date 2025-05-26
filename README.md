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
in vm1 run:

	sudo docker pull onosproject/onos

## - Pull Containernet Image
in vm1 run:

	sudo  docker pull containernet/containernet:v1


 
## - Change Directory to our project
in vm1 run:

	cd projet_M207

 ## - Create a custom ubuntu vm image acting as a gateway using the Dockerfile
in vm1 run :

	sudo docker build -t gateway .

 ## - Create two vms for Kubernetes
Create two vms one as a master node (vm2) and the second as a worker node (vm3) and install Kubeadm by following the kubeadm_install.txt file in the repositry or by following the documentation
	https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/

## - Deploy services in Kubernetes
After installing and running kubeadm create three yaml files in the master node for: http, samba and mysql (The files are provided in the repositry). And then run the follwing commands in vm1:
	`kubectl apply -f http.yaml`
 	`kubectl apply -f mysql.yaml`
  	`kubectl apply -f samba.yaml`
Check if the services are running and their ports by typing:
	`kubectl get svc`
	    
## - Run docker-compose.yaml file
in vm1 run :

	sudo docker compose up -d

## - Access Onos web GUI
http://<vm1-ip-address>:8181/onos/ui/
Username : onos, Password : rocks

## - Activate applications in onos
	
In onos web gui go to the main menu -> Applications
	
Activate the following applications : 

	OpenFlow Base Provider (org.onosproject.openflow-base)  

	Proxy ARP/NDP (org.onosproject.proxyarp)

	LLDP Link Provider (org.onosproject.lldpprovider)

	Host Location Provider (org.onosproject.hostprovider)

	Reactive Forwarding (org.onosproject.fwd)

	Access Control Lists (org.onosproject.acl)



## - Access the containernet container in vm1 and create a new python file
in vm1 run:

	sudo docker exec -it containernet bash
	
	apt install nano
	
	nano mytopo.py

copy and paste mytopo.py file from the repositry and run :
	
	mn -c
	mn --custom mytopo.py	

## - Prevent Hosts from accessing the internet but allow accessing the other hosts

in vm1 run :
	curl -u onos:rocks -X POST -H "Content-Type: application/json" -d '{
	"srcIp": "10.10.0.0/16",
	"dstIp": "10.10.0.0/16",
	"action": "ALLOW"
	}' http://<vm1-ip-address>:8181/onos/v1/acl/rules
#
	curl -u onos:rocks -X POST -H "Content-Type: application/json" -d '{
	"srcIp": "10.10.0.0/16",
	"dstIp": "<your-vm-lan-network-address>/16",
	"action": "ALLOW"
	}' http://<vm1-ip-address>:8181/onos/v1/acl/rules
#
	curl -u onos:rocks -X POST -H "Content-Type: application/json" -d '{ 
	"srcIp": "10.10.0.0/16",
	"action": "DENY"
	}' http://<vm1-ip-address>:8181/onos/v1/acl/rules

