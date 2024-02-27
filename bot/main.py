from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    AIORateLimiter,
    MessageHandler,
    MessageHandler,
    filters
)

from telegram import Update
from telegram.ext import CallbackContext
from telegram.constants import ParseMode
from config.config import TELEGRAM_BOT_TOKEN
import json
from database.aggregation import Aggregation

async def start_handle(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "привет, это бот для тестового задания",  
        parse_mode=ParseMode.HTML
    )
async def message_handle(update: Update, context: CallbackContext):
    aggregation = Aggregation()
    _message = update.message.text
    aggregated = await aggregation.aggregate_data(json.loads(_message))
    _message = update.message.text
    await update.message.reply_text(
        str(aggregated.__dict__),  
        parse_mode=ParseMode.HTML
    )

def run_bot() -> None:
    application = (
        ApplicationBuilder()
        .token(TELEGRAM_BOT_TOKEN)
        .concurrent_updates(True)
        .rate_limiter(AIORateLimiter(max_retries=5))
        .http_version("1.1")
        .get_updates_http_version("1.1")
        .build()
    )

    application.add_handler(CommandHandler("start", start_handle))
    application.add_handler(MessageHandler(filters.TEXT, message_handle))
    application.run_polling()