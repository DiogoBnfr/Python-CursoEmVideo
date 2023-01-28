# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
# cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente 
# de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se 
# aposentar.
from datetime import date
data = {}
data['Nome'] = str(input('Digite seu nome completo: '))
data['Data de Nascimento'] = int(input('Digite seu ano de nascimento: '))
data['Carteira de Trabalho'] = int(input('Digite o número de sua carteira de trabalho [0 = não possui]: '))
if data['Carteira de Trabalho'] != 0:
    data['Ano de Contratação'] = int(input('Digite seu ano de contratação: '))
    data['Salário'] = float(input('Digite o valor do seu salário: '))
    data['Idade de Aposentadoria'] = (date.today().year - data['Data de Nascimento']) + (35 - (date.today().year - data['Ano de Contratação']))
print('= ' * 32)
for k, v in data.items():
    print(f'{k:<22}: {v:<10}')