# Complex GitLab CI/CD lab

This repository folder contains a complete CI/CD lab for a multi-component Docker Compose application.

Artifacts:

- `.gitlab-ci.yml` — GitLab CI/CD pipeline.
- `docker-compose.yml` — base Compose file.
- `docker-compose.staging.yml` and `docker-compose.production.yml` — environment-specific overrides.
- `services/*/Dockerfile` — Dockerfiles for web, database and cache services.
- `deploy/deploy.sh` — deployment script.
- `deploy/rollback.sh` — rollback plan.
- `docs/` — architecture and deployment documentation.
