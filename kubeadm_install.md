#For the Master Node:

1 - sudo swapoff -a
  - comment swap line in /etc/fstab

2 - Install Docker engine https://docs.docker.com/engine/install/ubuntu/

3 - sudo chmod 646 /etc/containerd/config.toml

4 - containerd config default > /etc/containerd/config.toml

5 - sudo nano /etc/containerd/config.toml  
    change "SystemdCgroup = false" to "SystemdCgroup = true" 
    change "sandbox_image = "registry.k8s.io/pause:3.8" to "sandbox_image = "registry.k8s.io/pause:3.10"
    save the file and exit

6 - sudo systemctl restart containerd

7 - sudo apt-get update

8 - sudo apt-get install -y apt-transport-https ca-certificates curl gpg

9 - curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.33/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

10 - echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.33/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list

11 - sudo apt-get update

12 - sudo apt-get install -y kubelet kubeadm kubectl

13 - sudo apt-mark hold kubelet kubeadm kubectl

14 - sudo systemctl enable --now kubelet

15 - kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=<master-node-ip>

16 - mkdir -p $HOME/.kube

17 - sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config

18 - sudo chown $(id -u):$(id -g) $HOME/.kube/config

19 - sudo modprobe br_netfilter

20 - echo "br_netfilter" | sudo tee /etc/modules-load.d/k8s.conf

21 - cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
     net.bridge.bridge-nf-call-iptables  = 1
     net.ipv4.ip_forward                 = 1
     net.bridge.bridge-nf-call-ip6tables = 1
     EOF
 
22 - sudo sysctl --system

23 - kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml



For the Worker Node:

1 - sudo swapoff -a
  - comment swap line in /etc/fstab

2 - Install Docker engine https://docs.docker.com/engine/install/ubuntu/

3 - sudo chmod 646 /etc/containerd/config.toml

4 - containerd config default > /etc/containerd/config.toml

5 - sudo nano /etc/containerd/config.toml
    change "SystemdCgroup = false" to "SystemdCgroup = true"
    change "sandbox_image = "registry.k8s.io/pause:3.8" to "sandbox_image = "registry.k8s.io/pause:3.10"
    save the file and exit

6 - sudo systemctl restart containerd

7 - sudo apt-get update

8 - sudo apt-get install -y apt-transport-https ca-certificates curl gpg

9 - curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.33/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-a>

10 - echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.33/deb/ /' | sud>

11 - sudo apt-get update

12 - sudo apt-get install -y kubelet kubeadm kubectl

13 - sudo apt-mark hold kubelet kubeadm kubectl

14 - sudo systemctl enable --now kubelet

15 - after running "kubeadm init" in the master node run :
     kubeadm join <your-master-node-info>

16 - sudo modprobe br_netfilter

17 - echo "br_netfilter" | sudo tee /etc/modules-load.d/k8s.conf

18 - cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
     net.bridge.bridge-nf-call-iptables  = 1
     net.ipv4.ip_forward                 = 1
     net.bridge.bridge-nf-call-ip6tables = 1
     EOF

19 - sudo sysctl --system
