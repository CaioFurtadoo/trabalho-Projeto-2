# Desafio 2 — Volumes e Persistência

## Objetivo
Demonstrar persistência de dados usando volumes Docker.  
Usamos PostgreSQL e um volume nomeado (`desafio2_postgres_data`) para garantir que os dados persistam mesmo depois de remover containers.

## Arquitetura da solução
- Serviço `db` — PostgreSQL (container oficial).
- Serviço `writer` — container Python que cria a tabela `notes` (se necessário) e insere uma nota.
- Serviço `reader` — container Python que lê e exibe todas as notas.

Todos os serviços estão conectados a uma rede Docker interna `desafio2-net`. O volume `postgres_data` (nomeado `desafio2_postgres_data`) armazena o diretório `/var/lib/postgresql/data`.

## Estrutura do projeto
desafio2/
├─ app/
│ ├─ Dockerfile
│ ├─ requirements.txt
│ ├─ writer.py
│ └─ reader.py
├─ docker-compose.yml
└─ README.md

## Como executar (passo a passo)
### Requisitos
- Docker instalado e rodando (Docker Desktop / Docker Engine).
- Terminal (Git Bash no Windows recomendado).

## Testes rápidos que você pode executar agora (resumo)
1. `docker compose up -d db`
2. `docker compose run --rm writer python writer.py`
3. `docker compose run --rm reader python reader.py` → confirma dados
4. `docker compose down`
5. `docker compose up -d db`
6. `docker compose run --rm reader python reader.py` → dados ainda aparecem