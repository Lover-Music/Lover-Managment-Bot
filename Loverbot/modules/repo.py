from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from Loverbot import pbot, START_IMG

@pbot.on_message(filters.command(["repo", "source"]))
async def repo(_, message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""ʜᴇʏ ɪ'ᴍ Lover Boy

⥤ ᴅᴇᴠᴇʟᴏᴘᴇʀ : @shubhamsah1
⥤ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : `{y()}`
⥤ ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ : `{o}`
⥤ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : `{s}`
⥤ ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : `{z}`

LOVERBOT ɪs ᴀɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ ʙᴏᴛ ᴘʀᴏᴊᴇᴄᴛ.
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="sᴏᴜʀᴄᴇ", url="https://github.com/Lover-Music/Lover-Managment-Bot"), 
                    InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=1548904516)
                ]
            ]
        )
    )
