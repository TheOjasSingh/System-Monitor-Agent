import psutil
import time
import json

def get_system_metrics():
    """Collects current CPU, Memory, and Disk usage."""
    metrics = {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return metrics

def log_metrics(metrics, filename="system_metrics.log"):
    """Append metrics to log file."""
    with open(filename, "a") as f:
        f.write(json.dumps(metrics) + "\n")

if __name__ == "__main__":
    while True:
        data = get_system_metrics()
        log_metrics(data)
        print(f"Logged: {data}")
        time.sleep(5)  # every 5 seconds
