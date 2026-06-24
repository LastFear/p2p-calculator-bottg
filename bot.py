import json
import os
import urllib.request

from flask import Flask, jsonify, request


BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
WEBAPP_URL = os.environ.get("WEBAPP_URL", "").strip()
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

app = Flask(__name__)


def api_call(method, payload=None):
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(f"{API_URL}/{method}", data=data, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def send_message(chat_id, text, reply_markup=None):
    payload = {
        "chat_id": chat_id,
        "text": text,
    }
    if reply_markup:
        payload["reply_markup"] = reply_markup
    return api_call("sendMessage", payload)


def send_webapp_button(chat_id):
    reply_markup = {
        "inline_keyboard": [[
            {
                "text": "Открыть P2P калькулятор",
                "web_app": {"url": WEBAPP_URL},
            }
        ]]
    }
    return send_message(chat_id, "Нажми кнопку ниже, чтобы открыть калькулятор.", reply_markup)


def handle_update(update):
    message = update.get("message")
    if not message:
        return

    chat_id = (message.get("chat") or {}).get("id")
    text = (message.get("text") or "").strip()
    if not chat_id:
        return

    if text.startswith("/start") or text.startswith("/app"):
        send_webapp_button(chat_id)
    else:
        send_message(chat_id, "Напиши /start, чтобы открыть калькулятор.")


@app.get("/")
def healthcheck():
    return jsonify({
        "ok": True,
        "service": "telegram-p2p-calculator-bot",
        "webapp_configured": WEBAPP_URL.startswith("https://"),
    })


@app.post("/webhook")
def telegram_webhook():
    if not BOT_TOKEN:
        return jsonify({"ok": False, "error": "BOT_TOKEN is not set"}), 500
    if not WEBAPP_URL.startswith("https://"):
        return jsonify({"ok": False, "error": "WEBAPP_URL must be HTTPS"}), 500

    handle_update(request.get_json(force=True, silent=True) or {})
    return jsonify({"ok": True})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
