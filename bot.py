import os
from telegram.ext import Application

BOT_TOKEN = os.environ.get("TELEGRAM_TOKEN")  # Токен из Railway

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    # ... твои обработчики команд ...
    app.run_polling()

if __name__ == "__main__":
    main()
