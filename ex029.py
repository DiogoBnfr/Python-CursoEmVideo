# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vcar = int(input('Qual era a velocidade em que o carro trafegava?'))
vmax = 80
cost = float((vcar - vmax) * 7.00)
if vcar <= vmax:
    print('Tudo certo. O carro trafegava dentro dos limites de velocidade.')
else:
    print('O carro trafegava acima do limite e devera ser multado em R${:.2f}.'.format(cost))
