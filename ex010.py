# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = float(real) * 0.21
euro = float(real) * 0.19
print('Os seus R${:.2f} equiavalem a:\nUSD${:.2f}\nEUR${:.2f}'.format(real, dolar, euro))
