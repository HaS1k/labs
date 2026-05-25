# Deployment guide

## Staging

```bash
./deploy/deploy.sh staging
python tests/e2e_check.py http://127.0.0.1:18081/health
```

## Production

```bash
./deploy/deploy.sh production
python tests/e2e_check.py http://127.0.0.1:18082/health
```

## Rollback

```bash
./deploy/rollback.sh production previous-tag
```

Secrets such as registry credentials and SSH keys should be stored in protected and masked GitLab CI/CD variables.
