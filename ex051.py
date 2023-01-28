# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.
pt = int(input('Digite o primeiro termo:'))
r = int(input('Razão:'))
if pt == 0:
    for pa in range(pt, 10 * r, r):
        print(pa, end=' > ')
    print('ACABOU')
else:
    for pa in range(pt, 10 * r + 1, r):
        print(pa, end=' > ')
    print('ACABOU')
