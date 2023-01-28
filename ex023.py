# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Primeira forma:
num = int(input('Digite um número entre 0 e 9999:'))
print('Analisando o número...')
n = str(num)
print('Analisando o número {}'.format(num))
print(' Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}'.format(n[3], n[2], n[1], n[0]))

# Obs.: Apresenta falha quando os 4 slots não são preenchidos.

# Segunda forma:
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(' Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}'.format(u, d, c, m))
