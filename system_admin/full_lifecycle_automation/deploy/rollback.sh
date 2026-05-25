#!/usr/bin/env bash
set -u
ENVIRONMENT="${1:-production}"
PREVIOUS_TAG="${2:-previous-release}"
echo "Rollback for $ENVIRONMENT: switch APP_IMAGE_TAG to $PREVIOUS_TAG and run deploy.sh $ENVIRONMENT."
echo "In a real registry-based flow this step pulls the previous image tag from GitLab Container Registry."
