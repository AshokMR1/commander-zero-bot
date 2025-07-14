from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler
import datetime

# A dict to simulate user progress (can be replaced by file/db)
user_progress = {}

# Routine blocks (time, task)
routine_schedule = [
    ("05:00", "Wake up"),
    ("05:15", "Cold shower & make bed"),
    ("05:30", "Physical training (30 mins minimum)"),
    ("06:15", "Meditation (10 minutes)"),
    ("06:30", "Read 10 pages of a book"),
    ("07:00", "Light meal & plan the day"),
    ("08:00", "Execute main task (deep work)"),
    ("12:30", "Break + Tactical reflection"),
    ("13:30", "Skill learning / growth work"),
    ("17:00", "Physical reset (walk/stretch)"),
    ("18:00", "Serve others (kindness mission)"),
    ("19:00", "Light dinner"),
    ("20:00", "Journaling: 3 wins + 1 lesson"),
    ("21:00", "Digital detox"),
    ("21:30", "Sleep like a lion")
]

async def routine(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_progress[user_id] = set()  # Reset progress for the day

    buttons = [
        [InlineKeyboardButton(f"✅ {task}", callback_data=f"done_{i}")]
        for i, (_, task) in enumerate(routine_schedule)
    ]

    await update.message.reply_text(
        "🪖 **Commander Zero Routine - Discipline Protocol**\n\nSelect each task after completing it."
        "\nTrack your progress. Be honest. Be lethal.",
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode="Markdown"
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data.startswith("done_"):
        index = int(query.data.split("_")[1])
        _, task = routine_schedule[index]

        # Prevent duplicate completion
        if user_id in user_progress and index in user_progress[user_id]:
            await query.edit_message_text(
                text=f"🔁 You already completed: {task}"
            )
        else:
            user_progress.setdefault(user_id, set()).add(index)
            await query.edit_message_text(
                text=f"✅ Task marked as complete: {task}\nDiscipline recorded. Proceed, soldier."
            )

            # Check for bonus drill injection
            if index in [2, 8, 12]:
                await context.bot.send_message(
                    chat_id=query.message.chat_id,
                    text="💣 BONUS DRILL: Do 20 push-ups. Reply with /done_pushups when complete."
                )

async def routine_now(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.now().strftime("%H:%M")
    next_task = "Rest or journal."
    for time_block, task in routine_schedule:
        if now <= time_block:
            next_task = task
            break

    await update.message.reply_text(f"⏰ It's {now}\nYour next mission: {next_task}")

async def done_pushups(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Acknowledge: Mind over body. Push-ups logged. Continue the mission.")

async def routine_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    done = user_progress.get(user_id, set())

    if not done:
        await update.message.reply_text("❌ You haven’t completed any tasks yet today. Start with /routine")
        return

    text = "📊 Your Progress:\n"
    for i, (_, task) in enumerate(routine_schedule):
        check = "✅" if i in done else "❌"
        text += f"{check} {task}\n"

    progress = (len(done) / len(routine_schedule)) * 100
    text += f"\n🔥 Discipline Score: {int(progress)}%"

    await update.message.reply_text(text)
