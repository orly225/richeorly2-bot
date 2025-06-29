from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
import threading

# Token de ton bot
TOKEN = "7865019518:AAEiTP6ZAgwbUG7ZxsKy5LaJ1VVP-L1Y60s"

# Serveur web minimal pour Render
app_web = Flask('')

@app_web.route('/')
def home():
    return "RICHEORLY2 Bot is running!"

def run_flask():
    app_web.run(host='0.0.0.0', port=8080)

# Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenue sur RICHEORLY2 ! 🚀")

# Lancement du bot + webserver
if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
