import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

usuario = os.getenv('USUARIO')
senha = os.getenv('SENHA')
url = os.getenv('URL')

auth_string = f"{usuario}:{senha}".encode()

auth = base64.b64encode(auth_string).decode("utf-8")
headers = { "Authorization": f"Basic {auth}" }

def api_delete(id):
    """
    Faz a requisicao para deletar o item com o id passado
    """
    response = requests.delete(f"{url}/{id}/", headers=headers)
    return response

    
def api_get():
    """
    Faz a requisição para pegar todas os registros    
    """
    response = requests.get(url, headers=headers)
    return response.json()

def api_post(body):
    """
    Faz a requisição para salvar um novo registro
    """
    try:
        response = requests.post(url, data=body, headers=headers)
        status = response.status_code
        response = response.json()
        response["status"] = status
    except ValueError as e:
        raise e
    return response

print(api_get())