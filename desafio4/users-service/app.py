from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/users")
def get_users():
    users = [
        {"id": 1, "name": "Caio", "active_since": "2022-01-10"},
        {"id": 2, "name": "Mariana", "active_since": "2023-05-01"},
        {"id": 3, "name": "Pedro", "active_since": "2024-02-20"},
    ]
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
