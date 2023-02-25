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


#------------Inicio defs-----------------#
def gen0(cc, mes, ano, cvv):
    
    global ccgen
    global mesgen
    global ccano
    global cvvgen

    result = ""
    while result != "True":
        numeros = "1234567890"
        lista = list(numeros)
        random.shuffle(lista)
        resultados = ''.join(lista)
        resultados = cc + resultados
        if cc[0] == '3':
            ccgen = resultados[0:15]
        else:
            ccgen = resultados[0:16]

        if mes == "x":
            mesgen = random.randint(1, 12)
            if len(str(mesgen)) == 1:
                mesgen = str("0") + str(mesgen)
        elif mes == "xx":
            mesgen = random.randint(1, 12)
            if len(str(mesgen)) == 1:
                mesgen = str("0") + str(mesgen)
        elif mes == "xxx":
            mesgen = random.randint(1, 12)
            if len(str(mesgen)) == 1:
                mesgen = str("0") + str(mesgen)
        elif mes == "xxxx":
            mesgen = random.randint(1, 12)
            if len(str(mesgen)) == 1:
                mesgen = str("0") + str(mesgen)
        elif mes == "rnd":
            mesgen = random.randint(1, 12)
            if len(str(mesgen)) == 1:
                mesgen = str("0") + str(mesgen)
        elif mes == "":
            mesgen = random.randint(1, 12)
            if len(str(mesgen)) == 1:
                mesgen = str("0") + str(mesgen)
        else:
            mesgen = mes
            if len(str(mesgen)) == 1:
                mesgen = str("0") + str(mesgen)

        if ano == 'xxxx':
            ccano = random.randint(2023, 2032)
        elif ano == 'xxx':
            ccano = random.randint(2023, 2032)
        elif ano == 'xx':
            ccano = random.randint(2023, 2032)
        elif ano == '20xx':
            ccano = random.randint(2023, 2032)
        elif ano == '202x':
            ccano = random.randint(2023, 2032)
        elif ano == "rnd":
            ccano = random.randint(2023, 2032)

        else:
            ccano = ano
            if len(str(ccano)) == 2:
                ccano = str("20") + str(ccano)

        if cvv == 'xxx' or "" or "rnd":
            if cc[0] == "3":
                cvvgen = random.randint(1000, 9999)
            else:
                cvvgen = random.randint(100, 999)
        else:
            cvvgen = cvv

        veri = verify(ccgen)
        if veri == False:
            result = "False"
        if veri == True:
            result = "True"
            return ccgen, mesgen, ccano, cvvgen
    
def gen1(cc, mes, ano, cvv):
    
    global ccgen1
    global mesgen1
    global ccano1
    global cvvgen1

    result1 = ""
    while result1 != "True":
        numeros = "1234567890"
        lista = list(numeros)
        random.shuffle(lista)
        resultados = ''.join(lista)
        resultados = cc + resultados
        if cc[0] == '3':
            ccgen1 = resultados[0:15]
        else:
            ccgen1 = resultados[0:16]

        if mes == "x":
            mesgen1 = random.randint(1, 12)
            if len(str(mesgen1)) == 1:
                mesgen1 = str("0") + str(mesgen1)
        elif mes == "xx":
            mesgen1 = random.randint(1, 12)
            if len(str(mesgen1)) == 1:
                mesgen1 = str("0") + str(mesgen1)
        elif mes == "xxx":
            mesgen1 = random.randint(1, 12)
            if len(str(mesgen1)) == 1:
                mesgen1 = str("0") + str(mesgen1)
        elif mes == "xxxx":
            mesgen1 = random.randint(1, 12)
            if len(str(mesgen1)) == 1:
                mesgen1 = str("0") + str(mesgen1)
        elif mes == "rnd":
            mesgen1 = random.randint(1, 12)
            if len(str(mesgen1)) == 1:
                mesgen1 = str("0") + str(mesgen1)
        elif mes == "":
            mesgen1 = random.randint(1, 12)
            if len(str(mesgen1)) == 1:
                mesgen1 = str("0") + str(mesgen1)
        else:
            mesgen1 = mes
            if len(str(mesgen1)) == 1:
                mesgen1 = str("0") + str(mesgen1)

        if ano == 'xxxx':
            ccano1 = random.randint(2023, 2032)
        elif ano == 'xxx':
            ccano1 = random.randint(2023, 2032)
        elif ano == 'xx':
            ccano1 = random.randint(2023, 2032)
        elif ano == '20xx':
            ccano1 = random.randint(2023, 2032)
        elif ano == '202x':
            ccano1 = random.randint(2023, 2032)
        elif ano == "rnd":
            ccano1 = random.randint(2023, 2032)

        else:
            ccano1 = ano
            if len(str(ccano1)) == 2:
                ccano1 = str("20") + str(ccano1)

        if cvv == 'xxx' or "" or "rnd":
            if cc[0] == "3":
                cvvgen1 = random.randint(1000, 9999)
            else:
                cvvgen1 = random.randint(100, 999)
        else:
            cvvgen1 = cvv

        veri1 = verify(ccgen1)
        if veri1 == False:
            result1 = "False"
        if veri1 == True:
            result1 = "True"
            return ccgen1, mesgen1, ccano1, cvvgen1

