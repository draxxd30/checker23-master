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

@Client.on_message(filters.command(["rnd", "random"], prefixes=["/", "."]))
async def rnd(_, m: Message):
    username = m.from_user.username
    id = m.from_user.id
    user = usuario(username, id)
    datos = user.buscar()
    if not datos or datos == False: return await m.reply('<b>Usuario no registrado porfavor registrese con /start</b>')
    
    mesageF = m.text
    mesage = mesageF.replace("random", "rnd")
    country = mesage[len("/rnd "):]
    api = requests.get(f"https://randomuser.me/api/?nat={country}").json()
    nombre = api["results"][0]["name"]["first"]
    apellido = api["results"][0]["name"]["last"]
    zipcode = api["results"][0]["location"]["postcode"]
    pais = api["results"][0]["location"]["country"]
    calleN = api["results"][0]["location"]["street"]["name"]
    Callet = api["results"][0]["location"]["street"]["number"]
    ciudad = api["results"][0]["location"]["city"]
    estado = api["results"][0]["location"]["state"]
    email = api["results"][0]["email"]
    edad = api["results"][0]["dob"]["age"]
    celular = api["results"][0]["cell"]
    respuesta = (f"""
 
-------------------------------------------------   
<b>nombre:</b> <code>{nombre}</code> <code>{apellido}</code>
<b>Email:</b> <code>{email}</code>
<b>Edad: {edad}</b>
<b>Celular:</b> <code>{celular}</code>
<b>Pais:</b>  <code>{pais}</code>
<b>Estado:</b> <code>{estado}</code>
<b>Ciudad:</b> <code>{ciudad}</code>
<b>Calle:</b> <code>{calleN}, {Callet}</code>
<b>Zip:</b> <code>{zipcode}</code>
-------------------------------------------------
    
    
    """)
    await m.reply(respuesta)
