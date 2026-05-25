# Ansible infrastructure automation lab

This project contains a complete Ansible structure for infrastructure automation:

- static inventory with web, database, load balancer and monitoring groups;
- roles for common settings, Nginx, PostgreSQL master/replica, HAProxy, Prometheus and Grafana;
- Jinja2 templates and handlers;
- Ansible Vault example for sensitive variables;
- additional playbooks for database backups, OS user management and system update planning.

The lab uses safe local inventory aliases for demonstration. The same roles can be adapted to real VMs by replacing `ansible_connection=local` with SSH host parameters.
