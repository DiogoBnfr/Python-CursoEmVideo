# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numbers = int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: '))
print('Os números digitados foram: ', end='')
for n in numbers:
    print(f'{n} ', end='')
print(f'\nO número 9 apareceu {numbers.count(9)} vezes entre os números digitados')
if 3 in numbers:
    print(f'O número 3 apareceu pela primeira vez na {numbers.index(3)}a posição')
else:
    print('O número 3 não foi digitado')
print(f'Os números pares digitados foram: ', end='')
for n in numbers:
    if n % 2 == 0:
        print(n, end=' ')