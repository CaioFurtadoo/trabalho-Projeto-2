from flask import Flask, jsonify
import os
import json
import time
import psycopg2
from psycopg2.extras import RealDictCursor
import redis

app = Flask(__name__)

# Config via env
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_USER = os.getenv("DB_USER", "demo")
DB_PASS = os.getenv("DB_PASS", "demo_pass")
DB_NAME = os.getenv("DB_NAME", "demo_db")

REDIS_HOST = os.getenv("REDIS_HOST", "cache")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
CACHE_TTL = int(os.getenv("CACHE_TTL", 30))  # segundos

# Conexão redis (padrão: tentativa simples)
cache = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT,
        user=DB_USER, password=DB_PASS, dbname=DB_NAME
    )
    return conn

def fetch_items_from_db():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT id, name, description FROM items ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/items")
def items():
    # tenta ler do cache
    cached = cache.get("items")
    if cached:
        source = "cache"
        items = json.loads(cached)
    else:
        source = "db"
        items = fetch_items_from_db()
        cache.set("items", json.dumps(items), ex=CACHE_TTL)
    return jsonify({"source": source, "count": len(items), "items": items})

@app.route("/items/refresh")
def refresh():
    items = fetch_items_from_db()
    cache.set("items", json.dumps(items), ex=CACHE_TTL)
    return jsonify({"msg": "cache refreshed", "count": len(items)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
