 - Ubuntu Vm

 - Clone the repositry
	git clone https://github.com/younessoub/projet_M207.git

 - Install docker
	https://docs.docker.com/engine/install/ubuntu/
	
 - Pull Onos Image 
	sudo docker pull onosproject/onos

 - Pull Containernet Image
	sudo  docker pull containernet/containernet

 - Create docker-compose.yml
	version: '3.3'

	services:
	  onos:
	    image: onosproject/onos:latest
	    restart: always
	    ports:
	      - "8181:8181"
	      - "6633:6633"
	      - "6653:6653"
	    container_name: onos

	  containernet: 
	    depends_on: 
	      - onos
	    image: containernet/containernet:v1
	    volumes:
	      - "/var/run/docker.sock:/var/run/docker.sock"      
	    privileged: true
	    pid: host
	    tty: true
	    container_name: containernet
	    
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
	
	
