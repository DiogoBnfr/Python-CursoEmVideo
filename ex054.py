# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.
from datetime import date
d = date.today().year
p = 0
tma = 0
tme = 0
for c in range(0, 7):
    p += 1
    i = int(input('Em que ano a {}a pessoa nasceu?'.format(p)))
    r = d - i
    if r >= 21:
        tma += 1
    else:
        tme += 1
if tma == 0:
    print('Nenhuma das pessoas acima é maior de idade!')
    print('Todos são menores de idade.')
elif tma == 1:
    print('Somente {} pessoa é maior de idade!'.format(tma))
    print('{} pessoas são menores de idade.'.format(tme))
else:
    print('{} pessoas são maiores de idade.'.format(tma))
    print('{} pessoas são menores de idade.'.format(tme))
