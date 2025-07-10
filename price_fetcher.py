import requests

COINGECKO_API = 'https://api.coingecko.com/api/v3/simple/price'

def fetch_sol_price() -> float:
    params = {'ids': 'solana', 'vs_currencies': 'usd'}
    r = requests.get(COINGECKO_API, params=params)
    return r.json().get('solana', {}).get('usd', 0.0)
