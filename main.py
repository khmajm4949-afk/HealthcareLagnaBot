import os
from flask import Flask
from telegram.ext import Application, CommandHandler

# إعداد Flask
server = Flask(__name__)

@server.route("/")
def home():
    return "✅ Healthcare Lagna Bot is alive!"

# إعداد البوت
TOKEN = os.getenv("BOT_TOKEN")  # التوكن لازم يكون في Environment Variables بـ Render

app = Application.builder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text("👋 مرحبا! أنا مساعدك وعضو لجنة الرعاية الصحية الإلكتروني.")

app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    # نشغل البوت polling
    app.run_polling()
