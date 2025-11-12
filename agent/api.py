from flask import Flask, jsonify
from monitor import get_system_metrics

app = Flask(__name__)

@app.route("/metrics", methods=["GET"])
def metrics():
    data = get_system_metrics()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
