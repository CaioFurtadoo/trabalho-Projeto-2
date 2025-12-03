from flask import Flask, request, jsonify
from datetime import datetime
import socket

app = Flask(__name__)
HOSTNAME = socket.gethostname()

@app.route("/")
def index():
    now = datetime.utcnow().isoformat() + "Z"
    return jsonify({
        "message": "Servidor ativo",
        "timestamp": now,
        "hostname": HOSTNAME
    })

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json or {}
    now = datetime.utcnow().isoformat() + "Z"
    return jsonify({
        "received": data,
        "timestamp": now,
        "hostname": HOSTNAME
    })

if __name__ == "__main__":
    # roda o Flask na porta 8080, acessível de outras máquinas/containers
    app.run(host="0.0.0.0", port=8080)
