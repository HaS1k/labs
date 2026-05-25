#!/usr/bin/env bash
set -u
ENVIRONMENT="${1:-staging}"
PREVIOUS_TAG="${2:-previous}"
echo "Rollback plan for $ENVIRONMENT: retag/pull image tag $PREVIOUS_TAG and run deploy.sh $ENVIRONMENT"
echo "In production this command would be combined with image tags stored in the registry."
