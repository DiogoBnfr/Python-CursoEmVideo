# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
list = []
start = 0
for number in range(0, 5):
    list.append(int(input(f'Digite um número para a posição {number}: ')))
max = max(list)
min = min(list)

print(f'Os valores digitados foram: {list}')

print(f'O maior valor digitado foi {max} na(s) posição(ções):', end='')
for i, v in enumerate(list):
    if v == max:
        print(f' {i}', end='')

print(f'\nO menor valor digitado foi {min} na(s) posição(ções):', end='')
for i, v in enumerate(list):
    if v == min:
        print(f' {i}', end='')