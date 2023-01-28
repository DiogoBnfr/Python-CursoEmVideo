# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite o número que você deseja ver a tabuada:'))
x = 0
for t in range(0, n * 10 + 1, n):
    print(x, 'x', n, '=', t)
    x += 1

# Correção:
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} =  {}'.format(num, c, num * c))
     