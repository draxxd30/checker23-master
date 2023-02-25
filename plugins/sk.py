import json
import requests
import time
import asyncio
import random
from luhn import verify
from plugins.clases.usuarios import usuario

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from SQLaccounts import run_query


@Client.on_message(filters.command(["sk"], prefixes=["/", "."]))
async def sk(_, m: Message):
    id = m.from_user.id
    username = m.from_user.username
    user = usuario(username, id)
    datos = user.buscar()
    if not datos or datos == False: return await m.reply('<b>Usuario no registrado porfavor registrese con /start</b>')
    if datos[2] == "Free":
        return await m.reply("𝐘𝐨𝐮 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐛𝐞 𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐜𝐨𝐦𝐦𝐚𝐧𝐝")

    key = m.text[len("/sk "):]
    if not key:
        return await m.reply("𝐄𝐧𝐭𝐞𝐫 𝐭𝐡𝐞 𝐤𝐞𝐲 𝐜𝐨𝐫𝐫𝐞𝐜𝐭𝐥𝐲")
    cc = "5339228468176001"
    cvc = "902"
    mes = "06"
    ano = "2028"

    headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
    data ={
    "card[number]": cc,
    "card[cvc]": cvc,
    "card[exp_month]": mes,
    "card[exp_year]": ano
    }

    api = requests.post(f"https://api.stripe.com/v1/tokens", data=data, headers=headers, auth=(key, ""))

    if "Invalid API Key provided" in api.text:
        await m.reply(f"""
        
𝐑𝐞𝐬𝐮𝐥𝐭: 𝐃𝐞𝐚𝐝 ❌
𝐊𝐞𝐲: <code>{key}</code>
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Invalid API Key provided</code>
𝐎𝐰𝐧𝐞𝐫: <code>Draxxd30</code>
        """)
    elif "api_key_expired" in api.text:
        await m.reply(f"""
        
𝐑𝐞𝐬𝐮𝐥𝐭: 𝐃𝐞𝐚𝐝 ❌
𝐊𝐞𝐲: <code>{key}</code>
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>api_key_expired</code>
𝐎𝐰𝐧𝐞𝐫: <code>Draxxd30</code>
        """)
    elif "testmode_charges_only" in api.text:
        await m.reply(f"""
        
𝐑𝐞𝐬𝐮𝐥𝐭: 𝐃𝐞𝐚𝐝 ❌
𝐊𝐞𝐲: <code>{key}</code>
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>testmode_charges_only</code>
𝐎𝐰𝐧𝐞𝐫: <code>Draxxd30</code>
        """)
    elif "test_mode_live_card" in api.text:
        await m.reply(f"""
        
𝐑𝐞𝐬𝐮𝐥𝐭: 𝐃𝐞𝐚𝐝 ❌
𝐊𝐞𝐲: <code>{key}</code>
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>test_mode_live_card</code>
𝐎𝐰𝐧𝐞𝐫: <code>Draxxd30</code>
        """)
    else:
        await m.reply(f"""

𝐑𝐞𝐬𝐮𝐥𝐭: 𝐋𝐢𝐯𝐞 ✅
𝐊𝐞𝐲: <code>{key}</code>
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>SK_Live!</code>    
𝐎𝐰𝐧𝐞𝐫: <code>Draxxd30</code>
""")
