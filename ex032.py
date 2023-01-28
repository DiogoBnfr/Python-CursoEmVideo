# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from time import sleep
from datetime import date
year = int(input('Que ano deseja analisar? (Digite 0 para analisar o ano atual):'))
print('ANALISANDO...'), sleep(1)
if year == 0:
    year = date.today().year
analysis1 = year % 4
analysis2 = year % 100
analysis3 = year % 400
if analysis1 == 0 and analysis2 != 0 or analysis1 == 0 and analysis2 == 0 and analysis3 == 0:
    print('{} é um ano bissexto.'.format(year))
else:
    print('{} não é um ano bissexto.'.format(year))
