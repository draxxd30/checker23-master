import requests
def buscarEnT(res, primer, final):
    try:
        inicio = res.index( primer ) + len( primer )
        fin = res.index( final, inicio )
        return res[inicio:fin]
    except ValueError:
        return None
    
def get_cc(t): 
    t1 = t.replace("|", " ")
    t = t1.replace("/", " ")
    list = str.split(t)
    cc, mes, año, cvv = "", "", "", ""
    for parte in list:
        try:
            if parte.isdigit():
                if len(parte) == 16: cc = parte
                elif len(parte) == 1 or len(parte) == 2: 
                    if parte[0] == "1" or parte[0] == "0": mes = parte
                    elif parte[0] == "2": año = parte
                elif len(parte) == 4: 
                    if parte[0] == "2": año = parte
                elif len(parte) == 3: cvv = parte
        except: continue
    #texto = f"{cc}|{mes}|{año}|{cvv}"
    return cc, mes, año, cvv
def luhn(Card):
    Numeros = list(map(int, Card))
    n1 = sum(Numeros[-1::-2]) #Suma de pares
    n2 = sum([sum(divmod(2 * l, 10)) for l in Numeros[-2::-2]]) #Numeros impares
    rest = (n1 + n2) % 10 #resto de division de la suma
    if rest == 0: return True
    else: return False
def bininfo(cc):
    BIN = cc[:6]
    gateBIN = requests.get(f"https://binlookup-1.andrexxone.repl.co/index.php?bin={BIN}").json()    
    try:
        bin = gateBIN["query"]  
        brand = gateBIN["brand"]
        type = gateBIN["type"]
        level = gateBIN["level"]
        bank = gateBIN['bank']["name"];
        pais = gateBIN["country"]["ISO2"]
        country = gateBIN["country"]["name"]
        emojiCountry = gateBIN["country"]["flag"];
        currency = gateBIN["country"]["currency"]

        if bank == "":
            bank = "/"
        elif brand == "":
            brand = "/"
        elif type == "":
            type = "/"
        elif level == "":
            level = "/"
        elif pais == "":
            pais = "/"
        elif country == "":
            country = "/"
        elif emojiCountry == "":
            emojiCountry = "/"
        elif currency == "":
            currency = "/"
        return bin, brand, type, level, bank, pais, country, emojiCountry, currency
    except Exception as a:
        return