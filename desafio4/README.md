Desafio 4 — Microsserviços Independentes
📌 Descrição da Solução

Neste desafio foram desenvolvidos dois microsserviços totalmente independentes, cada um com seu próprio Dockerfile e execução isolada. Eles se comunicam via HTTP, utilizando nomes DNS internos da rede Docker criada automaticamente pelo Docker Compose.

Os serviços são:

🟦 Microsserviço A — Users Service

Responsável por fornecer uma lista de usuários em formato JSON.
Ele responde no endpoint:

GET /users

🟩 Microsserviço B — Consumer Service

Consome o serviço A, processa os dados recebidos e retorna informações combinadas.
Endpoint:

GET /combined


Este serviço faz uma requisição interna para:

http://users-service:8080/users


E devolve frases como:

Usuário Caio ativo desde 2022-01-10

🧱 Arquitetura e Fluxo
flowchart LR
    A[Users Service<br>Flask API<br>porta 8080] <-- HTTP --> B[Consumer Service<br>Flask API<br>porta 9090]
    
    subgraph Docker Network
        A
        B
    end

Explicação do fluxo:

O Users Service expõe um endpoint com uma lista fixa de usuários.

O Consumer Service faz uma chamada HTTP interna usando DNS Docker (http://users-service:8080).

Ele processa os dados e devolve uma representação textual dos usuários.

Ambos os serviços rodam isolados em containers separados.

🗂 Estrutura do Projeto
desafio4/
│
├── users-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── consumer-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md

🐳 Dockerfiles
📘 Users Service — users-service/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]

📗 Consumer Service — consumer-service/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 9090

CMD ["python", "app.py"]

⚙️ docker-compose.yml
version: "3.9"

services:
  users-service:
    build: ./users-service
    container_name: users-service
    ports:
      - "8080:8080"
    networks:
      - desafio4-net

  consumer-service:
    build: ./consumer-service
    container_name: consumer-service
    ports:
      - "9090:9090"
    depends_on:
      - users-service
    networks:
      - desafio4-net

networks:
  desafio4-net:
    driver: bridge

▶️ Como Executar o Projeto
1. Entrar na pasta do desafio
cd desafio4

2. Subir os serviços
docker compose up --build -d

3. Testar os serviços
🔵 Users Service
curl http://localhost:8080/users


Retorno esperado:

[
  {"id":1,"name":"Caio","active_since":"2022-01-10"},
  {"id":2,"name":"Mariana","active_since":"2023-05-01"},
  {"id":3,"name":"Pedro","active_since":"2024-02-20"}
]

🟢 Consumer Service
curl http://localhost:9090/combined


Retorno esperado:

{
  "details": [
    "Usuário Caio ativo desde 2022-01-10",
    "Usuário Mariana ativo desde 2023-05-01",
    "Usuário Pedro ativo desde 2024-02-20"
  ]
}

🧪 Testando a Comunicação Interna

Dentro de qualquer container, o DNS funciona automaticamente:

docker exec -it consumer-service sh
curl http://users-service:8080/users


Se a resposta aparecer, significa que:

✔ Rede configurada
✔ DNS interno funcionando
✔ Comunicação entre microsserviços OK

📌 Decisões Técnicas

Python + Flask pela simplicidade e clareza para APIs pequenas.

Rede interna do Compose para comunicação sem expor portas extras.

Dockerfiles separados garantindo isolamento e independência.

Compose gerenciando build, rede e dependências.

Comunicação feita diretamente via HTTP, sem gateway (como pedido no desafio).

🎯 Conclusão

O desafio cumpre todos os requisitos:

✔ Microsserviços independentes
✔ Comunicação via HTTP
✔ Dockerfiles separados
✔ Compose funcional
✔ Explicação clara da arquitetura
✔ Código simples e original