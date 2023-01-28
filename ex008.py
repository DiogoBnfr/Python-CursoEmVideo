# Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm.
m = float(input('Digite o valor em metros:'))
cm = float(m) * 10 * 10
mm = float(m) * 10 * 10 * 10
print('Valor inicial: {}m\n Em centímetros: {}cm\n Em milímetros: {}mm'.format(m, cm, mm))