def gen2(cc, mes, ano, cvv):
    
    global ccgen2
    global mesgen2
    global ccano2
    global cvvgen2

    result2 = ""
    while result2 != "True":
        numeros = "1234567890"
        lista = list(numeros)
        random.shuffle(lista)
        resultados = ''.join(lista)
        resultados = cc + resultados
        if cc[0] == '3':
            ccgen2 = resultados[0:15]
        else:
            ccgen2 = resultados[0:16]

        if mes == "x":
            mesgen2 = random.randint(1, 12)
            if len(str(mesgen2)) == 1:
                mesgen2 = str("0") + str(mesgen2)
        elif mes == "xx":
            mesgen2 = random.randint(1, 12)
            if len(str(mesgen2)) == 1:
                mesgen2 = str("0") + str(mesgen2)
        elif mes == "xxx":
            mesgen2 = random.randint(1, 12)
            if len(str(mesgen2)) == 1:
                mesgen2 = str("0") + str(mesgen2)
        elif mes == "xxxx":
            mesgen2 = random.randint(1, 12)
            if len(str(mesgen2)) == 1:
                mesgen2 = str("0") + str(mesgen2)
        elif mes == "rnd":
            mesgen2 = random.randint(1, 12)
            if len(str(mesgen2)) == 1:
                mesgen2 = str("0") + str(mesgen2)
        elif mes == "":
            mesgen2 = random.randint(1, 12)
            if len(str(mesgen2)) == 1:
                mesgen2 = str("0") + str(mesgen2)
        else:
            mesgen2 = mes
            if len(str(mesgen2)) == 1:
                mesgen2 = str("0") + str(mesgen2)

        if ano == 'xxxx':
            ccano2 = random.randint(2023, 2032)
        elif ano == 'xxx':
            ccano2 = random.randint(2023, 2032)
        elif ano == 'xx':
            ccano2 = random.randint(2023, 2032)
        elif ano == '20xx':
            ccano2 = random.randint(2023, 2032)
        elif ano == '202x':
            ccano2 = random.randint(2023, 2032)
        elif ano == "rnd":
            ccano2 = random.randint(2023, 2032)

        else:
            ccano2 = ano
            if len(str(ccano2)) == 2:
                ccano2 = str("20") + str(ccano2)

        if cvv == 'xxx' or "" or "rnd":
            if cc[0] == "3":
                cvvgen2 = random.randint(1000, 9999)
            else:
                cvvgen2 = random.randint(100, 999)
        else:
            cvvgen2 = cvv

        veri2 = verify(ccgen2)
        if veri2 == False:
            result2 = "False"
        if veri2 == True:
            result2 = "True"
            return ccgen2, mesgen2, ccano2, cvvgen2

