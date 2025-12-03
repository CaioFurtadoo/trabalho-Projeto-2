🧩 Desafio 5 — Sistema de Fila com Redis (Producer/Consumer)
📌 Descrição da Solução

Este desafio implementa um sistema simples baseado em fila de mensagens, utilizando Redis como broker.
O sistema possui dois containers principais:

producer → Envia mensagens para uma fila chamada queue:messages.

consumer → Lê continuamente a fila e processa cada mensagem.

A comunicação é feita pela rede Docker interna, e os serviços são orquestrados via Docker Compose.

📁 Estrutura de Arquivos
desafio5/
│
├── producer/
│   ├── producer.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── consumer/
│   ├── consumer.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md

🚀 Como funciona cada componente
✔️ Redis

Servidor principal de mensagens.

Contém a fila queue:messages.

✔️ Producer

Envia mensagens para Redis usando o comando:

r.lpush("queue:messages", mensagem)


O producer cria uma mensagem com timestamp e envia para a fila.

✔️ Consumer

Consome mensagens continuamente via:

r.brpop("queue:messages")


Cada mensagem retirada da fila é exibida no terminal, simulando um processamento.

▶️ Como Executar
1. Subir toda a stack
docker compose up -d


Isso iniciará:

redis

consumer

OBS: o producer não roda automaticamente para permitir execuções manuais.

2. Executar o producer (enviar uma mensagem)
docker compose run --rm producer


Exemplo de saída:

Producer iniciado.
Mensagem enviada: "Olá do producer! - 2025-12-01 15:42:00"
Producer finalizado.

3. Visualizar o consumer processando

O consumer roda automaticamente em background.

Para ver logs:

docker compose logs -f consumer


Exemplo:

Consumer iniciado. Aguardando mensagens...
Mensagem recebida: "Olá do producer! - 2025-12-01 15:42:00"

🛑 Parar tudo
docker compose down -v


Remove containers, rede e volumes.

🔧 Serviços (docker-compose.yml)
services:
  redis:
    image: redis:7
    container_name: redis
    networks:
      - desafio5-net

  producer:
    build: ./producer
    networks:
      - desafio5-net
    depends_on:
      - redis

  consumer:
    build: ./consumer
    networks:
      - desafio5-net
    depends_on:
      - redis

networks:
  desafio5-net:
    driver: bridge

💬 Exemplo do Producer (producer.py)
import redis
from datetime import datetime
import time

r = redis.Redis(host="redis", port=6379)

print("Producer iniciado.")

msg = f"Mensagem gerada em {datetime.now()}"
r.lpush("queue:messages", msg)

print(f"Mensagem enviada: {msg}")
print("Producer finalizado.")

🔄 Exemplo do Consumer (consumer.py)
import redis

r = redis.Redis(host="redis", port=6379)

print("Consumer iniciado. Aguardando mensagens...")

while True:
    _, msg = r.brpop("queue:messages")
    print(f"Mensagem recebida: {msg.decode()}")

✅ Resultado Esperado

Ao rodar o producer, o consumer deve automaticamente processar a mensagem, demonstrando:

comunicação entre containers

uso real de uma fila

persistência temporária de mensagens

fluxo producer → broker → consumer