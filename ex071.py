#  Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#  Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
from termcolor import cprint

cprint(' BANCO CEV '.center(37, ':'), 'blue')
valor_saque = int(input('Quanto deseja sacar? R$' ))

notas_50 = notas_20 = notas_10 = notas_1 = 0

if valor_saque >= 50:
    notas_50 = valor_saque // 50
    valor_saque -= notas_50 * 50

if valor_saque >= 20:
    notas_20 = valor_saque // 20
    valor_saque -= notas_20 * 20

if valor_saque >= 10:
    notas_10 = valor_saque // 10
    valor_saque -= notas_10 * 10

if valor_saque >= 1:
    notas_1 = valor_saque // 1
    valor_saque -= notas_1 * 1

if notas_50 != 0:
    print(f'Total de {notas_50} cédulas de R$50')
if notas_20 != 0:
    print(f'Total de {notas_20} cédulas de R$20')
if notas_10 != 0:
    print(f'Total de {notas_10} cédulas de R$10')
if notas_1 != 0:
    print(f'Total de {notas_1} cédulas de R$1')

cprint(''.center(37, ':'), 'blue')
print('\nVolte sempre ao Banco CEV! Tenha um bom dia!\n')