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
LinkWebBot = "file:///C:/Users/Felipe/OneDrive/Escritorio/Pagina/Index.html"


@Client.on_message(filters.command(["web"], prefixes=["/", "."]))
async def web(_, m: Message):
    id = m.from_user.id
    username = m.from_user.username
    user = usuario(username, id)
    datos = user.buscar()
    if not datos or datos == False: return await m.reply('<b>Usuario no registrado porfavor registrese con /start</b>')
    if datos[2] != "Owner":
        return await m.reply("<b>Necesita ser Owner para utilizar este comando</b>")
    await m.reply(f""" <b>
Link de le la web:

<code>{LinkWebBot}</code>
    
</b>""")