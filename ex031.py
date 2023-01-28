# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
kmi = int(input("Quantos km's deseja viajar?"))
kmm = 200
if kmi <= kmm:
    custo = kmi * 0.50
    print('O valor da sua viagem será de R${}'.format(custo))
else:
    custo = kmi * 0.45
    print('O valor da sua viagem será de R${}'.format(custo))
