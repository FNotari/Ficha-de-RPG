import requests

BASE_URL = "https://www.dnd5eapi.co/api"

def get(endpoint):
    #Realiza uma requisição GET para a API
    url = f"{BASE_URL}/{endpoint}"
    
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        return resposta.json()
    
    raise Exception(f"\nErro ao acessar a API\n"
        f"URL: {url}\n"
        f"Status: {resposta.status_code}")