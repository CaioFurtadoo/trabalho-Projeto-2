# Desafio 3 — Docker Compose Orquestrando Serviços

## Objetivo
Orquestrar 3 serviços com Docker Compose: `web` (Flask), `db` (Postgres) e `cache` (Redis).  
Demonstrar dependências, variáveis de ambiente, rede interna e comunicação entre serviços.

---

## Arquitetura
- `db` (Postgres): armazena tabela `items` (inicializada por `db/init.sql`).
- `cache` (Redis): armazena JSON serializado com TTL para acelerar leitura.
- `web` (Flask): expõe endpoints `/items`, `/items/refresh` e `/health`.
  - `/items` tenta ler do Redis; se não existir, consulta Postgres e popula cache.
  - `/items/refresh` força refresh do cache.

Rede: todos os serviços ficam na rede interna `desafio3-net`. O `web` se conecta a `db` e `cache` via seus nomes de serviço.

---

## Estrutura de arquivos

desafio3/
├─ web/
│ ├─ app.py
│ ├─ Dockerfile
│ └─ requirements.txt
├─ db/
│ └─ init.sql
├─ docker-compose.yml
└─ README.md

---

## Como executar (passo a passo)

### Requisitos
- Docker e Docker Compose (Docker Desktop ou Docker Engine).
- Terminal (Git Bash recomendado no Windows).

### 1) Subir todos os serviços e rodar no gitbash
```bash
cd desafio3
docker compose up -d
docker ps
docker compose ps
curl http://localhost:5000/items
curl http://localhost:5000/items/refresh
curl http://localhost:5000/health
docker logs -f desafio3_web
docker logs -f desafio3_db