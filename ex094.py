# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando 
# os dados de cada pessoa em um dicionário e todos os dicionários em uma 
# lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média 
# de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade 
# acima da média.
pessoas = []
dados = {}
soma = 0
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: '))
    while True:
        dados['Sexo'] = str(input('Sexo [M/F]: ')).upper() [0]
        if dados['Sexo'] in 'MmFf':
            break
        else:
            print('Erro! O valor inserido é inválido.')
    while True:
        dados['Idade'] = int(input('Idade: '))
        if 120 > dados['Idade'] > -1:
            soma += dados['Idade']
            break
        else:
            print('Erro! O valor inserido é inválido.')
    pessoas.append(dados.copy())
    while True:
        c = str(input('Deseja continuar [S/N]? ')).upper() [0]
        if c in 'SsNn':
            break
        else:
            print('O valor inserido é inválido.')
    if c in 'Ss':
        pass
    else:
        break
print('= ' * 25)
print(f'Total de Pessoas Cadastradas: {len(pessoas)}')
print(f'Média de Idade: {(soma / len(pessoas)):0.2f}')
print('Lista de Mulheres Cadastradas:', end=' ')
for p in pessoas:
    if p["Sexo"] == 'F':
        print(f'{p["Nome"]}', end=' ')
print('\nLista de Pessoas com Idade Acima da Média:', end=' ')
for p in pessoas:
    if p["Idade"] > (soma / len(pessoas)):
        print(f'{p["Nome"]}', end=' ')