# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
ipay = float(input('Digite o salário atual do funcionário:'))
perc = ipay / 100 * 15
fpay = ipay + perc
print('O salário com aumento será de R${}'.format(fpay))
