import pyrogram
from config import Config 

plugins = dict(
    root="plugins"
)
app = pyrogram.Client(
    "Maintain Bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    plugins=plugins
)
app.run()