def gen3(cc, mes, ano, cvv):
    
    global ccgen3
    global mesgen3
    global ccano3
    global cvvgen3
    
    result3 = ""
    while result3 != "True":
        numeros = "1234567890"
        lista = list(numeros)
        random.shuffle(lista)
        resultados = ''.join(lista)
        resultados = cc + resultados
        if cc[0] == '3':
            ccgen3 = resultados[0:15]
        else:
            ccgen3 = resultados[0:16]

        if mes == "x":
            mesgen3 = random.randint(1, 12)
            if len(str(mesgen3)) == 1:
                mesgen3 = str("0") + str(mesgen3)
        elif mes == "xx":
            mesgen3 = random.randint(1, 12)
            if len(str(mesgen3)) == 1:
                mesgen3 = str("0") + str(mesgen3)
        elif mes == "xxx":
            mesgen3 = random.randint(1, 12)
            if len(str(mesgen3)) == 1:
                mesgen3 = str("0") + str(mesgen3)
        elif mes == "xxxx":
            mesgen3 = random.randint(1, 12)
            if len(str(mesgen3)) == 1:
                mesgen3 = str("0") + str(mesgen3)
        elif mes == "rnd":
            mesgen3 = random.randint(1, 12)
            if len(str(mesgen3)) == 1:
                mesgen3 = str("0") + str(mesgen3)
        elif mes == "":
            mesgen3 = random.randint(1, 12)
            if len(str(mesgen3)) == 1:
                mesgen3 = str("0") + str(mesgen3)
        else:
            mesgen3 = mes
            if len(str(mesgen3)) == 1:
                mesgen3 = str("0") + str(mesgen3)

        if ano == 'xxxx':
            ccano3 = random.randint(2023, 2032)
        elif ano == 'xxx':
            ccano3 = random.randint(2023, 2032)
        elif ano == 'xx':
            ccano3 = random.randint(2023, 2032)
        elif ano == '20xx':
            ccano3 = random.randint(2023, 2032)
        elif ano == '202x':
            ccano3 = random.randint(2023, 2032)
        elif ano == "rnd":
            ccano3 = random.randint(2023, 2032)

        else:
            ccano3 = ano
            if len(str(ccano3)) == 2:
                ccano3 = str("20") + str(ccano3)

        if cvv == 'xxx' or "" or "rnd":
            if cc[0] == "3":
                cvvgen3 = random.randint(1000, 9999)
            else:
                cvvgen3 = random.randint(100, 999)
        else:
            cvvgen3 = cvv

        veri3 = verify(ccgen3)
        if veri3 == False:
            result3 = "False"
        if veri3 == True:
            result3 = "True"
            return ccgen3, mesgen3, ccano3, cvvgen3

def gen4(cc, mes, ano, cvv):    
    
    global ccgen4
    global mesgen4
    global ccano4
    global cvvgen4
    
    result4 = ""
    while result4 != "True":
        numeros = "1234567890"
        lista = list(numeros)
        random.shuffle(lista)
        resultados = ''.join(lista)
        resultados = cc + resultados
        if cc[0] == '3':
            ccgen4 = resultados[0:15]
        else:
            ccgen4 = resultados[0:16]

        if mes == "x":
            mesgen4 = random.randint(1, 12)
            if len(str(mesgen4)) == 1:
                mesgen4 = str("0") + str(mesgen4)
        elif mes == "xx":
            mesgen4 = random.randint(1, 12)
            if len(str(mesgen4)) == 1:
                mesgen4 = str("0") + str(mesgen4)
        elif mes == "xxx":
            mesgen4 = random.randint(1, 12)
            if len(str(mesgen4)) == 1:
                mesgen4 = str("0") + str(mesgen4)
        elif mes == "xxxx":
            mesgen4 = random.randint(1, 12)
            if len(str(mesgen4)) == 1:
                mesgen4 = str("0") + str(mesgen4)
        elif mes == "rnd":
            mesgen4 = random.randint(1, 12)
            if len(str(mesgen4)) == 1:
                mesgen4 = str("0") + str(mesgen4)
        elif mes == "":
            mesgen4 = random.randint(1, 12)
            if len(str(mesgen4)) == 1:
                mesgen4 = str("0") + str(mesgen4)
        else:
            mesgen4 = mes
            if len(str(mesgen4)) == 1:
                mesgen4 = str("0") + str(mesgen4)

        if ano == 'xxxx':
            ccano4 = random.randint(2023, 2032)
        elif ano == 'xxx':
            ccano4 = random.randint(2023, 2032)
        elif ano == 'xx':
            ccano4 = random.randint(2023, 2032)
        elif ano == '20xx':
            ccano4 = random.randint(2023, 2032)
        elif ano == '202x':
            ccano4 = random.randint(2023, 2032)
        elif ano == "rnd":
            ccano4 = random.randint(2023, 2032)

        else:
            ccano4 = ano
            if len(str(ccano4)) == 2:
                ccano4 = str("20") + str(ccano4)

        if cvv == 'xxx' or "" or "rnd":
            if cc[0] == "3":
                cvvgen4 = random.randint(1000, 9999)
            else:
                cvvgen4 = random.randint(100, 999)
        else:
            cvvgen4 = cvv

        veri4 = verify(ccgen4)
        if veri4 == False:
            result4 = "False"
        if veri4 == True:
            result4 = "True"
            return ccgen4, mesgen4, ccano4, cvvgen4

