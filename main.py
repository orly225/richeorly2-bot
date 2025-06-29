from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# Remplace par ton token dans Render si ce n'est pas encore fait
TOKEN = os.environ.get("TELEGRAM_TOKEN")

# === Callback Menu Handler ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎰 Lucky Jet", callback_data="luckyjet")],
        [InlineKeyboardButton("💣 Mines", callback_data="mines")],
        [InlineKeyboardButton("🚀 Rocket Queen", callback_data="rocketqueen")],
        [InlineKeyboardButton("📊 Crash", callback_data="crash")],
        [InlineKeyboardButton("📢 Canal VIP", url="https://t.me/+SQBxv3-AEOU5Njdk")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Bienvenue sur RICHEORLY2 🚀 !", reply_markup=reply_markup)

# === Actions pour chaque jeu ===
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "luckyjet":
        await query.edit_message_text("🎰 Prévision Lucky Jet :\n➡️ Multipliez vos chances maintenant !")
    elif query.data == "mines":
        await query.edit_message_text("💣 Prévision Mines :\nVoici une configuration recommandée :\n⬜⬜⬜⬜⬜\n⬜💎💎💎⬜\n⬜⬜⬜⬜⬜")
    elif query.data == "rocketqueen":
        await query.edit_message_text("🚀 Rocket Queen :\nPrévision spéciale disponible !")
    elif query.data == "crash":
        await query.edit_message_text("📊 Crash Prediction :\nMultiplier estimé ➡️ x2.67")

# === Lancer le bot ===
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot lancé...")
    app.run_polling()
