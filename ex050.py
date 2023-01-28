# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
s = 0
for n in range(0, 6):
    i = int(input('Digite um número inteiro:'))
    if i % 2 == 0:
        s += i
print('A soma dos números pares acima é igual a:', s)
