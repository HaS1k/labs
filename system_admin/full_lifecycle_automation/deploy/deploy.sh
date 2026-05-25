#!/usr/bin/env bash
set -u
ENVIRONMENT="${1:-staging}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"
if docker compose version >/dev/null 2>&1; then COMPOSE="docker compose"; else COMPOSE="docker-compose"; fi
case "$ENVIRONMENT" in
  staging) ENV_FILE=".env.staging"; PROJECT="full_staging"; OVERRIDE="docker-compose.staging.yml" ;;
  production) ENV_FILE=".env.production"; PROJECT="full_production"; OVERRIDE="docker-compose.production.yml" ;;
  *) echo "Usage: $0 staging|production" >&2; exit 2 ;;
esac
$COMPOSE -p "$PROJECT" --env-file "$ENV_FILE" -f docker-compose.yml -f "$OVERRIDE" down --remove-orphans || true
$COMPOSE -p "$PROJECT" --env-file "$ENV_FILE" -f docker-compose.yml -f "$OVERRIDE" up -d --build
$COMPOSE -p "$PROJECT" --env-file "$ENV_FILE" -f docker-compose.yml -f "$OVERRIDE" ps
