from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orders")
def get_orders():
    data = [
        {"id": 10, "user_id": 1, "total": 150.90},
        {"id": 11, "user_id": 2, "total": 89.30},
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
