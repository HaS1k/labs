# Complex CI/CD architecture

The project contains a multi-component application with three services:

| Service | Purpose | Port |
|---|---|---|
| web | HTTP API and user entry point | 8080 |
| db | simple persistent database service with a named Docker volume | 5432 |
| cache | in-memory cache service | 6379 |

All services are connected through a custom Docker bridge network. The web service addresses the database as `db` and the cache as `cache`, using Docker Compose service DNS.

The CI/CD pipeline includes linting, Docker image build, unit tests, integration tests, image/security scanning, registry publication, staging deployment, staging E2E test and manual production deployment.
