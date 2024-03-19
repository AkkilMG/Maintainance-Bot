import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):

    # Required Variables
    
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # The Telegram API things
    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    
    # Non-required Variables
    
    # Text
    MAINTAINANCE_TEXT = os.environ.get("MAINTAINANCE_TEXT", "Bot is under maintainance. Please try again later.")
    
    # Update channel and support group info
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")
    SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "")
    # Private only or not
    PRIVATE_ONLY = bool(os.environ.get("PRIVATE_ONLY", True))
    # Filter text messages or commands only
    FILTER_TEXT = bool(os.environ.get("FILTER_TEXT", True))
    # Filter media (default is False)
    FILTER_MEDIA = bool(os.environ.get("FILTER_MEDIA", False))
    
    # Source code
    SOURCE_CODE = "https://github.com/AkkilMG/Maintenance-Bot/"
