from flask import Flask, jsonify, Response
from monitor import get_system_metrics

app = Flask(__name__)

@app.route("/metrics", methods=["GET"])
def metrics():
    """Expose Prometheus-formatted metrics."""
    data = get_system_metrics()
    prometheus_format = (
        f'# HELP cpu_percent CPU usage percent\n'
        f'# TYPE cpu_percent gauge\n'
        f'cpu_percent {data["cpu_percent"]}\n'
        f'# HELP memory_percent Memory usage percent\n'
        f'# TYPE memory_percent gauge\n'
        f'memory_percent {data["memory_percent"]}\n'
        f'# HELP disk_percent Disk usage percent\n'
        f'# TYPE disk_percent gauge\n'
        f'disk_percent {data["disk_percent"]}\n'
    )
    return Response(prometheus_format, mimetype="text/plain; version=0.0.4")

@app.route("/json", methods=["GET"])
def json_metrics():
    """Expose JSON metrics for manual inspection."""
    data = get_system_metrics()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
