import json
import requests
import time
import asyncio
from plugins.clases.usuarios import usuario

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import (
   Message,
   InlineKeyboardButton,
   InlineKeyboardMarkup,
   )


@Client.on_message(filters.command(["bin"], prefixes=["/", "."]))
async def bin(_, m: Message):
    username = m.from_user.username
    id = m.from_user.id
    user = usuario(username, id)
    datos = user.buscar()
    if not datos or datos == False: return await m.reply('<b>Usuario no registrado porvafor registrese con /start</b>')
    
    BIN = m.text[len("/bin "): 11]
    
    if len(BIN) < 6:
        return await m.reply("❌ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐞𝐧𝐭𝐞𝐫 𝐚 𝐯𝐚𝐥𝐢𝐝 𝐁𝐢𝐧")
    if not BIN:
       return await m.reply("❌ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐞𝐧𝐭𝐞𝐫 𝐚 𝐯𝐚𝐥𝐢𝐝 𝐁𝐢𝐧")

    inputm = m.text.split(None, 1)[1]
    bincode = 6

    BIN = inputm[:bincode]
    
    gateBIN = requests.get(f"https://binlookup-1.andrexxone.repl.co/index.php?bin={BIN}").json()
    if gateBIN["status"] == True:
        status = "𝐕𝐚𝐥𝐢𝐝 𝐁𝐢𝐧"
        bin = gateBIN["query"]  
        brand = gateBIN["brand"]
        type = gateBIN["type"]
        level = gateBIN["level"]
        bank = gateBIN['bank']["name"];
        pais = gateBIN["country"]["ISO2"]
        country = gateBIN["country"]["name"]
        emojiCountry = gateBIN["country"]["flag"];
        currency = gateBIN["country"]["currency"]


        
        
        resultados = (f"""
✅ {status}
↯ 𝐁𝐢𝐧: <b><code>{bin}</code></b>
↯ 𝐈𝐧𝐟𝐨: <code>{brand} - {type} - {level}</code>
↯ 𝐁𝐚𝐧𝐤: <code>{bank}</code> 
↯ 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} {emojiCountry}</code> - <code>{currency}</code>
↯ 𝐎𝐰𝐧𝐞𝐫: <code><i>Draxxd30</i></code>
""")

        
        return await m.reply(resultados)
    else:
        return await m.reply("❌ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐞𝐧𝐭𝐞𝐫 𝐚 𝐯𝐚𝐥𝐢𝐝 𝐁𝐢𝐧")

