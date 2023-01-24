import logging
import os
import sys
import time
import spamwatch

import telegram.ext as tg
from pyrogram import Client, errors
from telethon import TelegramClient
from telethon.sessions import MemorySession
from aiohttp import ClientSession
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, ChannelInvalid
from pyrogram.types import Chat, User
from inspect import getfullargspec
from Loverbot.quotstuff.quotapi import Quotly

StartTime = time.time()

# enable logging
FORMAT = "[LoverBot] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)

async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})

aiohttpsession = ClientSession()

    
from config import Development as Config

TOKEN = Config.TOKEN

try:
    OWNER_ID = int(Config.OWNER_ID)
except ValueError:
    raise Exception("Your OWNER_ID variable is not a valid integer.")

JOIN_LOGGER = Config.JOIN_LOGGER
OWNER_USERNAME = Config.OWNER_USERNAME
ALLOW_CHATS = Config.ALLOW_CHATS
try:
    DRAGONS = set(int(x) for x in Config.DRAGONS or [])
    DEV_USERS = set(int(x) for x in Config.DEV_USERS or [])
except ValueError:
    raise Exception("Your sudo or dev users list does not contain valid integers.")

try:
    DEMONS = set(int(x) for x in Config.DEMONS or [])
except ValueError:
    raise Exception("Your support users list does not contain valid integers.")

try:
    WOLVES = set(int(x) for x in Config.WOLVES or [])
except ValueError:
    raise Exception("Your whitelisted users list does not contain valid integers.")

try:
    TIGERS = set(int(x) for x in Config.TIGERS or [])
except ValueError:
    raise Exception("Your tiger users list does not contain valid integers.")

EVENT_LOGS = Config.EVENT_LOGS
WEBHOOK = Config.WEBHOOK
URL = Config.URL
BOT_USERNAME = Config.BOT_USERNAME
BOT_NAME = Config.BOT_NAME
PORT = Config.PORT
CERT_PATH = Config.CERT_PATH
API_ID = Config.API_ID
API_HASH = Config.API_HASH
DB_URI = Config.SQLALCHEMY_DATABASE_URI
MONGO_DB_URI = Config.MONGO_DB_URI
TEMP_DOWNLOAD_DIRECTORY = Config.TEMP_DOWNLOAD_DIRECTORY
OPENWEATHERMAP_ID = Config.OPENWEATHERMAP_ID
START_IMG = Config.START_IMG
ALIVE_IMG = Config.ALIVE_IMG
BOT_ID = Config.BOT_ID
LOAD = Config.LOAD
NO_LOAD = Config.NO_LOAD
DEL_CMDS = Config.DEL_CMDS
STRICT_GBAN = Config.STRICT_GBAN
WORKERS = Config.WORKERS
BAN_STICKER = Config.BAN_STICKER
ALLOW_EXCL = Config.ALLOW_EXCL
CASH_API_KEY = Config.CASH_API_KEY
TIME_API_KEY = Config.TIME_API_KEY
UPDATE_CHANNEL = Config.UPDATE_CHANNEL
SUPPORT_CHAT = Config.SUPPORT_CHAT
SUPPORT_GROUP = SUPPORT_CHAT
SPAMWATCH_SUPPORT_CHAT = Config.SPAMWATCH_SUPPORT_CHAT
SPAMWATCH_API = Config.SPAMWATCH_API
INFOPIC = Config.INFOPIC
IBM_WATSON_CRED_URL = Config.IBM_WATSON_CRED_URL
IBM_WATSON_CRED_PASSWORD = Config.IBM_WATSON_CRED_PASSWORD

try:
    BL_CHATS = set(int(x) for x in Config.BL_CHATS or [])
except ValueError:
    raise Exception("Your blacklisted chats list does not contain valid integers.")

DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)

if not SPAMWATCH_API:
    sw = None
    LOGGER.warning("SpamWatch API key missing! recheck your config.")
else:
    try:
        sw = spamwatch.Client(SPAMWATCH_API)
    except:
        sw = None
        LOGGER.warning("Can't connect to SpamWatch!")

updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient(MemorySession(), API_ID, API_HASH)
pbot = Client("loverpbot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
dispatcher = updater.dispatcher

BOT_ID = dispatcher.bot.id
BOT_NAME = dispatcher.bot.first_name
BOT_UERNAME = dispatcher.bot.username

DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)

# Load at end to ensure all prev variables have been set
from Razerbot.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler

#-------Quote-------
quotly = Quotly()
#-------------------
