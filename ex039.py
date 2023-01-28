#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_nasc = int(input('Digite seu ano de nascimento:'))
ano_at = date.today().year
idade = ano_at - ano_nasc
periodo = idade - 18
print('Quem nasceu em {} tem {} em {}'.format(ano_nasc, idade, ano_at))
if periodo == 0:
    print('Você deve se alistar ainda esse ano.')
elif periodo > 0:
    previsao = ano_at - periodo
    print('Você já deveria ter se alistado há {} anos'.format(periodo))
    print('Seu alistamento foi em {}'.format(previsao))
elif periodo < 0:
    previsao = (periodo - 2 * periodo) + ano_at
    print('Você deve se alistar daqui {} anos.\nSeu alistamento será em {}.'.format(periodo - 2 * periodo, previsao))
