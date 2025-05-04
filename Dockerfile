FROM ubuntu:xenial

RUN apt-get update && apt-get install -y \
    iproute2 \
    net-tools \
    iputils-ping \
    iptables \
    dnsutils \
    curl \
    tcpdump \
    vim \
    python && \
    apt-get clean
