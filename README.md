# Trabalhos - Desafios Docker e Microsserviços

Repositório contendo as entregas individuais dos desafios propostos no curso.

Conteúdo:
- `desafio1/` — Containers em Rede (server Flask + client em loop)
- `desafio2/` — Volumes e Persistência (Postgres + writer/reader)
- `desafio3/` — Docker Compose Orquestrando Serviços (web, db, cache)
- `desafio4/` — Microsserviços Independentes (users-service + consumer-service)
- `desafio5/` — Microsserviços / Gateway ou fila (implementação específica por pasta)

**Descrição geral**

Cada pasta `desafioN` contém sua solução completa (código, `Dockerfile`, `docker-compose.yml` quando aplicável e `README.md` específico). Os READMEs de cada desafio trazem:
- descrição da solução e decisões técnicas;
- explicação de arquitetura e fluxos (containers, redes, volumes, endpoints);
- instruções passo a passo para executar e testar localmente;
- comandos úteis para demonstrar persistência, comunicação e limpeza.

### Como usar este repositório

Pré-requisitos:
- Docker instalado e em execução (Docker Desktop / Engine).
- Docker Compose disponível (na versão do Docker Desktop ou `docker compose`).

Executar um desafio (exemplo):

1. Entre na pasta do desafio que deseja testar:
   ```powershell
   cd desafio1
   ```
2. Siga as instruções do `desafioX/README.md` correspondente. Cada README contém comandos práticos como `docker build`, `docker run`, `docker compose up` e verificações de logs.

Observações por desafio (resumo rápido):
- `desafio1`: rede Docker nomeada, server Flask na porta `8080`, client em loop mostrando comunicação via DNS interno.
- `desafio2`: demonstra volumes e persistência com Postgres e containers `writer`/`reader` para inserir/ler dados.
- `desafio3`: docker-compose com `web` (Flask), `db` (Postgres) e `cache` (Redis) demonstrando orquestração e `depends_on`.
- `desafio4`: dois microsserviços independentes (Users e Consumer) comunicando via HTTP; cada serviço tem Dockerfile próprio.
- `desafio5`: implementação disponível na pasta; favor checar o `desafio5/README.md` para instruções específicas (pode ser Gateway ou outra arquitetura implementada).