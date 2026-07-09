# Contract Risk AI — Production Deployment Guide

Deploy Contract Risk AI to an **AWS EC2 Ubuntu** server with Nginx reverse proxy,
FastAPI backend (systemd), and SQLite database.

## Architecture

```
Internet ──▶ Nginx (:80 / :443)
               ├── /api/*       →  FastAPI  (127.0.0.1:8000)
               ├── /            →  Static files (frontend/dist/)
               └── SPA fallback →  index.html
```

| Component    | Role                           | Tech                |
|-------------|--------------------------------|----------------------|
| Nginx       | Reverse proxy + static files   | nginx                |
| Backend     | REST API                       | FastAPI + Uvicorn    |
| Database    | Users + Reports                | SQLite (aiosqlite)   |
| Frontend    | Vue 3 SPA                      | Built to static HTML |
| AI          | DeepSeek API (external)       | HTTP call via httpx  |

## Prerequisites

- **AWS EC2** Ubuntu 22.04 / 24.04 (t3.small or larger recommended)
- SSH access with sudo
- A domain name pointing to the server's public IP (optional but recommended)
- DeepSeek API key ([platform.deepseek.com](https://platform.deepseek.com/api_keys))

## Quick Deploy (Automated)

SSH into your server and run:

```bash
# As root / sudo user
curl -fsSL https://github.com/baobateer-arch/ai-automation-toolkit/archive/main.tar.gz | tar xz
cd ai-automation-toolkit-main
chmod +x deploy/deploy.sh
sudo ./deploy/deploy.sh contractriskai.com

# After deploy, edit environment variables
sudo nano /opt/contractriskai/.env
# Set DEEPSEEK_API_KEY and JWT_SECRET_KEY

sudo systemctl restart contractriskai
```

## Manual Step-by-Step

### 1. Install System Dependencies

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nginx git
```

### 2. Install Node.js (for frontend build)

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
node --version     # should be v20.x
npm --version
```

### 3. Deploy Application

```bash
# Clone the repository
sudo mkdir -p /opt/contractriskai
sudo git clone https://github.com/baobateer-arch/ai-automation-toolkit.git /opt/contractriskai
sudo chown -R www-data:www-data /opt/contractriskai
cd /opt/contractriskai
```

### 4. Setup Python Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### 5. Build Frontend

```bash
cd frontend
npm install
npm run build      # Output: frontend/dist/
cd ..
```

### 6. Configure Environment

```bash
cp .env.example .env
nano .env
```

Required variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `DEEPSEEK_API_KEY` | DeepSeek API key from platform.deepseek.com | `sk-abc123...` |
| `JWT_SECRET_KEY` | Random 64+ char secret for JWT signing | `openssl rand -hex 64` |
| `DEBUG` | Set to `false` in production | `false` |

```bash
# Generate a secure JWT secret
echo "JWT_SECRET_KEY=$(openssl rand -hex 64)" | sudo tee -a /opt/contractriskai/.env
```

Create required directories:

```bash
mkdir -p uploads exports
chmod 755 uploads exports
```

### 7. Configure Nginx

```bash
# Copy Nginx config
sudo cp deploy/nginx-contractriskai.conf /etc/nginx/sites-available/contractriskai

# Enable site
sudo ln -sf /etc/nginx/sites-available/contractriskai /etc/nginx/sites-enabled/

# Test and reload
sudo nginx -t
sudo systemctl reload nginx
```

**Config details** (`deploy/nginx-contractriskai.conf`):

- Serves static files from `/opt/contractriskai/frontend/dist/`
- Proxies `/api/*` to FastAPI on `127.0.0.1:8000`
- SPA fallback: all non-file routes serve `index.html`
- Upload limit: 50MB

### 8. Setup systemd Service

```bash
sudo cp deploy/contractriskai.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable contractriskai
sudo systemctl start contractriskai

# Check status
sudo systemctl status contractriskai

# View logs
sudo journalctl -u contractriskai -f
```

### 9. Verify Deployment

```bash
# Health check
curl http://localhost:8000/api/health

# Frontend
curl -s http://localhost/ | head -5

# Full API check
curl -X POST http://localhost/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123456"}'
```

## SSL / HTTPS (Let's Encrypt)

```bash
sudo apt install -y certbot python3-certbot-nginx

# Obtain certificate (interactive)
sudo certbot --nginx -d contractriskai.com

# Auto-renewal (certbot adds a systemd timer automatically)
sudo certbot renew --dry-run
```

After SSL setup, Nginx will handle both HTTP → HTTPS redirect and HTTPS serving.

## Production Considerations

### Database

SQLite (`reports.db`) is suitable for **single-user and small team deployments**.
For higher concurrency, migrate to PostgreSQL:

1. Install PostgreSQL
2. Update `app/core/config.py` to read `DATABASE_URL` from environment
3. Update `app/database.py` to use `asyncpg` instead of `aiosqlite`

### File Storage

Uploaded PDFs and exported reports are stored locally:
- `uploads/` — uploaded contract PDFs
- `exports/` — generated PDF/DOCX reports

For multiple servers, mount an NFS / EFS volume at these paths.

### Backups

```bash
# Backup database and uploads
tar -czf /backup/contractriskai-$(date +%Y%m%d).tar.gz \
  /opt/contractriskai/reports.db \
  /opt/contractriskai/uploads \
  /opt/contractriskai/exports
```

### Monitoring

```bash
# Check service status
sudo systemctl status contractriskai

# Logs
sudo journalctl -u contractriskai -n 100 --no-pager

# API health
curl http://localhost:8000/api/health

# Nginx access logs
sudo tail -f /var/log/nginx/access.log | grep /api/
```

### Resource Requirements

| Instance  | vCPU | RAM  | Use Case              |
|-----------|------|------|-----------------------|
| t3.micro  | 2    | 1 GB | Single user / testing |
| t3.small  | 2    | 2 GB | Small team            |
| t3.medium | 2    | 4 GB | Multiple concurrent   |

## File Layout (Production)

```
/opt/contractriskai/
├── .env                      # Environment variables
├── app/                      # FastAPI application
├── frontend/
│   ├── dist/                 # Built static files (served by Nginx)
│   └── ...                   # Source code (not served)
├── uploads/                  # Uploaded contract PDFs
├── exports/                  # Generated report files
├── reports.db                # SQLite database
├── venv/                     # Python virtual environment
└── deploy/                   # Deployment configs
    ├── nginx-contractriskai.conf
    ├── contractriskai.service
    └── deploy.sh
```

## Docker Alternative

An existing `Dockerfile` and `docker-compose.yml` are in the repository root.
For a Docker-based deployment:

```bash
cd /opt/contractriskai
docker compose up --build -d
```

Note: The Docker setup does not include Nginx — it runs FastAPI directly on
port 8000. For production, add an Nginx container or use a cloud load balancer.

## Troubleshooting

**502 Bad Gateway**
- Check FastAPI is running: `sudo systemctl status contractriskai`
- Check logs: `sudo journalctl -u contractriskai -n 50`

**403 Forbidden on uploads**
- Check directory permissions: `ls -la /opt/contractriskai/uploads/`
- Owner should be `www-data`: `sudo chown -R www-data:www-data /opt/contractriskai`

**Frontend shows blank page**
- Check Nginx root path in config
- Verify `frontend/dist/index.html` exists
- Clear browser cache

**API returns 401 on /api/reports**
- JWT token is missing or expired
- Login again via `/login` page
- Check `JWT_SECRET_KEY` in `.env`

**DeepSeek API errors**
- Verify `DEEPSEEK_API_KEY` in `.env`
- Check network connectivity: `curl https://api.deepseek.com/chat/completions`
- Check service logs for HTTP error codes

## Version

| Tag | Description |
|-----|-------------|
| v5.7-sales-ready | Production-ready commercial MVP |
