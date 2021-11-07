import random

# Gera a Chave de Autenticacao dos Certificados
def create_authentication_key():
      return str(random.randint(10000000000000000000, 99999999999999999999))