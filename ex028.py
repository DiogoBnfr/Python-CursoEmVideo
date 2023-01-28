# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu.
from random import randint
from time import sleep
print('Vou pensar em um número de 0 a 5. Tente adivinhar...'), sleep(1)
user = int(input('Escolha um número:'))
result = randint(0, 5)
print('PROCESSANDO...'), sleep(1)
if user == result:
    print('Você acertou!')
else:
    print('Você errou! Meu número era {}.'.format(result))
