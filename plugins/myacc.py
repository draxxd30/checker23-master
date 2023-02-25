import json
import requests

import time
import asyncio
import random
from luhn import verify

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
import SQLaccounts
from plugins.clases.usuarios import usuario
        
        
        



@Client.on_message(filters.command(["myacc"], prefixes=["/", "."]))
async def myacc(_,m: Message):
    #ID = m.text[len("/myacc "):]
    nombre = m.from_user.username
    ID = m.from_user.id
    user = usuario(nombre, ID)
    datos = user.buscar()
    if not datos or datos == False: return await m.reply('<b>Usuario no registrado</b>')
    try:
        usuarioN = datos[1]
        rango = datos[2]
        Creditos = datos[3]
        idTG = datos[4]
        rangoP = datos[5]
        rangoPP = f" | {rangoP}"
        if rangoP == None: rangoPP = ""
    except Exception as e:
        return await m.reply('<b>Usuario no registrado</b>')
    
    await m.reply(f"""
𝐈𝐃 :  <code>{idTG}</code> 
𝐔𝐒𝐄𝐑 : <b>@{usuarioN}</b>
𝐂𝐇𝐀𝐓 𝐓𝐘𝐏𝐄 : <code>{m.chat.type.capitalize()}</code>
𝐒𝐓𝐀𝐓𝐔𝐒 : <b>{rango}{rangoPP}</b>
𝐂𝐑𝐄𝐃𝐈𝐓𝐒 : <b><code>{Creditos}</code></b>
𝐁𝐎𝐓 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐃 𝐁𝐘 : <code>Draxxd30</code>
""")