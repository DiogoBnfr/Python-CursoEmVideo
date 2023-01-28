# Crie um programa onde 4 jogadores joguem um dado e tenham resultados 
# aleatórios. Guarde esses resultados em um dicionário em Python. No final, 
# coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior 
# número no dado.
from random import randint
from time import sleep
data = {}
for n, c in enumerate(range(0, 4)):
    jogada = randint(1, 6)
    data[f'JOGADOR {n + 1}'] = jogada
for k in data:
    print(f'{k} tirou {data[k]} no dado'), sleep(1)
for n, k in enumerate(sorted(data, key=data.get, reverse=True)):
    print(f'{n + 1}o lugar: {k}, tirou {data[k]}'), sleep(1)
