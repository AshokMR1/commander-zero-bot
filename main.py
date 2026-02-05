from telegram.ext import ApplicationBuilder, CommandHandler, ConversationHandler, MessageHandler, filters
import commands.start as start_cmd
import commands.routine as routine_cmd
import commands.morse as morse_cmd
import commands.boldness as boldness_cmd
from telegram.ext import CommandHandler, CallbackQueryHandler
import commands.routine as routine_cmd
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")


#  Build the app
app = ApplicationBuilder().token(BOT_TOKEN).build()

#  Add all command handlers
app.add_handler(CommandHandler("start", start_cmd.start))
app.add_handler(CommandHandler("routine", routine_cmd.routine))
app.add_handler(CommandHandler("boldness", boldness_cmd.boldness))

app.add_handler(CommandHandler("routine", routine_cmd.routine))
app.add_handler(CallbackQueryHandler(routine_cmd.button_handler))
app.add_handler(CommandHandler("routine_now", routine_cmd.routine_now))
app.add_handler(CommandHandler("done_pushups", routine_cmd.done_pushups))
app.add_handler(CommandHandler("routine_status", routine_cmd.routine_status))

#  Add the interactive /morse conversation handler
morse_conv = ConversationHandler(
    entry_points=[CommandHandler("morse", morse_cmd.morse_start)],
    states={
        morse_cmd.MORSE_INPUT: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, morse_cmd.morse_convert)
        ]
    },
    fallbacks=[CommandHandler("cancel", morse_cmd.cancel)],
)

app.add_handler(morse_conv)

#  Optional: Handle unknown commands
async def unknown(update, context):
    await update.message.reply_text("❌ Unknown command. Type /start or /help for guidance.")

app.add_handler(MessageHandler(filters.COMMAND, unknown))

#  Start the bot
print("🪖 Commander Zero is standing by...")
app.run_polling()

