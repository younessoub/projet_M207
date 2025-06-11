#!/usr/bin/python
## Example topology for containernet
## Created by Jorge Lopez & Jose Reyes 
"""
This is a simple example of a Containernet custom topology.
"""

# Import necessary modules for Containernet networking
from mininet.net import Containernet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
import sys
import socket

# Set logging level to info for detailed output
setLogLevel('info')

# Create a new Containernet instance
net = Containernet()

# Add a remote controller (ONOS) to manage the network
info('*** Adding controller\n')
c1 = RemoteController( 'c1' , ip=socket.gethostbyname("onos"), port=6633)
net.addController(c1)

# Add a Docker container that will serve as the network gateway
info('*** Adding gateway container\n')
gateway = net.addDocker('gateway', ip='10.10.1.1', mac='00:00:00:00:00:01', dimage="gateway")

# Add Docker containers as network hosts
info('*** Adding docker containers\n')
h1 = net.addDocker('h1', ip='10.10.10.1', mac='9a:d8:73:d8:90:6a', dimage="ubuntu:trusty")

# Add regular Mininet hosts (not Docker containers)
info('*** Adding hosts\n')
h2 = net.addHost('h2',  ip='10.10.20.1', mac='9a:d8:73:d8:90:6b')
h3 = net.addHost('h3',  ip='10.10.20.2', mac='9a:d8:73:d8:90:6c')

# Add OpenFlow switches to the network topology
info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s3 = net.addSwitch('s3')
s4 = net.addSwitch('s4')
s5 = net.addSwitch('s5')

# Create physical links between network components
info('*** Creating links\n')

## Links from switch 1 to other switches (creating a mesh topology)
net.addLink( s1, s2, 2, 1 )  # s1 port 2 connects to s2 port 1
net.addLink( s1, s3, 3, 1 )  # s1 port 3 connects to s3 port 1
net.addLink( s1, s4, 4, 1 )  # s1 port 4 connects to s4 port 1
net.addLink( s1, s5, 5, 1 )  # s1 port 5 connects to s5 port 1

## Links from switch 2 to gateway and other switches
net.addLink( s2, gateway, 21, 2)  # s2 port 21 connects to gateway port 2
net.addLink( s2, s3, 3, 2 )       # s2 port 3 connects to s3 port 2
net.addLink( s2, s4, 4, 2 )       # s2 port 4 connects to s4 port 2
net.addLink( s2, s5, 5, 2 )       # s2 port 5 connects to s5 port 2

## Links from switch 3 to other switches and hosts
net.addLink( s3, s4, 4, 3 )   # s3 port 4 connects to s4 port 3
net.addLink( s3, h1, 11, 3 )  # s3 port 11 connects to h1 port 3

## Links from switch 4 to switch 5 and hosts h2, h3
net.addLink (s4, s5, 5, 4)   # s4 port 5 connects to s5 port 4
net.addLink (s4, h2, 12, 4)  # s4 port 12 connects to h2 port 4
net.addLink (s4, h3, 13, 4)  # s4 port 13 connects to h3 port 4

# Start the network (activate all switches, hosts, and links)
info('*** Starting network\n')
net.start()

# Configure the gateway container for NAT and IP forwarding
gateway.cmd("iptables --table nat -A POSTROUTING -o eth0 -j MASQUERADE")  # Enable NAT for outbound traffic
gateway.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")                      # Enable IP forwarding

# Configure routing on hosts to use the gateway as default route
h1.cmd("ip route del default")              # Remove existing default route on h1
h1.cmd("ip route add default via 10.10.1.1")  # Set gateway as default route for h1
h2.cmd("ip route add default via 10.10.1.1")  # Set gateway as default route for h2
h3.cmd("ip route add default via 10.10.1.1")  # Set gateway as default route for h3

# Start the interactive CLI for network management and testing
info('*** Running CLI\n')
CLI(net)

# Clean up and stop the network when CLI exits
net.stop()
