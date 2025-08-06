### 1. Initial Setup

- **Push code to GitHub**  
  Push your project code to a GitHub repository.

- **Create a Dockerfile**  
  Write a `Dockerfile` in the root of your project to containerize the app.

- **Create Kubernetes Deployemtn file**  
  Make a file named 'llmops-k8s.yaml' 

- **Create a VM Instance on Google Cloud**

  - Go to VM Instances and click **"Create Instance"**
  - Name: ``
  - Machine Type:
    - Series: `E2`
    - Preset: `Standard`
    - Memory: `16 GB RAM`
  - Boot Disk:
    - Change size to `256 GB`
    - Image: Select **Ubuntu 24.04 LTS**
  - Networking:
    - Enable HTTP and HTTPS traffic

- **Create the Instance**

- **Connect to the VM**
  - Use the **SSH** option provided to connect to the VM from the browser.



### 2. Configure VM Instance

- **Clone your GitHub repo**

  ```bash
  git clone https://github.com/data-guru0/TESTING-9.git
  ls
  cd TESTING-9
  ls  # You should see the contents of your project
  ```

- **Install Docker**

  - Search: "Install Docker on Ubuntu"
  - Open the first official Docker website (docs.docker.com)
  - Scroll down and copy the **first big command block** and paste into your VM terminal
  - Then copy and paste the **second command block**
  - Then run the **third command** to test Docker:

    ```bash
    docker run hello-world
    ```

- **Run Docker without sudo**

  - On the same page, scroll to: **"Post-installation steps for Linux"**
  - Paste all 4 commands one by one to allow Docker without `sudo`
  - Last command is for testing

- **Enable Docker to start on boot**

  - On the same page, scroll down to: **"Configure Docker to start on boot"**
  - Copy and paste the command block (2 commands):

    ```bash
    sudo systemctl enable docker.service
    sudo systemctl enable containerd.service
    ```

- **Verify Docker Setup**

  ```bash
  systemctl status docker       # You should see "active (running)"
  docker ps                     # No container should be running
  docker ps -a                 # Should show "hello-world" exited container
  ```


### 3. Configure Minikube inside VM

- **Install Minikube**

  - Open browser and search: `Install Minikube`
  - Open the first official site (minikube.sigs.k8s.io) with `minikube start` on it
  - Choose:
    - **OS:** Linux
    - **Architecture:** *x86*
    - Select **Binary download**
  - Reminder: You have already done this on Windows, so you're familiar with how Minikube works

- **Install Minikube Binary on VM**

  - Copy and paste the installation commands from the website into your VM terminal

- **Start Minikube Cluster**

  ```bash
  minikube start
  ```

  - This uses Docker internally, which is why Docker was installed first

- **Install kubectl**

  - Search: `Install kubectl`
  - Run the first command with `curl` from the official Kubernetes docs
  - Run the second command to validate the download
  - Instead of installing manually, go to the **Snap section** (below on the same page)

  ```bash
  sudo snap install kubectl --classic
  ```

  - Verify installation:

    ```bash
    kubectl version --client
    ```

- **Check Minikube Status**

  ```bash
  minikube status         # Should show all components running
  kubectl get nodes       # Should show minikube node
  kubectl cluster-info    # Cluster info
  docker ps               # Minikube container should be running
  ```

### 4. Interlink your Github on VSCode and on VM

```bash
git config --global user.email "gyrogodnon@gmail.com"
git config --global user.name "data-guru0"

git add .
git commit -m "commit"
git push origin main
```

- When prompted:
  - **Username**: `data-guru0`
  - **Password**: GitHub token (paste, it's invisible)

---


### 5. Build and Deploy your APP on VM

```bash
## Point Docker to Minikube
eval $(minikube docker-env)

docker build -t streamlit-app:latest .

kubectl create secret generic llmops-secrets \
  --from-literal=GROQ_API_KEY="" 

kubectl apply -f k8s-deployment.yaml


kubectl get pods

### U will see pods runiing


kubectl port-forward svc/streamlit-service 8501:80 --address 0.0.0.0

## Now copy external ip and :5000 and see ur app there....

```

# ✅ ELK Stack Setup on Kubernetes with Filebeat - Step-by-Step Guide

---

## 🚀 Step 1: Create a Namespace for Logging

```bash
kubectl create namespace logging
```
➡️ *This creates an isolated Kubernetes namespace called `logging` to keep all ELK components organized.*

---

## 📦 Step 2: Deploy Elasticsearch

```bash
kubectl apply -f elasticsearch.yaml
```
➡️ *Applies your Elasticsearch deployment configuration.*

```bash
kubectl get pods -n logging
```
➡️ *Checks if Elasticsearch pods are up and running.*

```bash
kubectl get pvc -n logging
```
➡️ *Checks PersistentVolumeClaims — these should be in `Bound` state (storage is allocated).*

```bash
kubectl get pv -n logging
```
➡️ *Checks PersistentVolumes — these too should show `Bound` to confirm the storage is working.*

✅ **Elasticsearch setup done...**

---

## 🌐 Step 3: Deploy Kibana

```bash
kubectl apply -f kibana.yaml
```
➡️ *Deploys Kibana, the frontend for Elasticsearch.*

```bash
kubectl get pods -n logging
```
➡️ *Wait until the Kibana pod is in `Running` state (might take a few minutes).*

```bash
kubectl port-forward -n logging svc/kibana 5601:5601 --address 0.0.0.0
```
➡️ *This makes Kibana accessible at `http://<your-ip>:5601`.*

✅ **Kibana setup done...**

---

## 🔄 Step 4: Deploy Logstash

```bash
kubectl apply -f logstash.yaml
```
➡️ *Deploys Logstash to process and forward logs.*

```bash
kubectl get pods -n logging
```
➡️ *Ensure Logstash is running.*

✅ **Logstash setup done...**

---

## 📤 Step 5: Deploy Filebeat

```bash
kubectl apply -f filebeat.yaml
```
➡️ *Deploys Filebeat to collect logs from all pods/nodes and send to Logstash.*

```bash
kubectl get all -n logging
```
➡️ *Checks all resources (pods, services, etc.) to confirm everything is running.*

✅ **Filebeat setup done...**

---

## 📊 Step 6: Setup Index Patterns in Kibana

1. Open Kibana in browser → `http://<your-ip>:5601`
2. Click **"Explore on my own"**
3. Go to **Stack Management** from the left panel
4. Click **Index Patterns**
5. Create new index pattern:
   - Pattern name: `filebeat-*`
   - Timestamp field: `@timestamp`
6. Click **Create Index Pattern**

➡️ *This tells Kibana how to search and filter logs coming from Filebeat.*

---

## 🔍 Step 7: Explore Logs

1. In the left panel, click **"Analytics → Discover"**
2. You will see logs collected from Kubernetes cluster!
3. Use filters like:
   - `kubernetes.container.name` to filter logs from specific pods like Filebeat, Kibana, Logstash, etc.

✅ **Done! Now you can monitor and analyze your K8s logs using ELK + Filebeat. 🎉**

---

