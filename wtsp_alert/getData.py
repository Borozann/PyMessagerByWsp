numero = None
KEY_API = None

def init():
    global numero, KEY_API
    numero = input("Numero: ")
    KEY_API = input("Chave API: ")

def getNumero():
    return numero

def getChave():
    return KEY_API

init()