#!/usr/bin/env bash
set -euo pipefail

APP_DIR="/opt/contractriskai"
REPO_URL="https://github.com/baobateer-arch/ai-automation-toolkit.git"
DOMAIN="${1:-contractriskai.com}"  # pass as arg or use default

echo "=== Contract Risk AI — Production Deploy ==="

# --- 1. System packages ---
echo "[1/7] Installing system dependencies…"
sudo apt update -qq
sudo apt install -y -qq python3 python3-pip python3-venv nginx git

# --- 2. Node.js for frontend build ---
echo "[2/7] Installing Node.js…"
if ! command -v node &>/dev/null; then
    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
    sudo apt install -y -qq nodejs
fi

# --- 3. Clone / update application ---
echo "[3/7] Deploying application to $APP_DIR…"
if [ -d "$APP_DIR" ]; then
    cd "$APP_DIR"
    sudo -u www-data git pull
else
    sudo git clone "$REPO_URL" "$APP_DIR"
    sudo chown -R www-data:www-data "$APP_DIR"
fi

# --- 4. Python virtualenv + requirements ---
echo "[4/7] Setting up Python virtualenv…"
cd "$APP_DIR"
sudo -u www-data python3 -m venv venv
sudo -u www-data venv/bin/pip install --upgrade pip setuptools wheel -q
sudo -u www-data venv/bin/pip install -r requirements.txt -q

# --- 5. Build frontend ---
echo "[5/7] Building frontend…"
cd "$APP_DIR/frontend"
sudo -u www-data npm install --silent
sudo -u www-data npm run build

# --- 6. Configure environment ---
echo "[6/7] Setting up environment…"
if [ ! -f "$APP_DIR/.env" ]; then
    sudo -u www-data cp "$APP_DIR/.env.example" "$APP_DIR/.env"
    echo ">> Please edit $APP_DIR/.env and set DEEPSEEK_API_KEY & JWT_SECRET_KEY"
fi

# Create required directories
sudo -u www-data mkdir -p "$APP_DIR/uploads" "$APP_DIR/exports"

# --- 7. Nginx ---
echo "[7/7] Configuring Nginx…"
sudo cp "$APP_DIR/deploy/nginx-contractriskai.conf" "/etc/nginx/sites-available/$DOMAIN"
sudo ln -sf "/etc/nginx/sites-available/$DOMAIN" "/etc/nginx/sites-enabled/"
sudo nginx -t && sudo systemctl reload nginx

# --- 8. systemd service ---
echo "[8/8] Configuring systemd service…"
sudo cp "$APP_DIR/deploy/contractriskai.service" "/etc/systemd/system/contractriskai.service"
sudo systemctl daemon-reload
sudo systemctl enable contractriskai
sudo systemctl restart contractriskai

echo ""
echo "=== Deploy complete ==="
echo "  App:     $APP_DIR"
echo "  API:     http://$(curl -s http://checkip.amazonaws.com)/api/health"
echo "  Status:  sudo systemctl status contractriskai"
echo "  Logs:    sudo journalctl -u contractriskai -f"
echo ""
echo "Next steps:"
echo "  1. Edit $APP_DIR/.env — set DEEPSEEK_API_KEY"
echo "  2. Set up SSL with: sudo certbot --nginx -d $DOMAIN"
echo "  3. Visit http://$DOMAIN to verify"
