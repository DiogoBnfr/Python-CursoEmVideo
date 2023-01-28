# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num_list = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    user_num = int(input('Insira um número de 0 à 20: '))
    if 0 <= user_num <= 20:
        break
    else:
        print('Erro! O valor inserido é inválido para a operação atual.')

print(f'Você digitou o número {num_list[user_num]}.')