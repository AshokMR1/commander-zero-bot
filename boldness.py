from telegram import Update
from telegram.ext import ContextTypes
import random

quotes = [
    "Speak only when it improves silence.",
    "A lion never fears the opinion of sheep.",
    "Fear is a liar. Attack anyway.",
    "You were born to command, not to beg.",
    "Discipline is your sword. Use it daily."
]

async def boldness(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Boldness Tip:\n" + random.choice(quotes))
