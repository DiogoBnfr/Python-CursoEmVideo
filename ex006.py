# Crie um algoritmo que leia um número e mostre o seu dobro, seu triplo e sua raiz quadrada.
num = int(input('Digite um número:'))
d = int(num) * 2
t = int(num) * 3
r = int(num) ** 0.5
print('O dobro de {} vale {} \n O triplo de {} vale {} \n A raiz quadrada de {} vale {}'.format(num, d, num, t, num, r))
