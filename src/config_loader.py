import sys
import toml

def load_config(path, cli_args):
    cfg = toml.load(path)

    # Wallets
    wallets = cli_args.wallets or cfg.get('wallets', {}).get('addresses', [])
    if len(wallets) > 5:
        print('Error: Maximum 5 wallets allowed', file=sys.stderr)
        sys.exit(1)

    # RPC & Output
    rpc_url     = cli_args.rpc    or cfg.get('rpc',    {}).get('url')
    output_file = cli_args.output or cfg.get('output', {}).get('file')

    # Telegram
    tg = cfg.get('telegram', {})
    bot_token = tg.get('bot_token')
    chat_id   = tg.get('chat_id')

    # Alerts
    alerts_cfg = cfg.get('alerts', {})
    thresholds = alerts_cfg.get('thresholds', [])
    cooldown_ms = alerts_cfg.get('cooldown_ms', 60000)

    if not bot_token or not chat_id:
        print('Error: Telegram credentials missing', file=sys.stderr)
        sys.exit(1)

    return wallets, rpc_url, output_file, bot_token, chat_id, thresholds, cooldown_ms
