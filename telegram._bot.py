import os, requests

def send_signal(signal: dict):
    token = os.getenv("TELEGRAM_TOKEN")
    chat = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat:
        print("📛 Missing Telegram credentials")
        return

    msg = (
        "📈 *Signal Alert*\n\n"
        f"Instrument: {signal['instrument']}\n"
        f"Direction: {signal['direction']}\n"
        f"Confidence: {signal['confidence']}%\n"
        f"Entry: {signal['entry']}\n"
        f"Exit: {signal['exit']}\n"
        f"Reason: {signal['reason']}"
    )
    res = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data={"chat_id": chat, "text": msg, "parse_mode": "Markdown"}
    )
    print("Telegram response:", res.status_code, res.text)
