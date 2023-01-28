# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo
# será negado.

VI = float(input('Informe o valor do imóvel: R$'))
SC = float(input('Informe o salário do comprador: R$'))
PA = float(input('Informe em quantos anos deseja quitar o pagamento:'))
PSC = (SC / 100) * 30
PM = VI / (PA * 12)
print('Para pagar um imóvel de {:.2f} em {} anos, sua prestação mensal será de R${:.2f}.'.format(VI, PA, PM), end=' ')
if PM > PSC:
    print('Empréstimo negado!')
elif PM <= PSC:
    print('Empréstimo aprovado!')
