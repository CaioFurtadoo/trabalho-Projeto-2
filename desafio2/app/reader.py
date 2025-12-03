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

def read_notes():
    conn = psycopg2.connect(host=PGHOST, user=PGUSER, password=PGPASSWORD, dbname=PGDATABASE)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT id, content, created_at FROM notes ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

if __name__ == "__main__":
    print("Reader iniciado. Lendo variáveis de ambiente...")
    wait_for_db()
    rows = read_notes()
    if not rows:
        print("Nenhuma nota encontrada.")
    else:
        print(f"TOTAL: {len(rows)} notas encontradas.")
        for r in rows:
            print(f"- id={r['id']} created_at={r['created_at']} content={r['content']}")
    print("Reader finalizado.")
