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

gate = "Shopify+B3 NoCap"
emojis1 = ["🙈", "💦", "🌏", "🐸", "🐧"]
emojis2 = ["😠", "☔", "☀", "🌈"]
rnd_emoji2 = random.choice(emojis2)
r = requests.Session()
#@Client.on_message(filters.command(["b3"], prefixes=["/", "."]))
#async def premium(_, m: Message):
start_time = time.time()
#user = m.from_user.username
#id = m.from_user.id
#user = usuario(nombre=user, id=id)
#rango = user.buscar()
#if not rango or rango == False: return await m.reply('<b>Usuario no registrado porfavor registrese</b>')
#if rango[2] == 'Free':
#    return await m.reply('<b>Necesita ser Premium para utilizar este gate</b>')
#try:
#    cc, mes, año, cvv = get_cc(m.text)
#    veri = luhn(cc)
#    if not cc or not mes or not año or not cvv: return await m.reply('<b>Formato invalido</b>')
#    if veri == False: return await m.reply("<b>Algoritmo Luhn invalido ❌</b>")
#except Exception:
#    return await m.reply("<b>Formato invalido\nCC|MES|AÑO|CVV</b>")
#respuesta = await m.reply(f"""<b>Checkeando CC | ⏳</b>""")
#fake = Faker()
#email = fake.ascii_free_email()

r1_headers = {
    'Host': 'cuboss.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36 CCleaner/108.0.19667.127',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1'
}

r1 = r.get("https://cuboss.com/shop/cuboss-sticker-c/", headers=r1_headers)
product_id = buscar(r1.text, '<div id="product-', '"')
print(product_id)
if not product_id: print(r1.text)

data_r1_2 = {
    'quantity': '1',
    'add-to-cart': product_id
}

r1_2 = r.post("https://cuboss.com/shop/cuboss-sticker-c/", data=data_r1_2, headers=r1_headers)
if not r1_2: print('Error1.2')

data_r2 = "JTdCJTIydjIlMjIlM0ExJTJDJTIyaWQlMjIlM0ElMjI0YjUwNzhjMGU2MmM5MWZhMzEwYjdhNTk5MWM1NjYyNyUyMiUyQyUyMnQlMjIlM0E3LjElMkMlMjJ0YWclMjIlM0ElMjI0LjUuNDIlMjIlMkMlMjJzcmMlMjIlM0ElMjJqcyUyMiUyQyUyMmElMjIlM0FudWxsJTJDJTIyYiUyMiUzQSU3QiUyMmElMjIlM0ElMjJodHRwcyUzQSUyRiUyRl95Y054M3EwZTF3d2VHcVV0VHo5eEJaTjJpMmM3c3dtanR1VXRjMXRPMUUuZzJ1OS1ocVp2R0lxWUpjUGxQZndKQWYtdjNSZ3lLX3gxTnBwekFsQTEyTSUyRm56RmROLVlIaWZwNVA0and3MWc1UEI5Z0w1a2UzbHpNczJsNV9MVG1jS1ElMkZucW5aMGdOY1JRZUhkOWNpdEFMT2VIVVQxZ3FnbGwwbGhNWGJZMzBxZTlnJTJGJTIyJTJDJTIyYiUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGX3ljTngzcTBlMXd3ZUdxVXRUejl4QlpOMmkyYzdzd21qdHVVdGMxdE8xRS5nMnU5LWhxWnZHSXFZSmNQbFBmd0pBZi12M1JneUtfeDFOcHB6QWxBMTJNJTJGX2RZRTM3M1JEQXVlYlUyaGRFSDNWei1yY0JwSTh4bGNhZWdUSjFfa3k4NCUyRiUyMiUyQyUyMmMlMjIlM0ElMjI3ejY0bEpfRTM2RXVGYm5VTUd6Q1lGQTVyNm1hcVN3X0N0NGdqWGVHWlA0JTIyJTJDJTIyZCUyMiUzQSUyMjAxMTU3NDI4LWExNDEtNGM5Yy05YzI3LTczMmI2MmYwNmVmNzIzYzdjOSUyMiUyQyUyMmUlMjIlM0ElMjI5Y2RiYzc5Yy1jMzZiLTRmNmYtYWQ5NC1kYTA2OTM2YjQyM2JmYWJlZDYlMjIlMkMlMjJmJTIyJTNBZmFsc2UlMkMlMjJnJTIyJTNBdHJ1ZSUyQyUyMmglMjIlM0F0cnVlJTJDJTIyaSUyMiUzQSU1QiUyMmxvY2F0aW9uJTIyJTVEJTJDJTIyaiUyMiUzQSU1QiU1RCUyQyUyMm4lMjIlM0EyNS43MDAwMDAwMDI5ODAyMzIlMkMlMjJ1JTIyJTNBJTIyY3Vib3NzLmNvbSUyMiUyQyUyMnYlMjIlM0ElMjJjdWJvc3MuY29tJTIyJTdEJTJDJTIyaCUyMiUzQSUyMmY3ZDg1MjM4ODE5MzFjYjg1OTlmJTIyJTdE"
r2 = r.post("https://m.stripe.com/6", data=data_r2).json()
#print(r2.text)
try:
    muid = r2["muid"]
    sid = r2["sid"]
    guid = r2["guid"]
except Exception as e: print(f'Error2: {e}')

r3_headers = {
    'authority': 'cuboss.com',
    'method': 'GET',
    'path': '/checkout/',
    'scheme': 'https',
    'accept': 'application/signed-exchange;v=b3;q=0.7,*/*;q=0.8',
    'accept-language': 'es-ES,es;q=0.9',
    'purpose': 'prefetch',
    'referer': 'https://cuboss.com/cart/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
r3 = r.get("https://cuboss.com/checkout/", headers=r3_headers)
print(r3.text)

