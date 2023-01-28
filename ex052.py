# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número inteiro:'))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        t += 1
    else:
        print('\033[30m', end='')
    print('{}'.format(c), end=' ')
if n == 0:
    print('0 não é divisivel, por isso não é um número primo')
else:
    if t == 1:
        print('\n\033[m{} é divisivel por {} número'.format(n, t))
    else:
        print('\n\033[m{} é divisivel por {} números'.format(n, t))
    if t == 2:
        print('\33[32m{} é um número primo'.format(n))
    else:
        print('\033[31m{} não é um número primo'.format(n))
