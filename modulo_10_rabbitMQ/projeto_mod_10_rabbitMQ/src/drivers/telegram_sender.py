import requests

def send_telegram_message(message: str) -> None:
    token = "7602059794:AAFMC0yzgNqWvUiRgoe_zsWwwJBbSQYvVNA"
    chat_id= -1002382732473

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(url, data=payload)