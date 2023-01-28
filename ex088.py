# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

lista = []
index = 0
print()
print('- ' * 14)
print(f'{"MEGA-SENA":^30}')
print('- ' * 14)
print()
for jogos in range(0, int(input('Quantos jogos deseja gerar? '))):
    lista.append([])
for jogo in lista:
    for numero in range(0, 6):
        index = 0
        while index != 1:
            n = randint(1, 60)
            if n not in jogo:
                jogo.append(n)
                index += 1
            else:
                pass
print()
for jogo in lista:
    print(jogo)
print()
