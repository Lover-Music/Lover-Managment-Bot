from pyrogram import filters, enums

from Razerbot import pbot, BOT_NAME, BOT_USERNAME


@pbot.on_message(filters.command("write"))
async def handwriting(_, message):
    if len(message.command) < 2:
        return await message.reply_text("» Gɪᴠᴇ Sᴏᴍᴇ Tᴇxᴛ Tᴏ Wʀɪᴛᴇ Iᴛ Oɴ Mʏ Cᴏᴩʏ...")
    m = await message.reply_text("» Wᴀɪᴛ A Sᴇᴄ, Lᴇᴛ Mᴇ Wʀɪᴛᴇ Tʜᴀᴛ Tᴇxᴛ...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("Uᴩʟᴏᴀᴅɪɴɢ...")
    await pbot.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_PHOTO)
    await message.reply_photo(hand, caption=f"Wʀɪᴛᴛᴇɴ Wɪᴛʜ 🖊 Bʏ [{BOT_NAME}](t.me/{BOT_USERNAME})")
