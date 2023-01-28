# Faça um programa que leia um número qualquer e mostre o seu fatorial.
n = int(input('Insira o número que deseja fatorar: '))
c = n
f = 1
print(f'{n}! = ', end ='')
while c > 0:
    if c > 1:
        print(f'{c} x ', end ='')
    else:
        print(f'{c} = ', end ='')
    f *= c
    c -= 1
print(f'{f}')
