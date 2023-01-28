# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo 
# teclado. No final, mostre a matriz na tela, com a formatação correta.

x = 0
y = 1
matriz = [[], [], []]
for c in range(0, 9):
    x += 1
    n = int(input(f'Insira um número na {y}a linha, {x}a coluna:'))
    if y == 1:
        matriz[0].append(n)
    elif y == 2:
        matriz[1].append(n)
    else:
        matriz[2].append(n)
    if x == 3 or x == 6 or x == 9:
        y += 1
        x = 0
print(f'''{matriz[0]:^5}
{matriz[1]}
{matriz[2]}''')