#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
#  quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos km o carro percorreu?'))
dias = int(input('Por quantos dias o carro foi alugado?'))
alug = (0.15 * km) + (60 * dias)
print('O valor do aluguel será de R${}.'.format(alug))
