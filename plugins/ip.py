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

@Client.on_message(filters.command(["ip"], prefixes=["/", "."]))
async def ip(_, m: Message):
    id = m.from_user.id
    username = m.from_user.username
    user = usuario(username, id)
    datos = user.buscar()
    if not datos or datos == False: return await m.reply('Usuario no registrado porfvor registrese con /start')
    ip = m.text[len('/ip '):]
    if not ip:
        return await m.reply("Coloque una ip de esta forma <code>/ip 1.1.1.1</code>")
    time1 = time.perf_counter
    
    
    apiIP = requests.get(f"http://ip-api.com/json/{ip}").json()
    status1 = apiIP["status"]
    if status1 == "success":
        country = apiIP["country"]
        countryCode = apiIP["countryCode"]
        region = apiIP["regionName"]
        ciudad = apiIP["city"]
        latitud = apiIP["lat"]
        longitud = apiIP["lon"]
        zonaHoraria = apiIP["timezone"]
        isp = apiIP["isp"]
        org = apiIP["org"]
        asn = apiIP["as"]
    else:
        return await m.reply("<b>Esta IP es invalida</b>")
    apiScam = requests.get(f"https://api11.scamalytics.com/felipe.castro/?key=ae1f15c62b7d27246854452e8c7c8244&ip={ip}&test=1").json()
    status = apiScam["status"]
    if status == "ok":
        ipF = apiScam["ip"]
        risk = apiScam["risk"]
        score = apiScam["score"]
        timeOk = time.perf_counter
        respuesta = (f"""<b>
ip: <code>{ipF}</code>
Fraude: {risk} [{score}]
as: {asn}
ISP: {isp}
Organizacion: {org}
Zona horaria: {zonaHoraria}
Ubicacion: {ciudad}, {region}, {country} [{countryCode}]
Coordenadas: <code>{latitud}, {longitud}</code>

Checkeada por: {m.from_user.username}
Owner: @Draxxd30
</b>""")
        
        await m.reply(respuesta)
    else:
        await m.reply("<b>Esta IP es invalida</b>")
    

