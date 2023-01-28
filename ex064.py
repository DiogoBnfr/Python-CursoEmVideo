#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = 0
soma = 0
count = 0

while n != 999:
    n = int(input('Digite um número [999 para encerrar]: '))
    if n != 999:
        soma += n
        count += 1
    else:
        pass
print(f'Soma dos números digitados: {soma}\nQuantidade de números digitados: {count}')
print('Processo finalizado...')
