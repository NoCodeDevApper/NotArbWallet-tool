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
```


### Option B: wget + unzip

# 1. Download ZIP of main branch
```
wget https://github.com/NoCodeDevApper/NotArbWallet-tool/archive/refs/heads/main.zip \
     -O NotArbWallet-tool-main.zip
```

# 2. Unzip
```
sudo apt update && sudo apt install -y unzip    # if you don’t have unzip
unzip NotArbWallet-tool-main.zip
```

# 3. Rename & enter
```
mv NotArbWallet-tool-main NotArbWallet-tool
cd NotArbWallet-tool
```

### ⚙️ Configuration
Copy the example config (or create if missing):

```bash
cp walletconf.example.toml walletconf.toml
```
Edit walletconf.toml
```toml
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
```

## 🛠️ Setup & Run
### Prerequisites
* Python 3.8+
* npm & PM2
* unzip (if using ZIP)

### Run the launcher:

```bash
chmod +x start_all.sh
./start_all.sh
```
### This will:
* Create or reuse venv/
* Install only missing/pinned deps from requirements.txt
* Start balancelog.py under PM2 (app name: balance-logger)
* Save PM2 process list & show status

### Verify:
```bash
pm2 status balance-logger
pm2 logs   balance-logger --lines 20
tail -f balances.log
```
🔄 Updating

```bash
```


