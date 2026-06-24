# Бесплатный деплой

Проект состоит из двух частей:

- `index.html` - Telegram Web App, его можно разместить на GitHub Pages.
- `bot.py` - Telegram bot webhook, его можно разместить на Render Free Web Service.

## 1. GitHub Pages для Web App

1. Создай публичный репозиторий на GitHub, например `p2p-calculator-bot`.
2. Загрузи туда файлы проекта.
3. Открой `Settings` -> `Pages`.
4. В `Build and deployment` выбери:
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/ (root)`
5. Сохрани.

Ссылка будет примерно такой:

```text
https://USERNAME.github.io/p2p-calculator-bot/
```

Именно эту ссылку нужно указать как `WEBAPP_URL` на Render.

## 2. Render для бота

1. Зайди на https://render.com и войди через GitHub.
2. Нажми `New` -> `Web Service`.
3. Выбери репозиторий с проектом.
4. Render сам увидит `render.yaml`.
5. Добавь переменные окружения:
   - `BOT_TOKEN` - новый токен из BotFather
   - `WEBAPP_URL` - ссылка GitHub Pages из первого шага
6. Нажми `Deploy`.

После деплоя Render выдаст ссылку сервиса:

```text
https://YOUR-SERVICE.onrender.com
```

## 3. Подключить webhook Telegram

Открой в браузере ссылку, подставив свой токен и ссылку Render:

```text
https://api.telegram.org/botBOT_TOKEN/setWebhook?url=https://YOUR-SERVICE.onrender.com/webhook
```

Если Telegram ответил `{"ok":true,...}`, бот подключен.

## Важно

Токен, который уже был отправлен в чат, лучше перевыпустить в BotFather командой `/revoke`.
Новый токен вставляй только в Render Environment Variables, не добавляй его в файлы проекта.
