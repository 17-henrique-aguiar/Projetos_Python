import random
import string

def gerar_senha(tamanho=5):
    "Gera uma senha aleatótia com números"
    numeros = string.digits
    senha = ''.join(random.choice(numeros) for i in range(tamanho))
    return senha

print(gerar_senha(5))