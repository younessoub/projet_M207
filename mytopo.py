#!/usr/bin/python

## Example topology for containernet
## Created by Jorge Lopez & Jose Reyes 

"""
This is a simple example of a Containernet custom topology.
"""
from mininet.net import Containernet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
import sys
import socket

setLogLevel('info')

net = Containernet()
info('*** Adding controller\n')
c1 = RemoteController( 'c1' , ip=socket.gethostbyname("onos"), port=6633)
net.addController(c1)

info('*** Adding gateway container\n')
gateway = net.addDocker('gateway', ip='10.10.1.1', mac='00:00:00:00:00:01', dimage="gateway")

info('*** Adding docker containers\n')
h1 = net.addDocker('h1', ip='10.10.10.1', mac='9a:d8:73:d8:90:6a', dimage="ubuntu:trusty")
info('*** Adding hosts\n')
h2 = net.addHost('h2',  ip='10.10.20.1', mac='9a:d8:73:d8:90:6b')
h3 = net.addHost('h3',  ip='10.10.20.2', mac='9a:d8:73:d8:90:6c')

info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s3 = net.addSwitch('s3')
s4 = net.addSwitch('s4')
s5 = net.addSwitch('s5')

info('*** Creating links\n')

## switch 1 links
net.addLink( s1, s2, 2, 1 )
net.addLink( s1, s3, 3, 1 )
net.addLink( s1, s4, 4, 1 )
net.addLink( s1, s5, 5, 1 )

## switch 2 links
net.addLink( s2, gateway, 21, 2)
net.addLink( s2, s3, 3, 2 )
net.addLink( s2, s4, 4, 2 )
net.addLink( s2, s5, 5, 2 )

## switch 3 links 

net.addLink( s3, s4, 4, 3 )
net.addLink( s3, h1, 11, 3 )

## switch 4 links 
net.addLink (s4, s5, 5, 4) 
net.addLink (s4, h2, 12, 4) 
net.addLink (s4, h3, 13, 4) 




info('*** Starting network\n')
net.start()

gateway.cmd("iptables --table nat -A POSTROUTING -o eth0 -j MASQUERADE")
gateway.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")


h1.cmd("ip route add default via 10.10.1.1")
h2.cmd("ip route add default via 10.10.1.1")
h3.cmd("ip route add default via 10.10.1.1")

info('*** Running CLI\n')
CLI(net)
net.stop()
