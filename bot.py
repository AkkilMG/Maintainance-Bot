import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from config import Config as C

PORT = int(C.PORT)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text(C.START_TEXT)

def all(update, context):
    update.message.reply_text(C.MAINTAINANCE_TEXT)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(C.BOT_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.all, all))
    dp.add_error_handler(error)
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=C.BOT_TOKEN)
    updater.bot.setWebhook('https://{C.APP_NAME}.herokuapp.com/' + C.BOT_TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()
