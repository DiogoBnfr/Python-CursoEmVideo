print('Calculadora SEQUÊNCIA DE FIBONACCI')
n = int(input('Digite quantos termos deseja calcular: '))
t1 = 1 
t2 = 1
print(f'{t1} > {t2} > ', end='')
while 2 < n:
    t3 = t1 + t2
    if n == 3:
        print(f'{t3}')
    else:
        print(f'{t3} > ', end='')
    t1 = t2
    t2 = t3
    n -= 1
