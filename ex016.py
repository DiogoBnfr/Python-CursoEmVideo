# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# Primeira forma:
import math
num = float(input('Digite um número:'))
res = math.trunc(num)
print('A parte inteira de {} é {}'.format(num, res))

# Segunda forma:
num = float(input('Digite um número:'))
print('A parte inteira de {} é {}'.format(num, math.trunc(num)))

# Terceira forma:
num = float(input('Digite um número:'))
print('A parte inteira de {} é {}'.format(num, int(num)))
