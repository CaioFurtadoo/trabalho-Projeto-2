#!/usr/bin/env python3
import os
import time
import psycopg2
from psycopg2.extras import RealDictCursor

PGHOST = os.environ.get("PGHOST", "db")
PGUSER = os.environ.get("PGUSER", "user")
PGPASSWORD = os.environ.get("PGPASSWORD", "pass")
PGDATABASE = os.environ.get("PGDATABASE", "desafio2")
PGPORT = int(os.environ.get("PGPORT", 5432))

def wait_for_db(max_wait=30):
    start = time.time()
    while True:
        try:
            conn = psycopg2.connect(host=PGHOST, user=PGUSER, password=PGPASSWORD, dbname=PGDATABASE, port=PGPORT)
            conn.close()
            print("Conexão com o DB estabelecida.")
            return
        except Exception as e:
            if time.time() - start > max_wait:
                raise
            print("DB não disponível ainda, esperando 1s...")
            time.sleep(1)

def ensure_table():
    conn = psycopg2.connect(host=PGHOST, user=PGUSER, password=PGPASSWORD, dbname=PGDATABASE)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id SERIAL PRIMARY KEY,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Tabela 'notes' garantida.")

def insert_note(content):
    conn = psycopg2.connect(host=PGHOST, user=PGUSER, password=PGPASSWORD, dbname=PGDATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO notes (content) VALUES (%s) RETURNING id, created_at;", (content,))
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    print(f"Nota inserida: id={row[0]}, created_at={row[1]}")

if __name__ == "__main__":
    print("Writer iniciado. Lendo variáveis de ambiente...")
    wait_for_db()
    ensure_table()
    insert_note(f"Nota inserida pelo writer em {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("Writer finalizado.")
