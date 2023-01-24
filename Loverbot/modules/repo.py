from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from Razerbot import pbot, START_IMG

@pbot.on_message(filters.command(["repo", "source"]))
async def repo(_, message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""ʜᴇʏ ɪ'ᴍ RΛZΞR

⥤ ᴅᴇᴠᴇʟᴏᴘᴇʀ : @WH0907
⥤ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : `{y()}`
⥤ ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ : `{o}`
⥤ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : `{s}`
⥤ ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : `{z}`

ʀᴀᴢᴇʀʙᴏᴛ ɪs ᴀɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ ʙᴏᴛ ᴘʀᴏᴊᴇᴄᴛ.
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="sᴏᴜʀᴄᴇ", url="https://github.com/LinuxGuy312/RazerBot"), 
                    InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=1413518510)
                ]
            ]
        )
    )