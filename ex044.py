# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('{:^32}'.format('VIA BUNKER'))  # ^ é usado para formatação centralizada (o que vier antes preenche os espaços)
v = float(input('Insira o valor total das compras:'))

# forma alternativa: print('[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista no cartão de crédito\n'
# '[ 3 ] 2x no cartão de crédito\n[ 4 ] 3x ou mais no cartão de crédito')

print('''[ 1 ] à vista dinheiro/cheque: 10% de desconto
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão: preço formal
[ 4 ] 3x ou mais no cartão: 20% de juros''')
opt = int(input('Insira a forma de pagamento:'))
if opt == 1:
    vfinal = v - (v / 100 * 10)
    des = v - vfinal
    print('Valor final: R${:.2f}\nDesconto: R${:.2f}'.format(vfinal, des))
elif opt == 2:
    vfinal = v - (v / 100 * 5)
    des = v - vfinal
    print('Valor final: R${:.2f}\nDesconto: R${:.2f}'.format(vfinal, des))
elif opt == 3:
    vfinal = v
    des = v - vfinal
    par = v / 2
    print('Valor final: {:.2f}\nValor da Parcela: R${:.2f}\nDesconto: R${:.2f}\n'.format(vfinal, par, des))
elif opt == 4:
    vfinal = v + (v / 100 * 20)
    des = v - vfinal
    acr = des - 2 * des
    par = int(input('Digite o número de parcelas desejadas:'))
    par = vfinal / par
    print('Valor final: R${:.2f}\nValor da Parcela: R${:.2f}\nAcréscimo: R${:.2f}'.format(vfinal, par, acr))
else:
    print('Erro: insira uma forma de pagamento válida!')
