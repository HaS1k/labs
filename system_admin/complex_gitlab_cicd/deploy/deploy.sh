#!/usr/bin/env bash
set -u
ENVIRONMENT="${1:-staging}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if docker compose version >/dev/null 2>&1; then
  COMPOSE="docker compose"
elif command -v docker-compose >/dev/null 2>&1; then
  COMPOSE="docker-compose"
else
  echo "Docker Compose not found" >&2
  exit 1
fi

case "$ENVIRONMENT" in
  staging)
    ENV_FILE=".env.staging"
    OVERRIDE="docker-compose.staging.yml"
    PROJECT="complex_staging"
    ;;
  production)
    ENV_FILE=".env.production"
    OVERRIDE="docker-compose.production.yml"
    PROJECT="complex_production"
    ;;
  *)
    echo "Usage: $0 staging|production" >&2
    exit 2
    ;;
esac

$COMPOSE -p "$PROJECT" --env-file "$ENV_FILE" -f docker-compose.yml -f "$OVERRIDE" down --remove-orphans || true
$COMPOSE -p "$PROJECT" --env-file "$ENV_FILE" -f docker-compose.yml -f "$OVERRIDE" up -d --build
$COMPOSE -p "$PROJECT" --env-file "$ENV_FILE" -f docker-compose.yml -f "$OVERRIDE" ps
