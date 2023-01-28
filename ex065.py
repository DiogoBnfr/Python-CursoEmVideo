# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior 
# e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = 0
count = 0
confirmation = 's'
maior = 0
menor = 0
soma = 0

while confirmation == 's':
    n = int(input('Insira um número: '))
    confirmation = str(input('Deseja continuar [S/N]? ')).lower
    soma += n
    if n != 0:
        count += 1
    if count == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
media = soma / count 
print(f'Maior número: {maior}\nMenor número: {menor}\nMédia: {media}')
