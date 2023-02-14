import re

def validate_email(email):
  # Expressão regular para verificar o formato de um endereço de email
  pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

  # Verifica se o endereço de email corresponde ao padrão
  return True if pattern.match(email) else False