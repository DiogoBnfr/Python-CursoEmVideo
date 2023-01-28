# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.
import colorama
from colorama import Fore
from termcolor import cprint

colorama.init()
dadosTime = []
dadosJogador = {}
golsJogador = []

while True:
    # Cadastro de Jogadores
    dadosJogador.clear()
    golsJogador.clear()
    dadosJogador['NOME'] = str(input(Fore.BLUE + 'Nome do Jogador: ' + Fore.RESET))
    for partidasJogador in range(0, int(input(Fore.BLUE + 'Partidas Jogadas: ' + Fore.RESET))):
        golsJogador.append(int(input(Fore.BLUE + f'Gols marcados na {partidasJogador + 1}a partida: ' + Fore.RESET)))
    dadosJogador['GOLS'] = golsJogador[:]
    dadosJogador['MÉDIA'] = float((sum(golsJogador)) / len(golsJogador))
    dadosJogador['TOTAL'] = int(sum(golsJogador))
    if dadosJogador['MÉDIA'] >= 0.8:
        dadosJogador['DESEMPENHO'] = 'BOM'
    elif dadosJogador['MÉDIA'] >= 0.4:
        dadosJogador['DESEMPENHO'] = 'MEDIANO'
    else:
        dadosJogador['DESEMPENHO'] = 'RUIM'
    dadosTime.append(dadosJogador.copy())

    # Confirmação de validade de resposta.
    while True:
        inputUsuario = str(input(Fore.CYAN + 'Deseja continuar [S/N]? ' + Fore.RESET)).upper()[0]
        if inputUsuario not in 'SN':
            cprint('Erro! O valor inserido é inválido. Por favor, digite apenas S ou N.')
        else:
            break

    # Redirecionamento do usuário
    if inputUsuario == 'S':
        pass
    else:
        break

# Tabela de Desempenho dos Jogadores / Header
cprint('= ' * 85, 'blue')
print(f'{"TABELA DE DESEMPENHO DOS JOGADORES":^170}')
cprint('= ' * 85, 'blue')
cprint(f'{"N.":<5}', end='')
for key in dadosJogador.keys():
    cprint(f'{key:^33}', end='')
print()
cprint('- ' * 85, 'blue')

# Tabela de Desempenho dos Jogadores / Conteúdo
for numero, jogador in enumerate(dadosTime):
    print(f'{numero:<5}{str(jogador["NOME"]):^33}{str(jogador["GOLS"]):^33}{jogador["MÉDIA"]:^33.2f}{str(jogador["TOTAL"]):^33}', end='')
    if str(jogador["DESEMPENHO"]) == 'BOM':
        cprint(f'{str(jogador["DESEMPENHO"]):^33}', 'green')
    if str(jogador["DESEMPENHO"]) == 'MEDIANO':
        cprint(f'{str(jogador["DESEMPENHO"]):^33}', 'yellow')
    if str(jogador["DESEMPENHO"]) == 'RUIM':
        cprint(f'{str(jogador["DESEMPENHO"]):^33}', 'red')
cprint('- ' * 85, 'blue')

# Informações do Jogador / Menu
while True:

    # Confirmação de Validade da Resposta
    while True:
        inputUsuario = int(input(Fore.CYAN + 'Digite o Número do Jogador para Visualizar Informações Detalhadas [-1 para encerrar]: ' + Fore.RESET))
        if inputUsuario >= len(dadosTime) or -1 > inputUsuario:
            cprint('Erro! O número digitado não corresponde à nenhum dos jogadores cadastrados.', 'red')
        else:
            break

    # Redirecionamento de Usuário        
    if inputUsuario == -1:
        cprint(f'{"ENCERRANDO . . ."}', 'red')
        break

    # Informações do Jogador / Conteúdo
    cprint('= ' * 44, 'blue')
    cprint(f'Informações do Jogador: ', 'blue', end='')
    print(dadosTime[inputUsuario]["NOME"])
    for numero, gols in enumerate(dadosTime[inputUsuario]["GOLS"]):
        cprint(f'{numero + 1}a Partida: ', 'blue', end='')
        print(f'{gols} gols')
    cprint('MÉDIA: ', 'blue', end='')
    print(dadosTime[inputUsuario]["MÉDIA"], end=' ')
    cprint('TOTAL: ', 'blue', end='')
    print(dadosTime[inputUsuario]["TOTAL"], end=' ')
    cprint('DESEMPENHO: ', 'blue', end='')
    if str(dadosTime[inputUsuario]["DESEMPENHO"]) == 'BOM':
        cprint(f'{str(dadosTime[inputUsuario]["DESEMPENHO"])}', 'green')
    if str(dadosTime[inputUsuario]["DESEMPENHO"]) == 'MEDIANO':
        cprint(f'{str(dadosTime[inputUsuario]["DESEMPENHO"])}', 'yellow')
    if str(dadosTime[inputUsuario]["DESEMPENHO"]) == 'RUIM':
        cprint(f'{str(dadosTime[inputUsuario]["DESEMPENHO"])}', 'red')
    cprint('= ' * 44, 'blue')