def gen5(cc, mes, ano, cvv):
    
    global ccgen5
    global mesgen5
    global ccano5
    global cvvgen5
    
    result5 = ""
    while result5 != "True":
        numeros = "1234567890"
        lista = list(numeros)
        random.shuffle(lista)
        resultados = ''.join(lista)
        resultados = cc + resultados
        if cc[0] == '3':
            ccgen5 = resultados[0:15]
        else:
            ccgen5 = resultados[0:16]

        if mes == "x":
            mesgen5 = random.randint(1, 12)
            if len(str(mesgen5)) == 1:
                mesgen5 = str("0") + str(mesgen5)
        elif mes == "xx":
            mesgen5 = random.randint(1, 12)
            if len(str(mesgen5)) == 1:
                mesgen5 = str("0") + str(mesgen5)
        elif mes == "xxx":
            mesgen5 = random.randint(1, 12)
            if len(str(mesgen5)) == 1:
                mesgen5 = str("0") + str(mesgen5)
        elif mes == "xxxx":
            mesgen5 = random.randint(1, 12)
            if len(str(mesgen5)) == 1:
                mesgen5 = str("0") + str(mesgen5)
        elif mes == "rnd":
            mesgen5 = random.randint(1, 12)
            if len(str(mesgen5)) == 1:
                mesgen5 = str("0") + str(mesgen5)
        elif mes == "":
            mesgen5 = random.randint(1, 12)
            if len(str(mesgen5)) == 1:
                mesgen5 = str("0") + str(mesgen5)
        else:
            mesgen5 = mes
            if len(str(mesgen5)) == 1:
                mesgen5 = str("0") + str(mesgen5)

        if ano == 'xxxx':
            ccano5 = random.randint(2023, 2032)
        elif ano == 'xxx':
            ccano5 = random.randint(2023, 2032)
        elif ano == 'xx':
            ccano5 = random.randint(2023, 2032)
        elif ano == '20xx':
            ccano5 = random.randint(2023, 2032)
        elif ano == '202x':
            ccano5 = random.randint(2023, 2032)
        elif ano == "rnd":
            ccano5 = random.randint(2023, 2032)

        else:
            ccano5 = ano
            if len(str(ccano5)) == 2:
                ccano5 = str("20") + str(ccano5)

        if cvv == 'xxx' or "" or "rnd":
            if cc[0] == "3":
                cvvgen5 = random.randint(1000, 9999)
            else:
                cvvgen5 = random.randint(100, 999)
        else:
            cvvgen5 = cvv

        veri5 = verify(ccgen5)
        if veri5 == False:
            result5 = "False"
        if veri5 == True:
            result5 = "True"
            return ccgen5, mesgen5, ccano5, cvvgen5

