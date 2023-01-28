# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

# Primeira forma:
import math
op = float(input('Comprimento do cateto oposto:'))
ad = float(input('Comprimento do cateto adjacente:'))
hip = ((op * op) + (ad * ad))
print('A hipotenusa vai medir {:.2f}'.format(math.sqrt(hip)))

# Segunda forma:
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# Terceira forma:
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
print('A hipotenuna será {:.2f}'.format(math.hypot(co, ca)))
