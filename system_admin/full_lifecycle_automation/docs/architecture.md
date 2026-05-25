# Архитектура комплексного решения

Решение объединяет четыре уровня автоматизации:

1. Контейнеризированное веб-приложение: web, worker, db, cache.
2. Docker Compose для локальной разработки, staging и production.
3. Ansible для подготовки инфраструктуры, пользователей, каталогов, конфигураций, правил файрвола и мониторинга.
4. GitLab CI/CD для полного конвейера от коммита до развертывания.

Поток выполнения: коммит кода -> lint -> build_images -> test -> scan_images -> push_images -> provision_staging_infra -> deploy_staging -> e2e_tests_staging -> manual deploy_production.
