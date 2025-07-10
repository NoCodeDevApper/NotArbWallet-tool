import requests

def send_message(bot_token: str, chat_id: str, text: str) -> None:
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text, 'parse_mode': 'Markdown'}
    resp = requests.post(url, json=payload)
    if not resp.ok:
        print(f'Telegram error: {resp.text}')
