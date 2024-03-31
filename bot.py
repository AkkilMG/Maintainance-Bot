from config import Config
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Maintainance Bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH
)

BUTTONS = [[]]
if Config.UPDATE_CHANNEL:
    BUTTONS[0].append([InlineKeyboardButton("Update Channel", url=Config.UPDATE_CHANNEL)])
if Config.SUPPORT_GROUP:
    BUTTONS[0].append([InlineKeyboardButton("Support Group", url=Config.SUPPORT_GROUP)])
if len(BUTTONS[0]) == 0:
    del BUTTONS[0]
BUTTONS.append([InlineKeyboardButton("Source Code", url=Config.SOURCE_CODE)])


@Bot.on_message(filters.media | filters.text)
async def maintainance(_, message):
    
    if Config.PRIVATE_ONLY and (message.chat.type != enums.ChatType.PRIVATE):
        return
    
    if (not Config.FILTER_TEXT) and message.text and (not message.text.startswith("/")):
        return
    
    if (not Config.FILTER_MEDIA) and message.media:
        return
    
    await message.reply_text(
        text=Config.MAINTAINANCE_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(BUTTONS),
        quote=True
    )


Bot.run()
