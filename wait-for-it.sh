#!/bin/bash
# wait-for-it.sh: espera hasta que un servicio esté disponible
# Ejemplo de uso: wait-for-it.sh localhost:8000 -t 15

set -e

host="$1"
port="$2"
shift 2
cmd="$@"

until nc -z ${host} ${port}; do
  echo "Esperando por ${host} ..."
  sleep 1
done

echo "Servicio ${host} disponible"
exec $cmd
