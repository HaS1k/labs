# Инструкция по эксплуатации

## Локальный запуск

```bash
docker compose --env-file .env -f docker-compose.yml up -d --build
python app/tests/e2e_check.py http://127.0.0.1:19080/health
```

## Staging

```bash
./deploy/deploy.sh staging
python app/tests/e2e_check.py http://127.0.0.1:19081/health
```

## Production

```bash
./deploy/deploy.sh production
python app/tests/e2e_check.py http://127.0.0.1:19082/health
```

## Ansible

```bash
cd ansible
ansible-playbook -i inventory/hosts.yml site.yml --check --diff
ansible-playbook -i inventory/hosts.yml site.yml
```

## Rollback

```bash
./deploy/rollback.sh production previous-release
```
