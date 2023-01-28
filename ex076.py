# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, 
# organizando os dados em forma tabular.

products = ('RX6600M', 1370.50,
'RTX2060Ti', 2290,
'GTX1080Ti', 1560,
'RX550', 749.99,
'RTX4090', 5999.99)

print('-' * 40)
print(f'{"KaBuM!":^40}')
print('-' * 40)

for p in range(0, len(products)):
    if p % 2 == 0:
        print(f'{products[p]:.<30}', end='')
    else:
        print(f'R${products[p]:>8.2f}')

print('-' * 40)