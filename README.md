# Telegram P2P Calculator Bot

Telegram-бот открывает P2P-калькулятор как Telegram Web App.

## Файлы

- `index.html` - Web App для GitHub Pages.
- `bot.py` - webhook-бот для Render.
- `render.yaml` - конфигурация бесплатного Render Web Service.
- `DEPLOY.md` - пошаговая инструкция деплоя.

## Локальная проверка

```powershell
$env:BOT_TOKEN="токен_бота"
$env:WEBAPP_URL="https://example.com/"
python bot.py
```

Для настоящего запуска без ПК смотри `DEPLOY.md`.