def gen6(cc, mes, ano, cvv):
    
    global ccgen6
    global mesgen6
    global ccano6
    global cvvgen6
        
    result6 = ""
    while result6 != "True":
        numeros = "1234567890"
        lista = list(numeros)
        random.shuffle(lista)
        resultados = ''.join(lista)
        resultados = cc + resultados
        if cc[0] == '3':
            ccgen6 = resultados[0:15]
        else:
            ccgen6 = resultados[0:16]

        if mes == "x":
            mesgen6 = random.randint(1, 12)
            if len(str(mesgen6)) == 1:
                mesgen6 = str("0") + str(mesgen6)
        elif mes == "xx":
            mesgen6 = random.randint(1, 12)
            if len(str(mesgen6)) == 1:
                mesgen6 = str("0") + str(mesgen6)
        elif mes == "xxx":
            mesgen6 = random.randint(1, 12)
            if len(str(mesgen6)) == 1:
                mesgen6 = str("0") + str(mesgen6)
        elif mes == "xxxx":
            mesgen6 = random.randint(1, 12)
            if len(str(mesgen6)) == 1:
                mesgen6 = str("0") + str(mesgen6)
        elif mes == "rnd":
            mesgen6 = random.randint(1, 12)
            if len(str(mesgen6)) == 1:
                mesgen6 = str("0") + str(mesgen6)
        elif mes == "":
            mesgen6 = random.randint(1, 12)
            if len(str(mesgen6)) == 1:
                mesgen6 = str("0") + str(mesgen6)
        else:
            mesgen6 = mes
            if len(str(mesgen6)) == 1:
                mesgen6 = str("0") + str(mesgen6)

        if ano == 'xxxx':
            ccano6 = random.randint(2023, 2032)
        elif ano == 'xxx':
            ccano6 = random.randint(2023, 2032)
        elif ano == 'xx':
            ccano6 = random.randint(2023, 2032)
        elif ano == '20xx':
            ccano6 = random.randint(2023, 2032)
        elif ano == '202x':
            ccano6 = random.randint(2023, 2032)
        elif ano == "rnd":
            ccano6 = random.randint(2023, 2032)

        else:
            ccano6 = ano
            if len(str(ccano6)) == 2:
                ccano6 = str("20") + str(ccano6)

        if cvv == 'xxx' or "" or "rnd":
            if cc[0] == "3":
                cvvgen6 = random.randint(1000, 9999)
            else:
                cvvgen6 = random.randint(100, 999)
        else:
            cvvgen6 = cvv

        veri6 = verify(ccgen6)
        if veri6 == False:
            result6 = "False"
        if veri6 == True:
            result6 = "True"
            return ccgen6, mesgen6, ccano6, cvvgen6

def gen7(cc, mes, ano, cvv):   
    
    global ccgen7
    global mesgen7
    global ccano7
    global cvvgen7
        
    result7 = ""
    while result7 != "True":
        numeros = "1234567890"
        lista = list(numeros)
        random.shuffle(lista)
        resultados = ''.join(lista)
        resultados = cc + resultados
        if cc[0] == '3':
            ccgen7 = resultados[0:15]
        else:
            ccgen7 = resultados[0:16]

        if mes == "x":
            mesgen7 = random.randint(1, 12)
            if len(str(mesgen7)) == 1:
                mesgen7 = str("0") + str(mesgen7)
        elif mes == "xx":
            mesgen7 = random.randint(1, 12)
            if len(str(mesgen7)) == 1:
                mesgen7 = str("0") + str(mesgen7)
        elif mes == "xxx":
            mesgen7 = random.randint(1, 12)
            if len(str(mesgen7)) == 1:
                mesgen7 = str("0") + str(mesgen7)
        elif mes == "xxxx":
            mesgen7 = random.randint(1, 12)
            if len(str(mesgen7)) == 1:
                mesgen7 = str("0") + str(mesgen7)
        elif mes == "rnd":
            mesgen7 = random.randint(1, 12)
            if len(str(mesgen7)) == 1:
                mesgen7 = str("0") + str(mesgen7)
        elif mes == "":
            mesgen7 = random.randint(1, 12)
            if len(str(mesgen7)) == 1:
                mesgen7 = str("0") + str(mesgen7)
        else:
            mesgen7 = mes
            if len(str(mesgen7)) == 1:
                mesgen7 = str("0") + str(mesgen7)

        if ano == 'xxxx':
            ccano7 = random.randint(2023, 2032)
        elif ano == 'xxx':
            ccano7 = random.randint(2023, 2032)
        elif ano == 'xx':
            ccano7 = random.randint(2023, 2032)
        elif ano == '20xx':
            ccano7 = random.randint(2023, 2032)
        elif ano == '202x':
            ccano7 = random.randint(2023, 2032)
        elif ano == "rnd":
            ccano7 = random.randint(2023, 2032)

        else:
            ccano7 = ano
            if len(str(ccano7)) == 2:
                ccano7 = str("20") + str(ccano7)

        if cvv == 'xxx' or "" or "rnd":
            if cc[0] == "3":
                cvvgen7 = random.randint(1000, 9999)
            else:
                cvvgen7 = random.randint(100, 999)
        else:
            cvvgen7 = cvv

        veri7 = verify(ccgen7)
        if veri7 == False:
            result7 = "False"
        if veri7 == True:
            result7 = "True"
            return ccgen7, mesgen7, ccano7, cvvgen7

