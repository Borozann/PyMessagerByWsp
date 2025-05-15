import getData as data
import requests

def enviar_whatsapp(mensagem):
    numero = data.getNumero
    API_KEY = data.getChave
    url = f'https://api.callmebot.com/whatsapp.php?phone={numero}&text={mensagem}&apikey={API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        print("Mensagem enviada com sucesso.")
    else:
        print(f"Erro: {response.status_code}")

if __name__ == "__main__":
    enviar_whatsapp("Mensagem teste via PyMessagerWsp.")
