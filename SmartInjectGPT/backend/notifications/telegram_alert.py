# telegram_alert.py — Sends alert to Telegram owner

import requests

# Hizi lazima zijazwe kwa token zako halisi
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
OWNER_CHAT_ID = "YOUR_CHAT_ID_HERE"

def send_telegram_alert(message: str) -> bool:
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": OWNER_CHAT_ID,
            "text": f"🚨 SmartInjectGPT Alert:\n\n{message}"
        }
        res = requests.post(url, json=payload)
        return res.status_code == 200
    except Exception as e:
        print("❌ Telegram alert failed:", str(e))
        return False
