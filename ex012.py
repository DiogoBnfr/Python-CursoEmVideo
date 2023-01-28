# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
cpro = float(input('Digite o custo do produto:'))
desc = (cpro / 100 * 5)
res = cpro - desc
print('O custo com desconto de 5% aplicado será de R${}'.format(res))
