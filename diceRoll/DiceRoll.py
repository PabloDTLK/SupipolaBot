import random
import re

patron = re.compile(r"\d{0,2}[dD]\d{1,3}")

def diceRoll(roll):
    #Sacamos todos las posibles tiradas
    listaTiradas = patron.findall(roll)
    #Verificamos que ha entrado una expresión correcta
    if len(listaTiradas) == 0:
        return "Ha habido un error"
    else:
        #Mensaje a devolver
        mensaje = ""
        for tirada in listaTiradas:
            #Desglosamos en variables la tirada
            [nDados, caras] = tirada.lower().split("d")
            #Si no se introduce numero de dados, será 1
            nDados = (nDados,"1")[nDados == '']
            #Indice del mensaje
            mensaje += f" - d{caras}:\n"
            #Por cada dado a tirar
            for n in range( int(nDados) ):
                #Realizamos la tirada
                resultado = random.randint(1, int(caras))
                #Lo guardamos numerado en el mensaje
                mensaje += f"  - {resultado}\n"
        #Devolvemos el mensaje
        return mensaje