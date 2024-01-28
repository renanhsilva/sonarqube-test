import random

def gerar_nome_gato():
    nomes = ["Mingau", "Bolinha", "Chico", "Luna", "Felix", "Bella", "Salem", "Nina", "Simba", "Mel"]
    return random.choice(nomes)

# Exemplo de uso
for _ in range(5):
    print(gerar_nome_gato())
