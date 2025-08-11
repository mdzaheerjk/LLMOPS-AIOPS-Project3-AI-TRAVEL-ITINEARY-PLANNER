# 🌍 LLMOps & AIOps Project 3: AI Travel Itinerary Planner

![LLMOps](https://img.shields.io/badge/LLMOps-AIOps-blueviolet)
![Python](https://img.shields.io/badge/Python-3.12%2B-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deploy-blue)
![Elastic Stack](https://img.shields.io/badge/ElasticStack-Logging%2FSearch-yellow)
![License](https://img.shields.io/badge/License-GPL--3.0-orange)

A next-generation, LLM-powered AI Travel Itinerary Planner. This project leverages modern LLMOps and AIOps best practices: modular pipeline, prompt chaining, observability with Elastic Stack (ELK), and scalable, cloud-native deployment with Docker and Kubernetes. Enter your preferences and get a smart, custom travel plan in seconds!

> 📁 **Repository:** `LLMOPS-AIOPS-Project3-AI-TRAVEL-ITINEARY-PLANNER`

---

## 🚀 Project Highlights

- ✈️ **AI Travel Planning:** Generate personalized travel itineraries using LLM chains and dynamic prompt engineering.
- 🔗 **Prompt Chaining:** Modular, extensible itinerary generation using custom chains.
- 📊 **Observability:** Full-stack logging and search with Elastic Stack (Elasticsearch, Logstash, Kibana, Filebeat).
- 🐳 **Dockerized:** Build, test, and run anywhere.
- ☸️ **Kubernetes-Ready:** Includes deployment manifests for scalable, cloud-native serving.
- 🛠️ **Config-Driven:** Flexible setup via Python config files.
- 📦 **Production Focus:** Clean code, robust structure, and ready for enterprise and research adaptation.

---

## 🧠 Technical Stack

- **Python 3.12+**
- **LLMs (Large Language Models)**
- **Prompt Chaining (custom modules)**
- **Elastic Stack (Elasticsearch, Logstash, Kibana, Filebeat)**
- **Docker, Kubernetes**
- **Modern Python OOP & Pipeline Patterns**

---

## 🏗️ Project Structure

```bash
LLMOPS-AIOPS-Project3-AI-TRAVEL-ITINEARY-PLANNER/
├── app.py                     # FastAPI/Flask app entry point
├── src/
│   ├── __init__.py
│   ├── chains/
│   │   ├── __init__.py
│   │   └── itinerary_chain.py    # Core itinerary LLM chain
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── planner.py           # Planning logic
│   └── utils/
│       └── __init__.py
├── elasticsearch.yaml          # Elasticsearch deployment manifest
├── kibana.yaml                 # Kibana dashboard manifest
├── logstash.yaml               # Logstash config/deployment
├── filebeat.yaml               # Filebeat config/deployment
├── k8s-deployment.yaml         # Main app Kubernetes manifest
├── Dockerfile
├── FULL DOCUMENTATION.md
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
```

---

## ⚡ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/mdzaheerjk/LLMOPS-AIOPS-Project3-AI-TRAVEL-ITINEARY-PLANNER.git
cd LLMOPS-AIOPS-Project3-AI-TRAVEL-ITINEARY-PLANNER
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```
Or build and run with Docker:
```bash
docker build -t travel-itinerary-ai .
docker run -p 8000:8000 travel-itinerary-ai
```

### 5. Kubernetes & Elastic Stack Deployment
Apply the manifests to your cluster:
```bash
kubectl apply -f elasticsearch.yaml
kubectl apply -f kibana.yaml
kubectl apply -f logstash.yaml
kubectl apply -f filebeat.yaml
kubectl apply -f k8s-deployment.yaml
```

---

## 📊 Observability & Monitoring

- **Elastic Stack (ELK):**
  - **Elasticsearch:** Stores logs and search data.
  - **Kibana:** Visualizes logs and provides dashboards.
  - **Logstash:** Centralized log processing.
  - **Filebeat:** Shipping app logs to Elastic Stack.

---

## 🧪 Example Usage

- **Custom Travel Itinerary:**  
  Input preferences (destinations, dates, interests) and get a full AI-generated trip plan.

- **Web/API Demo:**  
  Use the app via REST API or UI (if provided).

---

## 📚 Documentation

See [FULL DOCUMENTATION.md](FULL_DOCUMENTATION.md) for detailed architecture, code structure, and configuration instructions.

---

## ✍️ Author

**Mohammed Zaheeruddin**  
🎓 First-Year B.Tech Student | AI/ML & GenAI Enthusiast  
🏫 Shetty Institute of Technology, Gulbarga  
📧 info.zaheerjk@gmail.com

---

## 📜 License

This project is licensed under the **GPL-3.0 License** – see the LICENSE file for details.

---

#### Key Features:
1. LLM-powered, prompt-chained AI travel planner
2. Modular, extensible codebase with observability built-in (Elastic Stack)
3. Docker and Kubernetes ready for scalable production
4. Designed for research, education, and real-world applications
