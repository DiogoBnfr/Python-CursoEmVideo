# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
from time import sleep
ipay = float(input('Qual o seu salário? R$'))
print('CALCULANDO SEU AUMENTO...'), sleep(1)
if ipay <= 1250:
    fpay = ipay + (ipay / 100 * 15)
    print('Seu novo salário será de: R${:.0f}'.format(fpay))
else:
    fpay = ipay + (ipay / 100 * 10)
    print('Seu nove salário será de: R${:.0f}'.format(fpay))
