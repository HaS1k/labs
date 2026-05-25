# Role description

- `common`: base system configuration, common packages, SSH hardening, NTP template.
- `nginx`: web server virtual hosts and content templates.
- `postgresql_master`: PostgreSQL master configuration, users, database and replication access.
- `postgresql_replica`: standby configuration and replication connection settings.
- `haproxy`: load balancer configuration for web servers.
- `prometheus`: scrape configuration for infrastructure metrics.
- `grafana`: datasource and dashboard provisioning files.

All roles are parameterized through inventory variables and use handlers for service reload/restart operations.
