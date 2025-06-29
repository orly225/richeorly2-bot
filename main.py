from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenue sur RICHEORLY2 🚀 !")

if __name__ == "__main__":
    import os
    from telegram.ext import Application

    token = os.getenv("BOT_TOKEN")

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot démarré...")
    app.run_polling()
