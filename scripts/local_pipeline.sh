#!/usr/bin/env bash
set -euo pipefail
if docker compose version >/dev/null 2>&1; then
  COMPOSE="docker compose"
else
  COMPOSE="docker-compose"
fi
export APP_TAG="local"
$COMPOSE -p labcicd -f docker-compose.dev.yml build
$COMPOSE -p labcicd -f docker-compose.dev.yml up -d
./scripts/test.sh
echo "Push stage is simulated: no external registry is used."
./scripts/deploy.sh prod
