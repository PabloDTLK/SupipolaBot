import discord

from puentes.basic_funciones import *

#Leemos el token
with open("./recursos/token.txt", "r", encoding="utf-8") as fichero:
    token = fichero.read()

#Definimos los intents que son como los permisos
intents = discord.Intents.default()
intents.message_content = True

#Definimos el cliente
client = discord.Client(intents=intents)

#Controlamos los eventos

#Cuando se inicia
@client.event
async def on_ready():
    print(f"Me he logueado como {client.user}")
    
#Detectamos contenido de los mensajes
@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
        
    if msg.content.lower() == "soy frances":
        await insultoFrances(msg)
    
    if msg.content[0] == "/":
        await comandos(msg)

#Lanzamos la aplicación
client.run(token)