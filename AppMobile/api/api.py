import requests
import base64
from dotenv import load_env


usuario = load_env("USUARIO")
senha = load_env("SENHA")
url = load_env("URL")

auth = base64.b64encode(b"{}:{}".format(usuario, senha)).decode("utf-8")
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
