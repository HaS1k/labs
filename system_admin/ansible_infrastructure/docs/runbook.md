# Runbook

Inventory graph:

```bash
ansible-inventory -i inventories/lab/hosts.ini --graph
```

Syntax check:

```bash
ansible-playbook -i inventories/lab/hosts.ini site.yml --syntax-check --vault-password-file .vault_pass
```

Apply configuration:

```bash
ansible-playbook -i inventories/lab/hosts.ini site.yml --vault-password-file .vault_pass
```

Dry run and diff:

```bash
ansible-playbook -i inventories/lab/hosts.ini site.yml --check --diff --vault-password-file .vault_pass
```

Additional playbooks:

```bash
ansible-playbook -i inventories/lab/hosts.ini playbooks/backup_db.yml --vault-password-file .vault_pass
ansible-playbook -i inventories/lab/hosts.ini playbooks/users.yml --vault-password-file .vault_pass
ansible-playbook -i inventories/lab/hosts.ini playbooks/update_system.yml --vault-password-file .vault_pass
```
