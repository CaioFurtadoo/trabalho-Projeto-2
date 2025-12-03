
# Desafio 5 — Microsserviços com API Gateway

## Objetivo
Criar uma arquitetura com um API Gateway centralizando o acesso a dois microsserviços:
- `users-service`: fornece dados de usuários
- `orders-service`: fornece pedidos
- `gateway`: expõe endpoints `/users` e `/orders` e encaminha as requisições internamente

Todos os serviços rodam em containers e são orquestrados pelo `docker-compose.yml` da pasta.

## Arquitetura e decisões técnicas
- Linguagem: Python + Flask para serviços pequenos e claros.
- Comunicação interna: HTTP entre containers usando nomes de serviço do Docker Compose (`users-service`, `orders-service`).
- Gateway: faz proxy simples para os serviços e expõe uma porta única (`8000`) para o cliente.
- Isolamento: cada serviço tem seu próprio `Dockerfile` e ambiente, garantindo independência.

Fluxo de requisição (resumido):
1. Cliente -> `gateway` (http://localhost:8000/users ou /orders)
2. `gateway` faz `requests.get("http://users-service:5001/users")` ou `http://orders-service:5002/orders`
3. `gateway` retorna ao cliente a resposta JSON recebida do serviço alvo

## Estrutura do projeto
```
desafio5/
├─ docker-compose.yml
├─ gateway/
│  ├─ app.py
	├─ Dockerfile
	└─ requirements.txt
├─ users-service/
│  ├─ app.py
	├─ Dockerfile
	└─ requirements.txt
└─ orders-service/
	 ├─ app.py
	 ├─ Dockerfile
	 └─ requirements.txt
```

## Endpoints expostos
- `GET /users` (gateway) → proxied para `users-service` → responde lista de usuários JSON
- `GET /orders` (gateway) → proxied para `orders-service` → responde lista de pedidos JSON

Observação: `users-service` e `orders-service` escutam internamente nas portas `5001` e `5002`, respectivamente — essas portas não são mapeadas para o host. O único ponto de entrada para o usuário é o `gateway` na porta `8000`.

## Como executar (passo a passo)

### Pré-requisitos
- Docker instalado e em execução (Docker Desktop / Engine)

### Subir a stack
Abra um terminal na pasta `desafio5` e execute:

```powershell
cd C:\Users\Caio\Desktop\trabalho\desafio5
docker compose up --build -d
```

Com isso o Compose irá construir as imagens e iniciar os 3 containers na rede interna `desafio5`.

### Validar que os serviços estão rodando

```powershell
docker compose ps
```

Deve mostrar `gateway`, `users-service` e `orders-service` como `Up`.

### Testar os endpoints via gateway (exemplos)

```powershell
# Lista de usuários (via gateway)
curl http://localhost:8000/users

# Lista de pedidos (via gateway)
curl http://localhost:8000/orders
```

Exemplo de resposta esperada para `/users`:

```json
[
	{"id":1,"name":"Caio"},
	{"id":2,"name":"Mariana"}
]
```

Exemplo de resposta esperada para `/orders`:

```json
[
	{"id":10,"user_id":1,"total":150.9},
	{"id":11,"user_id":2,"total":89.3}
]
```

### Ver logs (debug / demonstração)

```powershell
# ver logs do gateway
docker compose logs -f gateway

# ver logs dos serviços
docker compose logs -f users-service
docker compose logs -f orders-service
```

### Parar e limpar

```powershell
docker compose down
```