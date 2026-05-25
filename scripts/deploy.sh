#!/usr/bin/env bash
set -euo pipefail
ENVIRONMENT="${1:-dev}"
if docker compose version >/dev/null 2>&1; then
  COMPOSE="docker compose"
else
  COMPOSE="docker-compose"
fi
if [ "$ENVIRONMENT" = "prod" ]; then
  FILE="docker-compose.prod.yml"
else
  FILE="docker-compose.dev.yml"
fi
$COMPOSE -p labcicd -f "$FILE" down --remove-orphans
$COMPOSE -p labcicd -f "$FILE" up -d
$COMPOSE -p labcicd -f "$FILE" ps
