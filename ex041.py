# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
from datetime import date
ano_nasc = int(input('Digite seu ano de nascimento:'))
ano_at = date.today().year
idade = ano_at - ano_nasc
print(idade)
if idade <= 9:
    print('Você é considerado um atleta mirim')
elif idade <= 14:
    print('Você é considerado um atleta infantil')
elif idade <= 19:
    print('Você é considerado um atleta júnior')
elif idade <= 25:
    print('Você é considerado um atleta sênior')
else:
    print('Você é considerado um atleta master')
