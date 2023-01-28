# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
from time import sleep
from termcolor import cprint
cprint('CONVERSOR DE BASES NUMÉRICAS', 'green'), sleep(1)
num = int(input('Digite o número que deseja converter:'))
cprint(' 1 - Binário \n 2 - Octal \n 3 - Hexadecimal', 'blue')
typecon = int(input('Selecione a base de conversão desejada:'))
if typecon == 1:
    cprint('CONVERTENDO PARA BINÁRIO...', 'green'), sleep(1)
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num) [2:]))
elif typecon == 2:
    cprint('CONVERTENDO PARA OCTAL...', 'green'), sleep(1)
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num) [2:]))
elif typecon == 3:
    cprint('CONVERTENDO PARA HEXADECIMAL...', 'green'), sleep(1)
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num) [2:]))
else:
    print('Opção inválida! Tente novamente.')
