from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

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

import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

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

async def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_button_click))

    print("Bot is running...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await app.updater.idle()

if __name__ == "__main__":
    asyncio.run(main())

