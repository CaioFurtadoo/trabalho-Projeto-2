from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def get_users():
    data = [
        {"id": 1, "name": "Caio"},
        {"id": 2, "name": "Mariana"},
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
