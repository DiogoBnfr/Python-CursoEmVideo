# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

from termcolor import cprint

maior_idade = homens = mulheres_menor_idade = 0

while True:
    cprint(' CADASTRO '.center(37, ':'), 'blue')
    idade = int(input('Informe sua idade: '))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()
        if sexo not in 'MF':
            cprint('Erro! O valor inserido é inválido para a operação atual.', 'red')

    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres_menor_idade += 1

    while True:
        repetir = str(input('Deseja continuar [S/N]? ')).upper().strip()
        if repetir not in 'SN':
            cprint('Erro! O valor inserido é invalido para a operação atual.', 'red')
        else:
            break
    if repetir == 'S':
        print('')
    if repetir == 'N':
        break

cprint('\nDentre as pessoas cadastradas:', 'yellow')

if maior_idade == 0:
    print(f'Nenhuma das pessoas cadastradas tem mais de 18 anos.')
elif maior_idade == 1:
    print(f'{maior_idade} pessoa tem mais de 18 anos.')
elif maior_idade > 1:
    print(f'{maior_idade} pessoas tem mais de 18 anos.')

if homens == 0:
    print(f'Nenhum homem foi cadastrado.')
elif homens == 1:
    print(f'{homens} foi cadastrado.')
elif homens > 1:
    print(f'{homens} foram cadastrados.')

if mulheres_menor_idade == 0:
    print(f'Nenhuma mulher menor de 20 anos foi cadastrada.')
elif mulheres_menor_idade == 1:
    print(f'{mulheres_menor_idade} mulher menor de 20 anos foi cadastrada.')
elif mulheres_menor_idade > 1:
    print(f'{mulheres_menor_idade} mulheres menores de 20 anos foram cadastradas.')