def gen8(cc, mes, ano, cvv):    
    
    global ccgen8
    global mesgen8
    global ccano8
    global cvvgen8
    
    result8 = ""
    while result8 != "True":
        numeros = "1234567890"
        lista = list(numeros)
        random.shuffle(lista)
        resultados = ''.join(lista)
        resultados = cc + resultados
        if cc[0] == '3':
            ccgen8 = resultados[0:15]
        else:
            ccgen8 = resultados[0:16]

        if mes == "x":
            mesgen8 = random.randint(1, 12)
            if len(str(mesgen8)) == 1:
                mesgen8 = str("0") + str(mesgen8)
        elif mes == "xx":
            mesgen8 = random.randint(1, 12)
            if len(str(mesgen8)) == 1:
                mesgen8 = str("0") + str(mesgen8)
        elif mes == "xxx":
            mesgen8 = random.randint(1, 12)
            if len(str(mesgen8)) == 1:
                mesgen8 = str("0") + str(mesgen8)
        elif mes == "xxxx":
            mesgen8 = random.randint(1, 12)
            if len(str(mesgen8)) == 1:
                mesgen8 = str("0") + str(mesgen8)
        elif mes == "rnd":
            mesgen8 = random.randint(1, 12)
            if len(str(mesgen8)) == 1:
                mesgen8 = str("0") + str(mesgen8)
        elif mes == "":
            mesgen8 = random.randint(1, 12)
            if len(str(mesgen8)) == 1:
                mesgen8 = str("0") + str(mesgen8)
        else:
            mesgen8 = mes
            if len(str(mesgen8)) == 1:
                mesgen8 = str("0") + str(mesgen8)

        if ano == 'xxxx':
            ccano8 = random.randint(2023, 2032)
        elif ano == 'xxx':
            ccano8 = random.randint(2023, 2032)
        elif ano == 'xx':
            ccano8 = random.randint(2023, 2032)
        elif ano == '20xx':
            ccano8 = random.randint(2023, 2032)
        elif ano == '202x':
            ccano8 = random.randint(2023, 2032)
        elif ano == "rnd":
            ccano8 = random.randint(2023, 2032)

        else:
            ccano8 = ano
            if len(str(ccano8)) == 2:
                ccano8 = str("20") + str(ccano8)

        if cvv == 'xxx' or "" or "rnd":
            if cc[0] == "3":
                cvvgen8 = random.randint(1000, 9999)
            else:
                cvvgen8 = random.randint(100, 999)
        else:
            cvvgen8 = cvv

        veri8 = verify(ccgen8)
        if veri8 == False:
            result8 = "False"
        if veri8 == True:
            result8 = "True"
            return ccgen8, mesgen8, ccano8, cvvgen8

