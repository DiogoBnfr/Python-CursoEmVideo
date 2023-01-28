#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

from termcolor import cprint

print('{:^32}'.format(' JOKENPÔ '))
input('Pressione Enter para iniciar!')
print('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
user = int(input('Escolha uma das opções acima:'))
pc = randint(1, 3)
if user != 1 and user != 2 and user != 3:
    print('O valor inserido é inválido, tente novamente!')
else:
    print('JO', end=' '), sleep(1)
    print('KEN', end=' '), sleep(1)
    print('PÔ!')
    if user == 1:
        user = 'Pedra'
    elif user == 2:
        user = 'Papel'
    elif user == 3:
        user = 'Tesoura'
        pass
    if pc == 1:
        pc = 'Pedra'
    elif pc == 2:
        pc = 'Papel'
    elif pc == 3:
        pc = 'Tesoura'
        pass
    if user == 'Pedra' and pc == 'Tesoura' or user == 'Papel' and pc == 'Pedra' or user == 'Tesoura' and pc == 'Papel':
        print('''O computador escolheu {}
Você escolheu {}'''.format(pc, user))
        cprint('VITÓRIA!', 'green')
    elif user == 'Pedra' and pc == 'Papel' or user == 'Papel' and pc == 'Tesoura' or \
            user == 'Tesoura' and pc == 'Pedra':
        print('''O computador escolheu {}
Você escolheu {}'''.format(pc, user))
        cprint('DERROTA!', 'red')
    elif user == pc:
        print('''O computador escolheu {}
Você escolheu {}'''.format(pc, user))
        cprint('EMPATE!', 'yellow')
