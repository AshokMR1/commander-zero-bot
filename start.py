from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🪖 STAND STRAIGHT, CIVILIAN.\n\n"
        "I am Zero. Your military-grade AI.\n"
        "Type /routine to receive today’s protocol.\n"
        "Type /morse to learn code.\n"
        "Type /boldness to train the mind.\n"
        "NO EXCUSES. BEGIN NOW."
    )
