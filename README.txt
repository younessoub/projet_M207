1 - Ubuntu Vm

2 - Install docker
	https://docs.docker.com/engine/install/ubuntu/
	
3 - Pull Onos Image 
	sudo docker pull onosproject/onos

4 - Pull Containernet Image
	sudo  docker pull containernet/containernet

5 - Create docker-compose.yml
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
	    
6 - Run docker-compose.yaml file
	docker compose up

7 - Access Onos web GUI
	http://localhost:8181/onos/ui/
	Username : onos, Password : rocks

8 - Activate applications in onos
	
	Go to the main menu -> Applications
	
	Activate the following applications : 

		OpenFlow Base Provider (org.onosproject.openflow-base)

		Proxy ARP/NDP (org.onosproject.proxyarp)

		LLDP Link Provider (org.onosproject.lldpprovider)

		Host Location Provider (org.onosproject.hostprovider)

9 - Access the onos container and access the CLI
	sudo docker exec -it onos bash
	./apache-karaf-4.2.14/bin/client
	app activate org.onosproject.fwd

10 - Access the containernet container and create a new python file
	sudo docker exec -it containernet bash
	touch mytopo.py
	apt install nano
	nano mytpo.py
	
	
