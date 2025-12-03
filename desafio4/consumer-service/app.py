from flask import Flask
import requests
import os

app = Flask(__name__)

USERS_SERVICE_URL = os.getenv("USERS_SERVICE_URL", "http://users-service:8080/users")

@app.get("/combined")
def combined():
    try:
        response = requests.get(USERS_SERVICE_URL, timeout=3)
        users = response.json()
    except Exception as e:
        return {"error": f"Erro ao consultar Users Service: {str(e)}"}, 500

    output = []
    for u in users:
        output.append(f"Usuário {u['name']} ativo desde {u['active_since']}")

    return {"details": output}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)
