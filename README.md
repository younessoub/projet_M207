# Introduction
This project demonstrates the practical implementation of Software-Defined Networking (SDN) concepts using a hybrid infrastructure composed of Docker, ONOS, Kubernetes, and Containernet. SDN decouples the control plane from the data plane in networking, enabling centralized, programmable network control.

By deploying SDN with the ONOS controller and Containernet for emulated topologies, this project offers a hands-on environment for understanding dynamic network management, traffic flow control, and access control. Additionally, the use of Kubernetes for service orchestration and GLPI for IT asset management showcases an integrated approach to systems and network administration.

The setup is distributed across three virtual machines and is ideal for IT students, educators, and professionals looking to simulate and manage a full-featured network and system infrastructure.

# 📍 Project Topology

![Topology Diagram](./topo.jpeg)

This project uses **three virtual machines**:

* `vm1`: Linux VM hosting Docker, ONOS, Containernet, and GLPI.
* `vm2`: Kubernetes master node.
* `vm3`: Kubernetes worker node.

---

## 🗅️ 1. Setup VM1 (Linux VM)

### ✅ Update System Packages

```bash
sudo apt update && sudo apt upgrade -y
```

### 🔁 Clone the Repository

```bash
git clone https://github.com/younessoub/projet_M207.git
cd projet_M207
```

### 🐳 Install Docker

Follow the official Docker installation guide for Ubuntu:
👉 [Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

### 📦 Pull Docker Images

```bash
sudo docker pull onosproject/onos
sudo docker pull containernet/containernet:v1
```

### 🛠️ Build Custom Gateway Image

```bash
sudo docker build -t gateway .
```

---

## ⚘️ 2. Setup Kubernetes (VM2 + VM3)

### 🧰 Install Kubeadm

Create two new VMs:

* `vm2`: Kubernetes **master node**
* `vm3`: Kubernetes **worker node**

Install Kubernetes using the instructions in `kubeadm_install.txt` in the repository or follow the official guide:
👉 [Install Kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)

---

## 🚀 3. Deploy Kubernetes Services

On the **master node (vm2)**, create and apply the following YAML files (available in the repo):

```bash
kubectl apply -f http.yaml
kubectl apply -f mysql.yaml
kubectl apply -f samba.yaml
```

Check service status and ports:

```bash
kubectl get svc
```

---

## 🧩️ 4. Run Docker Compose (ONOS + Others)

On `vm1`, run:

```bash
sudo docker compose up -d
```

---

## 🌐 5. Access ONOS Web GUI

Open in browser:
`http://<vm1-ip>:8181/onos/ui/`

* **Username:** `onos`
* **Password:** `rocks`

---

## ⚙️ 6. Activate ONOS Applications

From the ONOS UI:
Go to **Main Menu → Applications** and activate the following:

* OpenFlow Base Provider (`org.onosproject.openflow-base`)
* Proxy ARP/NDP (`org.onosproject.proxyarp`)
* LLDP Link Provider (`org.onosproject.lldpprovider`)
* Host Location Provider (`org.onosproject.hostprovider`)
* Reactive Forwarding (`org.onosproject.fwd`)
* Access Control Lists (`org.onosproject.acl`)

---

## 🥪 7. Use Containernet for Custom Topology

On `vm1`:

```bash
sudo docker exec -it containernet bash
apt install nano
nano mytopo.py
```

Copy the content of `mytopo.py` from the repository.

Run the topology:

```bash
mn -c
mn --custom mytopo.py
```

---

## 📋 8. Install GLPI as a Docker Service

On `vm1`:

```bash
cd glpi
sudo docker compose up -d
```

---

## 🔒 9. Configure ONOS ACL: Allow Internal Traffic Only

Replace `<vm1-ip-address>` and `<your-vm-lan-network-address>` accordingly.

```bash
# Allow communication within the 10.10.0.0/16 subnet
curl -u onos:rocks -X POST -H "Content-Type: application/json" -d '{
  "srcIp": "10.10.0.0/16",
  "dstIp": "10.10.0.0/16",
  "action": "ALLOW"
}' http://<vm1-ip-address>:8181/onos/v1/acl/rules

# Allow access to the LAN
curl -u onos:rocks -X POST -H "Content-Type: application/json" -d '{
  "srcIp": "10.10.0.0/16",
  "dstIp": "<your-vm-lan-network-address>/16",
  "action": "ALLOW"
}' http://<vm1-ip-address>:8181/onos/v1/acl/rules

# Deny internet access
curl -u onos:rocks -X POST -H "Content-Type: application/json" -d '{
  "srcIp": "10.10.0.0/16",
  "action": "DENY"
}' http://<vm1-ip-address>:8181/onos/v1/acl/rules
```

---

## 📃 10. Create Databases in Kubernetes MySQL Service

Connect to the MySQL service from `vm2`:

```bash
mysql -h <master-node-ip> -P <service-port> -u root -p
```

Password: `rootpass` (check `mysql.yaml`)

### 🔧 Create Databases

```sql
CREATE DATABASE db1;
CREATE DATABASE db2;
```

### 👥 Create Users

```sql
CREATE USER 'user1'@'%' IDENTIFIED BY 'password1';
CREATE USER 'user2'@'%' IDENTIFIED BY 'password2';
CREATE USER 'user3'@'%' IDENTIFIED BY 'password3';
```

### 🔐 Grant Permissions

```sql
GRANT ALL PRIVILEGES ON db1.* TO 'user1'@'%';
GRANT ALL PRIVILEGES ON db2.* TO 'user2'@'%';
GRANT ALL PRIVILEGES ON db2.* TO 'user3'@'%';
FLUSH PRIVILEGES;
```

---

## ✅ Final Notes

* Ensure each VM has proper networking to communicate.
* Use `kubectl get nodes` to verify Kubernetes cluster status.
* Use `docker ps` to verify running containers on `vm1`.
