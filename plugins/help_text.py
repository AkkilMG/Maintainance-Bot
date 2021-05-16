# (c) HeimanPictures

import logging
from pyrogram import Client, filters, StopPropagation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from sample_config import Config

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.private & filters.command(['start', 'help', 'donate', 'about']), group=0)
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Config.MAINTAINANCE_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Update Channel", url=Config.UPDATE_CHANNEL),
                    InlineKeyboardButton("Support Group", url=Config.SUPPORT_GROUP)
                ],
                [
                    InlineKeyboardButton("Repo", url="https://github.com/HeimanPictures/Maintenance-Bot/")
                ],
            ])
    )
