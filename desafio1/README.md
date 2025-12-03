# Desafio 1 — Containers em Rede

## Descrição da solução
Implementei dois containers conectados a uma rede Docker nomeada `desafio1-net`:
- **server**: aplicação Flask servindo endpoints em `0.0.0.0:8080`.
  - Endpoints: `GET /` e `POST /echo`.
- **client**: container Alpine que executa `loop.sh`, um script que periodicamente faz:
  - `GET /`
  - `POST /echo` com JSON

A comunicação é feita via DNS interno do Docker: o client usa `http://server:8080`.

## Arquivos
- `server/`
  - `server.py` — servidor Flask
  - `requirements.txt`
  - `Dockerfile`
- `client/`
  - `loop.sh` — script com `curl`
  - `Dockerfile`
- `run.sh` — script que cria rede, builda imagens e executa containers
- `README.md` — este arquivo

## Como executar (passo a passo)
1. Clone o repositório e entre em `desafio1`:
   ```bash
   git clone <seu-repo>
   cd desafio1
