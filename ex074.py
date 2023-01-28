# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

a = randint(1, 10)
maior_num = a
menor_num = a

b = randint(1, 10)
if b > maior_num:
    maior_num = b
if b < menor_num:
    menor_num = b

c = randint(1, 10)
if c > maior_num:
    maior_num = c
if c < menor_num:
    menor_num = c

d = randint(1, 10)
if d > maior_num:
    maior_num = d
if d < menor_num:
    menor_num = d

e = randint(1, 10)
if e > maior_num:
    maior_num = e
if e < menor_num:
    menor_num = e

tupla = a, b, c, d, e

print(f'Os números gerados foram: {tupla}')
print(f'Sendo o maior número {maior_num}, e o menor número {menor_num}.')
