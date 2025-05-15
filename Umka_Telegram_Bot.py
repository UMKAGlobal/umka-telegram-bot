import asyncio
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHANNEL_ID = -4782134982  # ID канала для отправки заявок

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton("Записаться в детский сад", callback_data='register_daycare')],
                [InlineKeyboardButton("Получить информацию о летнем лагере", callback_data='info_camp')],
                [InlineKeyboardButton("Узнать о поступлении в 1 класс", callback_data='info_school')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Добро пожаловать в UMKA Bilingual School & Kindergarten!\nЧем я могу помочь?", reply_markup=reply_markup
    )

async def handle_button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'register_daycare':
        await query.edit_message_text(
            text="Для записи в детский сад, пожалуйста, отправьте ваше имя, возраст ребенка и контактный номер. Наш менеджер свяжется с вами для уточнения деталей."
        )
    elif query.data == 'info_camp':
        await query.edit_message_text(
            text="Летний лагерь (июнь - июль)\n\nВозрастные группы: 3-5 лет и 6-8 лет\nПроекты: My Little Village, индивидуальные творческие задания, плавание, серфинг, пикники и многое другое!\n\nНапишите 'Хочу в лагерь', чтобы узнать больше!"
        )
    elif query.data == 'info_school':
        await query.edit_message_text(
            text="Поступление в 1 класс (2025 учебный год)\n\nСовместная программа с The First Academy, адаптация первоклассников и мягкий переход от детского сада.\n\nНапишите 'Хочу в 1 класс', чтобы узнать больше!"
        )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    user_name = update.message.from_user.username or update.message.from_user.full_name
    chat_id = update.message.chat_id

    message_to_channel = f"📬 Новая заявка от пользователя @{user_name} (ID: {chat_id}):\n\n{user_message}"

    # Отправляем сообщение в канал
    await context.bot.send_message(chat_id=CHANNEL_ID, text=message_to_channel)

async def run_bot():
    try:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(handle_button_click))
        app.add_handler(CommandHandler("register", handle_message))  # Добавляем обработчик сообщений

        print("Bot is running...")
        await app.initialize()
        await app.start()
        await app.updater.start_polling()
        await app.updater.idle()
    except Exception as e:
        print(f"Error: {e}")
        await asyncio.sleep(5)  # Ждем 5 секунд перед перезапуском
        await run_bot()

if __name__ == "__main__":
    asyncio.run(run_bot())
