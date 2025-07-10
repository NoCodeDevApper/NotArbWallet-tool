from solana.rpc.api import Client

WSOL_MINT = 'So11111111111111111111111111111111111111112'

def get_sol_balance(client: Client, address: str) -> float:
    resp = client.get_balance(address)
    return resp['result']['value'] / 1e9

def get_token_balance(client: Client, address: str, mint: str = WSOL_MINT) -> float:
    resp = client.get_token_accounts_by_owner(
        address,
        {'mint': mint},
        encoding='jsonParsed'
    )
    total = 0
    for acct in resp['result']['value']:
        info = acct['account']['data']['parsed']['info']['tokenAmount']
        total += int(info['amount']) / (10 ** info['decimals'])
    return total
