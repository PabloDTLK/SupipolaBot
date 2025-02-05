import random
from diceRoll.DiceRoll import *


#Detecciones de mensajes
async def insultoFrances(msg):
    idInsultos = "1321126827821109288"
    canalInsultos = await msg.author.guild.fetch_channel(idInsultos)

    await canalInsultos.send(f"{msg.author.mention} es imbécil")

async def comandos(msg):
    command = msg.content[1:].lower()
    
    if command == "ayuda":
        await msg.reply(ayuda())
    
    elif command == "usuarios":
        await msg.reply(f"Somos actualmente {msg.guild.member_count} miembros")
        
    elif command == "hola":
        await msg.reply("Hola humano")
        
    elif command == "pensar":
        await msg.reply(f"Sí, a veces pienso")
        
    elif command == "fruta":
        await msg.reply(f"Te ha tocado {generaFruta()}")
        
    elif command[:8] == "diceroll":
        await msg.reply(diceRoll(command))


#Leer el fichero de ayuda
def ayuda():
    with open("./recursos/ayuda.txt", "r", encoding="utf-8") as fichero:
        ayuda = fichero.read()
    return ayuda

#Funcion fruta
def generaFruta():
    frutas = [
        "un limón 🍋",
        "una pera 🍐",
        "una manzana 🍎",
        "un caballo de guerra 🐴⚔️",
        "un kiwi 🥝",
        "una mierda 💩"
    ]
    
    return frutas[random.randint(0, len(frutas) - 1)]