# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador 
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
print('Vou pensar em um número de 1 à 10, tente adivinhar!')
user_choice = int(input('Escolha um número de 1 à 10:'))
pc_choice = randint(1, 10)
count = 0
while user_choice != pc_choice:
    print('Você errou! Tente novamente.')
    if user_choice + 1 == pc_choice or user_choice - 1 == pc_choice:
        print('Você chegou muito perto desta vez!')
    count += 1
    user_choice = int(input('Escolha um número de 1 à 10:'))
print(f'Parabés! Você acertou.\nNúmero de tentativas: {count}')

'''
While Alternativo

acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    if jogador == computador:
        acertou = True
print('Acertou!')

'''
