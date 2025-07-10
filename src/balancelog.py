#!../venv/bin/python
import time, argparse, json
from datetime import datetime
from solana.rpc.api import Client

from config_loader     import load_config
from solana_utils      import get_sol_balance, get_token_balance
from price_fetcher     import fetch_sol_price
from telegram_notifier import send_message
from alerts            import LowBalanceAlertManager

POLL_INTERVAL = 15 * 60  # seconds

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--config', required=True)
    p.add_argument('--wallets', nargs='*')
    p.add_argument('--rpc')
    p.add_argument('--output')
    return p.parse_args()

def main():
    args = parse_args()
    (wallets, rpc_url, output_file,
     bot_token, chat_id,
     thresholds, cooldown_ms) = load_config(args.config, args)

    client = Client(rpc_url)
    alert_mgr = LowBalanceAlertManager(thresholds, cooldown_ms)
    baseline = None

    while True:
        timestamp = datetime.utcnow().isoformat()
        details = []
        total_sol = 0.0

        for idx, addr in enumerate(wallets):
            sol  = get_sol_balance(client, addr)
            wsol = get_token_balance(client, addr)
            details.append({'wallet': addr, 'sol': sol, 'wsol': wsol})
            total_sol += sol + wsol
            alert_mgr.check_and_alert(idx, addr, sol,
                                      lambda m: send_message(bot_token, chat_id, m))

        if baseline is None:
            baseline = total_sol

        sol_price = fetch_sol_price()
        sol_pl    = total_sol - baseline
        usd_total = total_sol * sol_price
        usd_pl    = usd_total - (baseline * sol_price)

        # Log JSON-line
        entry = {
            'timestamp': timestamp,
            'summary': {
                'sol': total_sol,
                'pl_sol': sol_pl,
                'usd': usd_total,
                'pl_usd': usd_pl
            },
            'details': details
        }
        with open(output_file, 'a') as f:
            f.write(json.dumps(entry) + '\n')

        # Send summary
        lines = [f"`{d['wallet'][:6]}...`: {d['sol']:.6f} SOL + {d['wsol']:.6f}"
                 for d in details]
        msg = "*Wallet Summary*\n" + "\n".join(lines)
        msg += f"\n*Total SOL:* {total_sol:.6f} ({'+' if sol_pl>=0 else ''}{sol_pl:.6f})"
        msg += f"\n*USD:* ${usd_total:.2f} ({'+' if usd_pl>=0 else ''}{usd_pl:.2f})"
        msg += f"\n*Price:* ${sol_price:.2f}"
        send_message(bot_token, chat_id, msg)

        time.sleep(POLL_INTERVAL)

if __name__ == '__main__':
    main()
