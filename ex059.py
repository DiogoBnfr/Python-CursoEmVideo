# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

print('Insira os valores a serem utilizados.')
num_1 = float(input('Primeiro número: '))
num_2 = float(input('Segundo número: '))
opt = 0
while opt != 5:
    print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair
''')
    opt = int(input('O que deseja fazer?'))
    if opt == 1:
        soma = num_1 + num_2
        print(f'A soma entre {num_1} e {num_2} é igual à {soma}.')
    elif opt == 2:
        multiplicação = num_1 * num_2
        print(f'O produto de {num_1} vezes {num_2} é igual à {multiplicação}.')
    elif opt == 3:
        if num_1 > num_2:
            print(f'{num_1} é maior que {num_2}.')
        elif num_2 > num_1:
            print(f'{num_2} é maior que {num_1}.')
        else:
            print(f'{num_1} e {num_2} são iguais.')
    elif opt == 4:
        print('Insira os valores a serem utilizados.')
        num_1 = float(input('Primeiro número: '))
        num_2 = float(input('Segundo número: '))
    elif opt == 5:
        print('Finalizando...'),sleep(1)
        print('Processo encerrado!')
    else:
        print('Erro! Por favor, insira uma opção válida.')