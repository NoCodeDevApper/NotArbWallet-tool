# NotArbWallet-tool

Solana wallet balance logger & P&L tracker with Telegram alerts and low-balance notifications, designed for easy PM2 deployment.

---

## 🚀 Features

- Periodic (15 min) fetch of SOL & WSOL balances  
- JSON-lines log of balances + P&L  
- Telegram summaries & low-balance alerts (with per-wallet cooldown)  
- Modular codebase—add new integrations by dropping in `src/*.py` modules  
- Fully configurable via `walletconf.toml`  

---

## 📥 Download & Install

### Option A: `git clone`

```bash
git clone https://github.com/NoCodeDevApper/NotArbWallet-tool.git
cd NotArbWallet-tool
Option B: wget + unzip
bash
Copy
Edit
# 1. Download ZIP of main branch
wget https://github.com/NoCodeDevApper/NotArbWallet-tool/archive/refs/heads/main.zip \
     -O NotArbWallet-tool-main.zip

# 2. Unzip
sudo apt update && sudo apt install -y unzip    # if you don’t have unzip
unzip NotArbWallet-tool-main.zip

# 3. Rename & enter
mv NotArbWallet-tool-main NotArbWallet-tool
cd NotArbWallet-tool
⚙️ Configuration
Copy the example config (or create if missing):

bash
Copy
Edit
cp walletconf.example.toml walletconf.toml
Edit walletconf.toml:

toml
Copy
Edit
[wallets]
addresses = ["<WALLET_PUBKEY1>", "<WALLET_PUBKEY2>"]

[rpc]
url = "https://api.mainnet-beta.solana.com"

[output]
file = "balances.log"

[telegram]
bot_token = "<YOUR_TELEGRAM_BOT_TOKEN>"
chat_id   = "<YOUR_TELEGRAM_CHAT_ID>"

[alerts]
thresholds  = [1.0, 0.5]    # SOL thresholds per wallet
cooldown_ms = 60000        # ms between alerts per wallet
NOTE: Do not commit real walletconf.toml—it contains secrets. Add it to .gitignore.

🛠️ Setup & Run
Ensure you have

Python 3.8+

npm & PM2

unzip (if using ZIP)

Run the launcher:

bash
Copy
Edit
chmod +x start_all.sh
./start_all.sh
This will:

Create or reuse venv/

Install only missing/pinned deps from requirements.txt

Start balancelog.py under PM2 (app name: balance-logger)

Save PM2 process list & show status

Verify:

bash
Copy
Edit
pm2 status balance-logger
pm2 logs   balance-logger --lines 20
tail -f balances.log
🔄 Updating
If you’ve pulled new commits:

bash
Copy
Edit
cd NotArbWallet-tool
git pull origin main
./start_all.sh    # re-installs missing deps & reloads PM2
🧩 Adding New Features
Drop your new module in src/, e.g. src/my_new_integration.py.

Import & wire it up in src/balancelog.py or another orchestrator.

Expose any new config in walletconf.toml.

⚠️ Troubleshooting
Authentication errors when pushing to GitHub over HTTPS → generate a Personal Access Token (PAT), then run:

bash
Copy
Edit
git remote set-url origin https://github.com/NoCodeDevApper/NotArbWallet-tool.git
git config --global credential.helper osxkeychain  # macOS
# or: git config --global credential.helper cache    # Linux
git push -u origin main  # enter PAT when prompted for password
Missing unzip → sudo apt install unzip or brew install unzip.

