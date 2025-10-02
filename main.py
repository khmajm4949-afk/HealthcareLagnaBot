import os
from flask import Flask
from telegram.ext import Application, CommandHandler

# إعداد Flask
app_flask = Flask(__name__)

@app_flask.route("/")
def home():
    return "✅ Bot is running on Render"

# بوت تيليجرام
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Application.builder().token(BOT_TOKEN).build()

async def start(update, context):
    await update.message.reply_text("👋 مرحبا بك! البوت يعمل.")

bot.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    import threading

    # Thread لتشغيل البوت
    threading.Thread(target=lambda: bot.run_polling()).start()

    # تشغيل Flask على بورت Render
    port = int(os.getenv("PORT", 5000))
    app_flask.run(host="0.0.0.0", port=port)
