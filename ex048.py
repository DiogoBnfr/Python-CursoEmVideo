# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
r = 0
c = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        r += n
        c += 1
        print('[', n, ']', end=' - ')
        print('[', r, ']')
print('''QUANTIDADE TOTAL DE VALORES: {}'''.format(c))
print('FIM!')
