# Full lifecycle automation lab

GitHub artifact folder for an integrated DevOps project using GitLab CI, Ansible, Docker and Docker Compose.

Main artifacts:

- `.gitlab-ci.yml` — full CI/CD pipeline.
- `docker-compose.yml`, `docker-compose.staging.yml`, `docker-compose.production.yml` — application deployment.
- `app/*/Dockerfile` — container images for all components.
- `ansible/` — inventory, roles, playbooks and templates.
- `deploy/` — deployment and rollback scripts.
- `docs/` — architecture and operations documentation.
