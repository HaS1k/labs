# Infrastructure architecture

The infrastructure is represented by the following Ansible inventory groups:

| Group | Hosts | Purpose |
|---|---:|---|
| webservers | 2 | Nginx application servers |
| db_master | 1 | PostgreSQL primary database server |
| db_replica | 1 | PostgreSQL standby replica |
| loadbalancers | 1 | HAProxy frontend for web servers |
| monitoring | 1 | Prometheus and Grafana monitoring server |

The `site.yml` playbook applies the `common` role first and then configures database, web, load balancer and monitoring roles in order.
