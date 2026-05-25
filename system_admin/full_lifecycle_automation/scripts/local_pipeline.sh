#!/usr/bin/env bash
set -euo pipefail
if docker compose version >/dev/null 2>&1; then COMPOSE="docker compose"; else COMPOSE="docker-compose"; fi
python3 -m py_compile app/web/app.py app/worker/app.py app/db/app.py app/cache/app.py app/tests/e2e_check.py
$COMPOSE --env-file .env -f docker-compose.yml build
$COMPOSE -p full_local --env-file .env -f docker-compose.yml up -d --build
sleep 5
python3 app/tests/e2e_check.py http://127.0.0.1:19080/health
$COMPOSE -p full_local --env-file .env -f docker-compose.yml down --remove-orphans