def gen9(cc, mes, ano, cvv):    
    
    global ccgen9
    global mesgen9
    global ccano9
    global cvvgen9
    
    result9 = ""
    while result9 != "True":
        numeros = "1234567890"
        lista = list(numeros)
        random.shuffle(lista)
        resultados = ''.join(lista)
        resultados = cc + resultados
        if cc[0] == '3':
            ccgen9 = resultados[0:15]
        else:
            ccgen9 = resultados[0:16]

        if mes == "x":
            mesgen9 = random.randint(1, 12)
            if len(str(mesgen9)) == 1:
                mesgen9 = str("0") + str(mesgen9)
        elif mes == "xx":
            mesgen9 = random.randint(1, 12)
            if len(str(mesgen9)) == 1:
                mesgen9 = str("0") + str(mesgen9)
        elif mes == "xxx":
            mesgen9 = random.randint(1, 12)
            if len(str(mesgen9)) == 1:
                mesgen9 = str("0") + str(mesgen9)
        elif mes == "xxxx":
            mesgen9 = random.randint(1, 12)
            if len(str(mesgen9)) == 1:
                mesgen9 = str("0") + str(mesgen9)
        elif mes == "rnd":
            mesgen9 = random.randint(1, 12)
            if len(str(mesgen9)) == 1:
                mesgen9 = str("0") + str(mesgen9)
        elif mes == "":
            mesgen9 = random.randint(1, 12)
            if len(str(mesgen9)) == 1:
                mesgen9 = str("0") + str(mesgen9)
        else:
            mesgen9 = mes
            if len(str(mesgen9)) == 1:
                mesgen9 = str("0") + str(mesgen9)

        if ano == 'xxxx':
            ccano9 = random.randint(2023, 2032)
        elif ano == 'xxx':
            ccano9 = random.randint(2023, 2032)
        elif ano == 'xx':
            ccano9 = random.randint(2023, 2032)
        elif ano == '20xx':
            ccano9 = random.randint(2023, 2032)
        elif ano == '202x':
            ccano9 = random.randint(2023, 2032)
        elif ano == "rnd":
            ccano9 = random.randint(2023, 2032)

        else:
            ccano9 = ano
            if len(str(ccano9)) == 2:
                ccano9 = str("20") + str(ccano9)

        if cvv == 'xxx' or "" or "rnd":
            if cc[0] == "3":
                cvvgen9 = random.randint(1000, 9999)
            else:
                cvvgen9 = random.randint(100, 999)
        else:
            cvvgen9 = cvv

        veri9 = verify(ccgen9)
        if veri9 == False:
            result9 = "False"
        if veri9 == True:
            result9 = "True"
            return ccgen9, mesgen9, ccano9, cvvgen9
#--------------------FIN DEFS-------------------#





