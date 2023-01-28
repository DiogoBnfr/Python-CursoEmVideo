# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
pt = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
c = 0
t = pt
while c < 10:
    if c < 9:
        print(f'{t} > ', end ='')
    else:
        print(f'{t}', end ='')
    t += r
    c += 1