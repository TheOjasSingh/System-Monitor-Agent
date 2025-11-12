# 🧠 System Monitoring Agent with Prometheus & Grafana

A lightweight **System Monitoring Agent** built using **Python** and **Flask** to monitor **CPU**, **memory**, and **disk usage** in real-time.  
It integrates seamlessly with **Prometheus** for metrics collection and **Grafana** for live visualization — demonstrating a complete **DevOps monitoring pipeline**.

---

## 🚀 Features

- 🧩 Collects real-time CPU, Memory, and Disk usage
- 🌐 REST API endpoint `/metrics` for Prometheus scraping
- 🐳 Fully containerized using Docker
- ⚙️ Automated orchestration via Docker Compose
- 📊 Real-time dashboards in Grafana
- 🔔 Supports alerting for high system load (optional)

---

## 🧱 Architecture

```
┌────────────────────┐      ┌────────────────────┐      ┌────────────────────┐
│ System Monitor API │ ---> │ Prometheus         │ ---> │ Grafana Dashboard  │
│ (localhost:8080)   │      │ (localhost:9090)   │      │ (localhost:3000)   │
└────────────────────┘      └────────────────────┘      └────────────────────┘
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/system-monitor-agent.git
cd system-monitor-agent
```

---

### 2️⃣ Build & Run the Project

Run all containers with one command using Docker Compose:

```bash
docker compose up -d
```

✅ This will start:
- The **Monitoring Agent** (Flask API)
- **Prometheus** (Metrics collector)
- **Grafana** (Dashboard visualizer)

---

### 3️⃣ Access Services

| Service | URL | Description |
|----------|-----|-------------|
| 🧠 Agent | [http://localhost:8080/metrics](http://localhost:8080/metrics) | Returns live system metrics |
| 📡 Prometheus | [http://localhost:9090](http://localhost:9090) | Scrapes and stores metrics |
| 📈 Grafana | [http://localhost:3000](http://localhost:3000) | Displays dashboards |

To stop everything:
```bash
docker compose down
```

---

## 🧠 Example Output (API Response)

```json
{
  "cpu_percent": 8.3,
  "memory_percent": 47.1,
  "disk_percent": 33.8,
  "timestamp": "2025-11-12 14:30:21"
}
```

---

## 📊 Prometheus Output Example

When visiting [http://localhost:9090](http://localhost:9090), you’ll see metrics like:

```
# HELP cpu_percent CPU usage percentage
# TYPE cpu_percent gauge
cpu_percent 8.3
# HELP memory_percent Memory usage percentage
# TYPE memory_percent gauge
memory_percent 47.1
# HELP disk_percent Disk usage percentage
# TYPE disk_percent gauge
disk_percent 33.8
```

---

## 📈 Grafana Dashboard Setup

1. Go to [http://localhost:3000](http://localhost:3000)
   - Username: `admin`
   - Password: `admin`
2. Add a **new Data Source**
   - Type: Prometheus  
   - URL: `http://prometheus:9090`
3. Create a new **Dashboard**
   - Add panels for:
     - `cpu_percent`
     - `memory_percent`
     - `disk_percent`
4. Choose visualization: *Graph / Gauge / Time series*  
5. Save your dashboard 🎨

---

## 🧾 File Structure

```
system-monitor-agent/
├── agent/
│   ├── monitor.py
│   └── api.py
├── monitoring/
│   └── prometheus.yml
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── ci-cd.yml
```

---

## 🧰 Tech Stack

| Layer | Technology |
|--------|-------------|
| Metrics Agent | Python (Flask, psutil) |
| Monitoring | Prometheus |
| Visualization | Grafana |
| Containerization | Docker & Docker Compose |
| CI/CD Automation | GitHub Actions |

---

## 🧩 CI/CD Pipeline (GitHub Actions)

Every time you push to `main`, GitHub Actions:
1. Builds your Docker image  
2. Pushes it to Docker Hub  
3. Ensures reproducible deployment  

This pipeline runs automatically using `.github/workflows/ci-cd.yml`.

---

## 🧠 Learning Outcomes

- Build and expose metrics with Flask  
- Containerize apps with Docker  
- Automate builds with GitHub Actions  
- Monitor metrics via Prometheus  
- Visualize trends with Grafana  
- Deploy and manage microservices locally  

---

## 💡 Future Improvements

- 🔔 Add Slack or Email alerting when CPU > 80%  
- 📤 Push metrics to InfluxDB for historical analysis  
- 🧠 Add anomaly detection using ML models  

---

## 👨‍💻 Author

**Ojas Singh**  
DevOps | AI | Backend Systems Engineer  
📫 [LinkedIn](https://www.linkedin.com) | [GitHub](https://github.com)

---

## 🪶 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.
