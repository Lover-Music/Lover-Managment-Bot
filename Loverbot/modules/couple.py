from Loverbot import pbot as app
from Loverbot.utils.errors import capture_err
from Loverbot.utils.mongo import get_couple, save_couple

from pyrogram import filters, enums
import random
import datetime

def dt():
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(" ")
    return dt_list

today = str(dt()[0])

@app.on_message(filters.command(["couple", "shipping"]))
@capture_err
async def couple(_, message):
    now = datetime.datetime.now()
    mnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    seconds = (mnight - now).seconds
    hms = str(datetime.timedelta(seconds=seconds))
    remtime = hms.split(':')
    rem_hrs = f"{remtime[0]} hours"
    rem_min = f"{remtime[1]} minutes"
    rem_sec = f"{remtime[2]} seconds"
    if message.chat.type == enums.ChatType.PRIVATE:
        return await message.reply_text("This command only works in groups.")
    try:
        chat_id = message.chat.id
        is_selected = await get_couple(chat_id, today)
        if not is_selected:
            list_of_users = []
            async for i in app.get_chat_members(message.chat.id, limit=50):
                if not i.user.is_bot:
                    list_of_users.append(i.user.id)
            if len(list_of_users) < 2:
                return await message.reply_text("Not enough users")
            c1_id = random.choice(list_of_users)
            c2_id = random.choice(list_of_users)
            while c1_id == c2_id:
                c1_id = random.choice(list_of_users)
            c1_mention = (await app.get_users(int(c1_id))).mention
            c2_mention = (await app.get_users(int(c2_id))).mention
            couple_selection_message = f"""Couple of the day:
{c1_mention} + {c2_mention} = ❤️

New couple of the day may be chosen in {rem_hrs} {rem_min} {rem_sec}"""
            await app.send_message(message.chat.id, text=couple_selection_message)
            couple = {"c1_id": c1_id, "c2_id": c2_id}
            await save_couple(chat_id, today, couple)

        elif is_selected:
            c1_id = int(is_selected["c1_id"])
            c2_id = int(is_selected["c2_id"])
            c1_mention = f"[{(await app.get_users(int(c1_id))).first_name}](tg://user?id={c1_id})"
            c2_mention = f"[{(await app.get_users(int(c2_id))).first_name}](tg://user?id={c2_id})"
            couple_selection_message = f"""Couple of the day has been chosen:
{c1_mention} + {c2_mention} = ❤️

New couple of the day may be chosen in {rem_hrs} {rem_min} {rem_sec}"""
            await app.send_message(message.chat.id, text=couple_selection_message)
    except Exception as e:
        await app.send_message(message.chat.id, text=str(e))
