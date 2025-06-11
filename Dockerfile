FROM ubuntu:xenial               # Use the official Ubuntu 16.04 (Xenial) base image

RUN apt-get update && \          # Update the package list from Ubuntu repositories
    apt-get install -y \         # Install the following packages without prompting for confirmation
    iproute2 \                   # Tools for network management and monitoring (e.g., `ip` command)
    net-tools \                  # Traditional networking tools (e.g., ifconfig, netstat)
    iputils-ping \               # Ping utility to test network connectivity
    iptables \                  # Linux firewall utilities for packet filtering
    dnsutils \                  # DNS utilities like dig and nslookup
    curl \                      # Tool to transfer data from or to a server using various protocols
    tcpdump \                   # Network packet analyzer for capturing network traffic
    vim \                       # Text editor, useful for editing config files
    python && \                 # Python interpreter (default Python 2 in Xenial)
    apt-get clean               # Clean up cached package lists to reduce image size
