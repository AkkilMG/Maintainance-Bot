# (c) HeimanPictures

from pyrogram import Client, filters, StopPropagation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

@Client.on_message(filters.private & filters.command(['start', 'help', 'donate', 'about']), group=0)
async def start(bot, update):
    await update.reply_text(
        text=Config.MAINTAINANCE_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("Update Channel", url=Config.UPDATE_CHANNEL),
            InlineKeyboardButton("Support Group", url=Config.SUPPORT_GROUP)
            ],[
            InlineKeyboardButton("Repo", url="https://github.com/HeimanPictures/Maintenance-Bot/")
            ]]
        )
    )
