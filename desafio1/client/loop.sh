#!/bin/bash 

TARGET="${TARGET:-http://server:8080}" 
INTERVAL_SECONDS="${INTERVAL_SECONDS:-3}"

echo "Iniciando client. Alvo: $TARGET. Intervalo: ${INTERVAL_SECONDS}s"

while true; do
  echo "==== $(date -u +"%Y-%m-%dT%H:%M:%SZ") - GET /"
  curl -s -w "\nHTTP_STATUS:%{http_code}\n" "${TARGET}/"
  echo
  echo "==== $(date -u +"%Y-%m-%dT%H:%M:%SZ") - POST /echo"
  curl -s -H "Content-Type: application/json" -X POST -d '{"from":"client","ts":"'"$(date -u +"%Y-%m-%dT%H:%M:%SZ")"'"}' -w "\nHTTP_STATUS:%{http_code}\n" "${TARGET}/echo"
  echo
  sleep "${INTERVAL_SECONDS}"
done
