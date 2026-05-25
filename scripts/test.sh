#!/usr/bin/env bash
set -euo pipefail
PORT="${WEB_PORT:-8095}"
python3 -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:${PORT}', timeout=10).read().decode().strip())"
docker compose exec -T web python -c "import socket; print('db_dns=' + socket.gethostbyname('db')); print('cache_dns=' + socket.gethostbyname('cache'))" 2>/dev/null || docker-compose exec -T web python -c "import socket; print('db_dns=' + socket.gethostbyname('db')); print('cache_dns=' + socket.gethostbyname('cache'))"
