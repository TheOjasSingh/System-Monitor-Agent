# 🧠 System Monitoring Agent

A lightweight, containerized Python-based agent that monitors **CPU, Memory, and Disk usage** in real-time.  
It exposes metrics through a **REST API** and can be integrated with **Prometheus** and **Grafana** for monitoring and visualization.

---

## 🚀 Features
- 🔍 Monitors system CPU, memory, and disk usage
- 🌐 Exposes metrics at `/metrics` endpoint via Flask API
- 🪶 Lightweight and containerized using Docker
- ⚙️ Ready for CI/CD integration with GitHub Actions
- 📊 Compatible with Prometheus and Grafana

---

## 🧩 Project Structure
```
system-monitor-agent/
├── agent/
│   ├── __init__.py
│   ├── monitor.py         # Collects system metrics
│   └── api.py             # Exposes metrics API
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container setup
├── README.md              # Documentation
```

---

## ⚙️ Setup Instructions

### **1. Clone the Repository**
```bash
git clone https://github.com/<your-username>/system-monitor-agent.git
cd system-monitor-agent
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the Agent Locally**
```bash
python agent/api.py
```

Now visit 👉 [http://localhost:8080/metrics](http://localhost:8080/metrics)

You’ll see:
```json
{
  "cpu_percent": 12.3,
  "memory_percent": 46.1,
  "disk_percent": 30.5,
  "timestamp": "2025-11-12 10:00:00"
}
```

---

## 🐳 Run with Docker

### **1. Build Docker Image**
```bash
docker build -t system-monitor-agent .
```

### **2. Run Container**
```bash
docker run -d -p 8080:8080 system-monitor-agent
```

### **3. Access Metrics**
Visit:
```
http://localhost:8080/metrics
```

---

## ⚡ CI/CD Integration (GitHub Actions)
You can automate Docker builds using GitHub Actions.  
The workflow will:
- Build and test the project
- Push the image to Docker Hub (or GHCR)

> Workflow file: `.github/workflows/deploy.yml`

*(to be added in the next step)*

---

## 📈 Monitoring with Prometheus & Grafana
Once containerized, you can easily monitor metrics using:
- **Prometheus** → scrapes data from `/metrics`
- **Grafana** → visualizes usage trends over time

---

## 🧰 Tech Stack
- **Language:** Python 3.10
- **Framework:** Flask
- **Monitoring:** Prometheus, Grafana
- **Containerization:** Docker
- **CI/CD:** GitHub Actions

---

## 🧑‍💻 Author
**Ojas Singh**  
DevOps & AI Enthusiast 🚀  
📫 [Your Email or LinkedIn]

---

## 📜 License
This project is licensed under the MIT License.
