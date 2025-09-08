# Ansible Web Stack

This project automates the deployment of a simple two-tier web application using **Ansible** on **Debian/Ubuntu-based systems**:

- **Frontend**: Nginx serving static HTML and acting as a reverse proxy.  
- **Backend**: Python Flask app managed with `systemd`.  

## How it works
- `frontend-playbook.yml` → installs Nginx, deploys a site config, and serves `index.html`.  
- `backend-playbook.yml` → installs Flask, copies `app.py`, and sets up a systemd service.  
- `site-playbook.yml` → runs both frontend and backend in one command.  
- Inventory is defined in `inventory/main.yml`.  

## Variables
- `vars/frontend.yml` → includes the **backend private IP** (used in Nginx proxy config).  
- `vars/backend.yml` → sets up Flask app directory, user, etc.  

## Usage
1. Configure hosts in `inventory/main.yml`.  
2. Set the backend’s **private IP** in `vars/frontend.yml`.  
3. Run the playbook:  
   ```bash
   ansible-playbook -i inventory/main.yml site-playbook.yml
