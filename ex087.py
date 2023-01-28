# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

# Contém correção de formatação da matriz anterior.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor[{linha + 1}:{coluna + 1}]:'))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
for linha in matriz:
    for numero in linha:
        if numero % 2 == 0:
            par += numero
print(f'A soma dos números pares inseridos é igual a: {par}')
print(f'A soma dos valores inseridos na terceira coluna é igual a: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor inserido na segunda linha é: {max(matriz[1])}')
