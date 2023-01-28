# Crie uma variável que diga o antecessor e o sucessor de um número.
num = int(input('Digite um número:'))
ant = int(num) - 1
suc = int(num) + 1
print('O antecessor de {} é {}, e o seu sucessor é {}.'.format(num, ant, suc))
