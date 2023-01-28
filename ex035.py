# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.
from time import sleep
a = float(input('Digite o primero valor:'))
b = float(input('Digite o segundo valor:'))
c = float(input('Digite o terceiro valor:'))
print('Analisando...'), sleep(1)
if a + b > c and a + c > b and b + c > a:
    print('Os valores {:.2f}, {:.2f} e {:.2f} podem formar um triângulo!'.format(a, b, c))
else:
    print('Os valores {:.2f}, {:.2f} e {:.2f} não podem formar um triâgulo!'.format(a, b, c))
