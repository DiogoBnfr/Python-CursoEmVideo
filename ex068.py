# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas 
# que ele conquistou no final do jogo.
from random import randint
from termcolor import cprint

user_name = str(input('Digite seu nome: ')).capitalize().strip()
victory_streak = 0

while True:
    while True:
        user_num = int(input('Escolha um número de 1 à 10: '))
        if user_num not in[1, 2, 3, 4, 5, 6 ,7 ,8 , 9, 10]:
            cprint('Erro! O valor inserido é inválido para a operação atual.', 'red')
        else:
            break
    while True:
        user_choice = str(input('Par ou Ímpar [P/I]: ')).upper().strip()
        if user_choice not in 'PI':
            cprint('Erro! O valor inserido é inválido para a operação atual.', 'red')
        else:
            break

    bot_num = randint(1, 10)
    if user_choice == 'P':
        bot_choice = 'N'
    if user_choice == 'N':
        bot_choice = 'P'

    result = (user_num + bot_num) % 2
    if result == 0 and user_choice == 'P':
        victory_streak += 1
        cprint('Vitória!', 'green')
        print(f'{user_name} você está numa sequência de {victory_streak} vitórias!\n')
    elif result != 0 and user_choice == 'I':
        victory_streak += 1
        cprint('Vitória!', 'green')
        print(f'{user_name} você está numa sequência de {victory_streak} vitórias!\n')
    else:
        if victory_streak > 0:
            cprint('Derrota!', 'red')
            print('Sua sequência de vitórias foi encerrada.')
            break
        else:
            cprint('Derrota!', 'red')
            break
