# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

num = soma = cont = 0
while num != 999:
    num = int(input('Insira um valor [999 para Encerrar]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Você digitou {cont} números.\nA soma total é {soma}.')
