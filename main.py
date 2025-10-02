import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from flask import Flask
import threading

TOKEN = os.getenv("BOT_TOKEN")

# Telegram Bot
async def start(update, context):
    welcome_msg = (
        "مرحبا 👋\n\n"
        "أنا مساعدك وعضو لجنة الرعاية الصحية الإلكتروني المختص فقط بمساعدتك "
        "والاهتمام بجميع استفساراتك. وإذا لم أستطع المساعدة كعضو إلكتروني "
        "فسأقوم بإحالتك إلى المساعد البشري. 🤝"
    )
    await update.message.reply_text(welcome_msg)

async def echo(update, context):
    await update.message.reply_text(f"📩 استلمت رسالتك: {update.message.text}")

def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

# Flask server (just to keep Render happy)
server = Flask(__name__)

@server.route('/')
def home():
    return "Bot is running!", 200

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 5000))
    server.run(host="0.0.0.0", port=port)
