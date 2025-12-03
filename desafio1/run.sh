set -e

NETWORK_NAME="desafio1-net"
SERVER_NAME="server"
CLIENT_NAME="client"

echo "Criando rede docker: $NETWORK_NAME (se ainda não existir)"
docker network inspect $NETWORK_NAME >/dev/null 2>&1 || docker network create $NETWORK_NAME

echo "Construindo imagens..."
docker build -t desafio1-server ./server
docker build -t desafio1-client ./client

docker rm -f $SERVER_NAME >/dev/null 2>&1 || true
docker rm -f $CLIENT_NAME >/dev/null 2>&1 || true

echo "Iniciando container do servidor (nome: $SERVER_NAME)..."
docker run -d --name $SERVER_NAME --network $NETWORK_NAME -p 8080:8080 desafio1-server

echo "Iniciando container do cliente (nome: $CLIENT_NAME)..."
docker run -d --name $CLIENT_NAME --network $NETWORK_NAME desafio1-client

echo "Pronto!"
echo "Servidor exposto em http://localhost:8080 (mapeado pela porta)."
echo "Logs do servidor: docker logs -f $SERVER_NAME"
echo "Logs do client: docker logs -f $CLIENT_NAME"
