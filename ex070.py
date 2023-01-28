# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
from termcolor import cprint
cprint(' NOME DO ESTABELECIMENTO '.center(37, ':'), 'blue')
total = hvp = lcp_nome = 0
lcp_valor = -1

while True:
    nome_produto = str(input('\nNome do Produto: ')).strip().capitalize()

    while True:
        valor_produto = float(input('Valor do Produto: R$'))
        if valor_produto < 0:
            cprint('Erro! O valor inserido é inválido para a operação atual.', 'red')
        else:
            break

    while True:
        confirmacao = str(input('Deseja continuar [S/N]: ')).strip().capitalize() [0] # Lendo somente a primeira letra digitada.
        if confirmacao not in 'SsNn':
            cprint('Erro! O valor inserido é inválido para a operação atual.', 'red')
        else:
            break
    
    total += valor_produto
    
    if valor_produto > 1000:
        hvp += 1

    if lcp_valor < 0:
        lcp_valor = valor_produto
        lcp_nome = nome_produto
    else:
        if lcp_valor > valor_produto:
            lcp_valor = valor_produto
            lcp_nome = nome_produto

    if confirmacao in 'Ss':
        pass
    if confirmacao in 'Nn':
        break

cprint(' FIM DO PROGRAMA '.center(50, ':'), 'blue')
print(f'''\nValor total: {total}
Produtos acima de R$1000: {hvp}
Produto mais barato foi {lcp_nome} custando R${lcp_valor}''')