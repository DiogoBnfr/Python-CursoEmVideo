# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, 
# tudo isso será guardado em um dicionário, incluindo o total de gols 
# feitos durante o campeonato.
data = {}
gols = []
data['Jogador'] = str(input('Insira o nome do jogador: '))
data['Partidas Jogadas'] = int(input('Quantas partidas jogou: '))
for p in range(0, data['Partidas Jogadas']):
    gols.append(int(input(f'Gols marcados na {p + 1}a partida: ')))
data['Gols Marcados'] = gols
data['Total'] = sum(gols)
print('= ' * 41)
print(data)
print('= ' * 41)
for k, v in data.items():
    print(f'{k}: {v}')
print('= ' * 41)
print(f'O jogador {data["Jogador"]} jogou {data["Partidas Jogadas"]} partidas.')
for p, g in enumerate(gols):
    if g == 1:
        print(f'{p + 1}a partida: {g} gol.')
    else:
        print(f'{p + 1}a partida: {g} gols.')
print(f'Total: {data["Total"]}')
print('= ' * 41)