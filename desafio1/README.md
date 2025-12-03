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

## Decisões técnicas
- Usei Python + Flask no `server` para simplicidade e saída JSON clara.
- O `client` é um container pequeno baseado em Alpine que roda um loop com `curl`.
- Rede nomeada `desafio1-net` garante DNS interno (`server` resolvido pelo nome do serviço).

## Como executar (passo a passo)

### Pré-requisitos
- Docker instalado e em execução.
- (Opcional) Git para clonar o repositório.

### Executando com o script fornecido
1. Abra um terminal na pasta `desafio1`.
2. Torne o `run.sh` executável (no Windows Git Bash) e execute:
   ```bash
   ./run.sh
   ```

O script faz:
- cria a rede `desafio1-net` (se não existir)
- builda as imagens `desafio1-server` e `desafio1-client`
- inicia o container `server` expondo a porta `8080` para `localhost`
- inicia o container `client` conectado à mesma rede

### Executando manualmente (comandos equivalentes)
1. Criar a rede (caso necessário):
   ```bash
   docker network inspect desafio1-net >/dev/null 2>&1 || docker network create desafio1-net
   ```
2. Buildar as imagens:
   ```bash
   docker build -t desafio1-server ./server
   docker build -t desafio1-client ./client
   ```
3. Rodar o servidor:
   ```bash
   docker run -d --name server --network desafio1-net -p 8080:8080 desafio1-server
   ```
4. Rodar o client (em background):
   ```bash
   docker run -d --name client --network desafio1-net desafio1-client
   ```

## Como testar / demonstrar comunicação
- Acesse localmente o servidor:
  - `curl http://localhost:8080/` → deve retornar JSON com `message`, `timestamp`, `hostname`.
- Verifique o `client` fazendo requisições internas usando o nome DNS `server`:
  - `docker logs -f client` → verá saídas periódicas de `GET /` e `POST /echo`.
- No servidor, verifique logs:
  - `docker logs -f server` → verá requisições recebidas do `client`.

## Exemplo de comandos de verificação
```bash
# ver resposta HTTP do servidor
curl http://localhost:8080/

# ver logs do client (mostra as requests feitas internamente)
docker logs -f client

# ver logs do servidor
docker logs -f server
```

## Limpeza
```bash
docker rm -f server client || true
docker network rm desafio1-net || true
docker image rm desafio1-server desafio1-client || true
```

