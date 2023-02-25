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
import SQLaccounts
from plugins.clases.usuarios import usuario

from pyrogram import Client, filters
#from configs import config
from asyncio import sleep
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery
)
import SQLaccounts
from plugins.sql.config import configIdioma




@Client.on_message(filters.command(["start"], prefixes=["/", "."]))
async def start( cl: Client, m: Message):
    username = m.from_user.username
    id = m.from_user.id
    user = usuario(username, id)
    verified = user.buscar()
    if not verified or verified == False:
        agregar = user.agregar()
        if not agregar or agregar == False: return await m.reply('Error al registrar al usuario')
        return await m.reply('<b>Usuario registrado con exito</b>')
    


    await cl.send_video(m.chat.id, "https://pa1.narvii.com/7158/ff23bcf4a488ebc69c641961e3c2fe929852f9f5r1-498-280_hq.gif")
    await cl.send_message(m.chat.id, text=f"""𝐖𝐞𝐥𝐜𝐨𝐦𝐞 @{m.from_user.username} press the buton commands 𝐭𝐨 𝐯𝐢𝐞𝐰 𝐚𝐥𝐥 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬.""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Owner", url="https://t.me/Draxxd30"),InlineKeyboardButton("Commands", callback_data='commansStart')]]))
    
    
