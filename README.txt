 - Ubuntu Vm

 - Clone the repositry
	git clone https://github.com/younessoub/projet_M207.git

 - Install docker
	https://docs.docker.com/engine/install/ubuntu/
	
 - Pull Onos Image 
	sudo docker pull onosproject/onos

 - Pull Containernet Image
	sudo  docker pull containernet/containernet

 - Change Directory to our project
	cd projet_M207
	    
 - Run docker-compose.yaml file
	docker compose up

 - Access Onos web GUI
	http://localhost:8181/onos/ui/
	Username : onos, Password : rocks

 - Activate applications in onos
	
	Go to the main menu -> Applications
	
	Activate the following applications : 

		OpenFlow Base Provider (org.onosproject.openflow-base)

		Proxy ARP/NDP (org.onosproject.proxyarp)

		LLDP Link Provider (org.onosproject.lldpprovider)

		Host Location Provider (org.onosproject.hostprovider)

		Reactive Forwarding (org.onosproject.fwd)


 - Create a custom ubuntu vm using the Dockerfile
	sudo docker build -t ubuntuvm .

 - Access the containernet container and create a new python file
	sudo docker exec -it containernet bash
	touch mytopo.py
	apt install nano
	nano mytpo.py
	
	
