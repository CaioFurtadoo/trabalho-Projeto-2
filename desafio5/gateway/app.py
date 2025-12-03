from flask import Flask, jsonify
import requests

app = Flask(__name__)

USERS_URL = "http://users-service:5001/users"
ORDERS_URL = "http://orders-service:5002/orders"

@app.route("/users")
def proxy_users():
    response = requests.get(USERS_URL)
    return jsonify(response.json())

@app.route("/orders")
def proxy_orders():
    response = requests.get(ORDERS_URL)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)