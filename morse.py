from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, MessageHandler, CommandHandler, filters

MORSE_INPUT = 1

MORSE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
    'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
    'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
    'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
    '8': '---..',  '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', ' ': '/'
}

def text_to_morse(text: str) -> str:
    return ' '.join(MORSE_DICT.get(char.upper(), '?') for char in text)

async def morse_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("📡 Enter the text you'd like to convert into Morse code:")
    return MORSE_INPUT

async def morse_convert(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_text = update.message.text
    morse_code = text_to_morse(user_text)
    await update.message.reply_text(f"🔐 Morse Code:\n`{morse_code}`", parse_mode="Markdown")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("❌ Morse code conversion cancelled.")
    return ConversationHandler.END
