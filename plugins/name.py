import requests
from requests.exceptions import HTTPError, ProxyError
import re
import base64
import os
import time
import json
import string
import random
import httpx
import pymongo
import logging
import pyrogram
from plugins.clases.usuarios import usuario

from pyrogram import Client, filters
#from configs import config
from asyncio import sleep
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from  SQLaccounts import cambiarNombre, run_query

@Client.on_message(filters.command(["name"], prefixes=["/", "."]))
async def name(_, m: Message):
    username = m.from_user.username
    id = m.from_user.id
    user = usuario(username, id)
    datos = user.buscar()
    if not datos or datos == False: return await m.reply('<b>Usuario no registrado porfavor registrese</b>')
    if datos[2] == "Free" or datos[2] == "Premium":
        return await m.reply("𝐘𝐨𝐮 𝐧𝐞𝐞𝐝 𝐭𝐨 𝐛𝐞 𝐚𝐝𝐦𝐢𝐧 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐜𝐨𝐦𝐦𝐚𝐧𝐝")
    
    mensaje = m.text[len("/name "):]
    if not mensaje:
        return await m.reply("""
𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐟𝐨𝐫𝐦𝐚𝐭
𝐅𝐨𝐫𝐦𝐚𝐭: 𝐈𝐃 | 𝐍𝐞𝐰 𝐍𝐚𝐦𝐞
""")
    else:
        mensaje = mensaje.replace("|", " | ")
        mensaje = mensaje.replace("/", " | ")

        if mensaje.find(" | ") != -1:
            split = mensaje.split(" | ")
            if split == [] or len(split) == 0:
                return await m.reply("""
𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐟𝐨𝐫𝐦𝐚𝐭
𝐅𝐨𝐫𝐦𝐚𝐭: 𝐈𝐃 | 𝐍𝐞𝐰 𝐍𝐚𝐦𝐞
""")
            else:
                id = split[0]
                rango = split[1]

                userD = usuario(username, id)
                datos = userD.buscar()
                if datos == False or datos == None: return await m.reply('Error al encontrar el id')
                try:
                    user = datos[1]
                except Exception: return
                if user == 'None': user = 'Not'
                cambio = cambiarNombre(id, rango)
                
                if cambio == "error1":
                    return await m.reply(f"𝐓𝐡𝐞 𝐮𝐬𝐞𝐫 <code>{user}</code> 𝐡𝐚𝐬 𝐚𝐥𝐫𝐞𝐚𝐝𝐲 𝐛𝐞𝐞𝐧 𝐚𝐬𝐬𝐢𝐠𝐧𝐞𝐝 𝐭𝐡𝐞 𝐫𝐚𝐧𝐤 <code>{rango}</code>")
                
                if cambio.find("sucess") != -1:
                    if user == 'Not':
                        user = id
                        return await m.reply(f"""
𝐍𝐚𝐦𝐞 𝐨𝐟 [ <code>{user}</code> ] 𝐮𝐩𝐝𝐚𝐭𝐞𝐝 𝐭𝐨 [ <code>{rango}</code> ]
""")
                    else:
                        await m.reply(f"""
𝐍𝐚𝐦𝐞 𝐨𝐟 <code>{user}</code> 𝐮𝐩𝐝𝐚𝐭𝐞𝐝 𝐭𝐨 [ <code>{rango}</code> ]
""")        
                else:
                    await m.reply("""
𝐍𝐚𝐦𝐞 𝐜𝐡𝐚𝐧𝐠𝐞 𝐞𝐫𝐫𝐨𝐫
""")

        else:
            await m.reply("""
𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐟𝐨𝐫𝐦𝐚𝐭
𝐅𝐨𝐫𝐦𝐚𝐭: 𝐈𝐃 | 𝐍𝐞𝐰 𝐍𝐚𝐦𝐞
""")



    