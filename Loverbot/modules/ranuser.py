import requests
import random
import os
import json
from datetime import date
from Loverbot import telethn as tbot
from Loverbot.events import register

@register(pattern="^[!/.]ranuser")
async def gen(event):
	fake = Faker()
	bhurr = await event.reply("ɢᴇɴᴇʀᴀᴛɪɴɢ ɪɴꜰᴏ...")
	yr = date.today().year
	cyr = int(yr)
	inf = "https://randomuser.me/api"
	rinf = requests.get(inf)
	injs = rinf.json()
	tt, fn, ln = injs['results'][0]['name']['title'], injs['results'][0]['name']['first'], injs['results'][0]['name']['last']
	gender = injs['results'][0]['gender']
	name = f"{tt} {fn} {ln}"
	snu, snam = injs['results'][0]['location']['street']['number'], injs['results'][0]['location']['street']['name']
	street = f"{snu}, {snam}"
	city = injs['results'][0]['location']['city']
	state = injs['results'][0]['location']['state']
	country = injs['results'][0]['location']['country']
	pscd = injs['results'][0]['location']['postcode']
	email = injs['results'][0]['email'].replace("example", "email")
	cell = injs['results'][0]['cell']
	ccnum = fake.credit_card_number(card_type='visa16')
	ccexp = fake.credit_card_expire()
	cvv = random.choice(range(100,999))
	poli = f"https://fakeface.rest/face/json?gender={gender}&minimum_age=18&maximum_age=40"
	rpoli = requests.get(poli)
	poinjs = rpoli.json()
	poto = poinjs['image_url']
	pyr = poinjs['age']
	dyr = cyr - int(pyr)
	dobin = injs['results'][0]['dob']['date']
	dfm = dobin[:10][4:]
	dob = f"{dyr}{dfm}"
	capt = f"**ɴᴀᴍᴇ:** {name}\n**ᴅᴏʙ:** {dob}\n**sᴛʀᴇᴇᴛ:** {street}\n**ᴄɪᴛʏ:** {city}\n**sᴛᴀᴛᴇ:** {state}\n**ᴄᴏᴜɴᴛʀʏ:** {country}\n**ᴘᴏsᴛᴀʟ ᴄᴏᴅᴇ:** {pscd}\n**ᴇᴍᴀɪʟ:** {email}\n**ᴘʜᴏɴᴇ:** {cell}\n\n**ᴄᴄ ɪɴꜰᴏ:**\n    **ᴄᴄ ɴᴜᴍʙᴇʀ:** {ccnum}\n    **ᴇxᴘɪʀʏ:** {ccexp}\n    **ᴄᴠᴠ:** {cvv}"
	await bhurr.delete()
	await tbot.send_file(event.chat_id, poto, caption=capt, reply_to=event.reply_to_msg_id, force_document=False)

__mod_name__ = "Rᴀɴᴜsᴇʀ"
__help__ = """Rᴀɴᴅᴏᴍ Usᴇʀ Iɴғᴏ Gᴇɴᴇʀᴀᴛᴏʀ

ᴜsᴀɢᴇ:
> /ranuser | Gᴇɴᴇʀᴀᴛᴇs Fᴀᴋᴇ Rᴀɴᴅᴏᴍ Usᴇʀ Iɴғᴏ (ɪᴍᴀɢᴇ ɪs ɢᴇɴᴇʀᴀᴛᴇᴅ ғʀᴏᴍ [ᴛʜɪsᴘᴇʀsᴏɴᴅᴏᴇsɴᴏᴛᴇxɪsᴛ.ᴄᴏᴍ](https://www.thispersondoesnotexist.com/))
"""