@Client.on_message(filters.command(["gen"], prefixes=["/", "."]))
async def gen(_, m: Message):
    id = m.from_user.id
    username = m.from_user.username
    user = usuario(username, id)
    datos = user.buscar()
    if not datos or datos == False: return await m.reply('<b>Usuario no registrado porfavor registrse con /start</b>')
    ccx = m.text[len('/gen '):]
    if not ccx:
        return await m.reply("<b>Ingrese correctamente los datos</b>")



    ccx = ccx.replace("/", "|")
    entra = ccx.split("|")
    ccsX = entra[0].replace("x", "")
    cc = ccsX
    mes = "xx"
    ano = "xxxx"
    cvv = "xxx"


    if len(str(ccsX))<6 or len(str(ccsX))>16:
        return await m.reply("<b>Ingrese un bin valido</b>")
    time1 = time.perf_counter()
    edit1 = await m.reply(f"""
<b>Generando ccs..</b>
""")
    if len(entra) == 2:
        cc = ccsX
        mes = entra[1]
        ano = "xxxx"
        cvv = "xxx"

    if len(entra) == 3:
        cc = ccsX
        mes = entra[1]
        ano = entra[2]
        cvv = "xxx"
    if len(entra) == 4:
        cc = ccsX
        mes = entra[1]
        ano = entra[2]
        cvv = entra[3]

    cantidad = "10"

    ccs = []
    ccs1 = []
    ccs2 = []
    ccs3 = []
    ccs4 = []
    ccs5 = []
    ccs6 = []
    ccs7 = []
    ccs8 = []
    ccs9 = []

    if ano == "x":
        return await edit1.edit("<b>Año invalido</b>")
    if mes == "x":
        return await edit1.edit("<b>Mes invalido</b>")



    gen0(cc, mes, ano, cvv)
    gen1(cc, mes, ano, cvv)
    gen2(cc, mes, ano, cvv)
    gen3(cc, mes, ano, cvv)
    gen4(cc, mes, ano, cvv)
    gen5(cc, mes, ano, cvv)
    gen6(cc, mes, ano, cvv)
    gen7(cc, mes, ano, cvv)
    gen8(cc, mes, ano, cvv)
    gen9(cc, mes, ano, cvv)




    cclist = str(ccgen) + "|" + str(mesgen) + "|" + str(ccano) + "|" + str(cvvgen)
    cclist1 = str(ccgen1) + "|" + str(mesgen1) + "|" + str(ccano1) + "|" + str(cvvgen1)
    cclist2 = str(ccgen2) + "|" + str(mesgen2) + "|" + str(ccano2) + "|" + str(cvvgen2)
    cclist3 = str(ccgen3) + "|" + str(mesgen3) + "|" + str(ccano3) + "|" + str(cvvgen3)
    cclist4 = str(ccgen4) + "|" + str(mesgen4) + "|" + str(ccano4) + "|" + str(cvvgen4)
    cclist5 = str(ccgen5) + "|" + str(mesgen5) + "|" + str(ccano5) + "|" + str(cvvgen5)
    cclist6 = str(ccgen6) + "|" + str(mesgen6) + "|" + str(ccano6) + "|" + str(cvvgen6)
    cclist7 = str(ccgen7) + "|" + str(mesgen7) + "|" + str(ccano7) + "|" + str(cvvgen7)
    cclist8 = str(ccgen8) + "|" + str(mesgen8) + "|" + str(ccano8) + "|" + str(cvvgen8)
    cclist9 = str(ccgen9) + "|" + str(mesgen9) + "|" + str(ccano9) + "|" + str(cvvgen9)

    ccs.append(cclist)
    ccs1.append(cclist1)
    ccs2.append(cclist2)
    ccs3.append(cclist3)
    ccs4.append(cclist4)
    ccs5.append(cclist5)
    ccs6.append(cclist6)
    ccs7.append(cclist7)
    ccs8.append(cclist8)
    ccs9.append(cclist9)


    cards = ''.join(ccs)
    cards1 = "".join(ccs1)
    cards2 = "".join(ccs2)
    cards3 = ''.join(ccs3)
    cards4 = ''.join(ccs4)
    cards5 = ''.join(ccs5)
    cards6 = ''.join(ccs6)
    cards7 = ''.join(ccs7)
    cards8 = ''.join(ccs8)
    cards9 = ''.join(ccs9)


    ccs.clear()

    #------------.Bin del gen-----------------------------#
    BIN = ccsX
    gateBIN = requests.get(f"https://binlookup-1.andrexxone.repl.co/index.php?bin={BIN}").json()
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
    if len(str(mes)) ==1:
        mes = "0" + str(mes)


    time2 = time.perf_counter()
    texto = f"""<b>
Aqui estan sus ccs generadas:
💳Bin: <code>{bin}</code>
detalles: {emojiCountry} - <code>{bank}</code> - <code>{brand}</code> - <code>{type}</code> - <code>{level}</code>

Formato: <code>{entra[0]}|{mes}|{ano}|{cvv}</code>
-----------------------------------------------
<code>{cards}</code>
<code>{cards1}</code>
<code>{cards2}</code>
<code>{cards3}</code>
<code>{cards4}</code>
<code>{cards5}</code>
<code>{cards6}</code>
<code>{cards7}</code>
<code>{cards8}</code>
<code>{cards9}</code>
-----------------------------------------------
cantidad: {cantidad}
Tiempo: {time2 - time1 :0.2} segundos
Bot de: @Draxxd30
</b>"""
    nuevo = [[InlineKeyboardButton("Generar", callback_data="gen")]]
    reply_markup = InlineKeyboardMarkup(nuevo)
    await edit1.edit(texto, reply_markup=reply_markup)