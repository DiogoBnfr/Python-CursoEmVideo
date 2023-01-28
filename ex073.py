# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

from termcolor import cprint

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo', 
'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'\nLista de times do Brasileirão: \n{times}\n')
cprint(188 * ':', 'blue')
print(f'\n5 primeiros colocados: \n{times[0:5]}\n')
cprint(188 * ':', 'blue')
print(f'\n4 últimos colocados: \n{times[-4:]}\n')
cprint(188 * ':', 'blue')
print(f'\nTimes em ordem alfabética: \n{sorted(times)}\n')
cprint(188 * ':', 'blue')
print(f'\nPosição do time Chapecoense: {times.index("Chapecoense") + 1}a Posição\n')
