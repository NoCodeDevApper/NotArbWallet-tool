#!/usr/bin/env bash
set -e

VENV_DIR="venv"
# 1) Create venv if missing
if [[ ! -d "$VENV_DIR" ]]; then
  python3 -m venv "$VENV_DIR"
  echo "Created virtual environment in $VENV_DIR"
fi

# 2) Activate & install requirements (idempotent)
source "$VENV_DIR/bin/activate"
pip install -r requirements.txt

echo "Launching PM2 process..."

# 3) Ensure pm2 is installed
if ! command -v pm2 &> /dev/null; then
  echo "PM2 not found. Install globally: npm install -g pm2"
  exit 1
fi

# 4) Start or reload
pm2 start ecosystem.config.js --env production
pm2 save
pm2 status
