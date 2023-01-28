# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

import math
ang = float(input('Digite o ângulo que você deseja:'))
print(' Seno: {:.2f}\n Cosseno: {:.2f}\n Tangente: {:.2f}'
      .format(math.sin(math.radians(ang)),
              math.cos(math.radians(ang)),
              math.tan(math.radians(ang))))
# "math.radians" para conversão em radianos.
