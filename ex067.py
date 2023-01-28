# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número 
# solicitado for negativo.
c = r = p = 0
while p > -1: # while True: para laços infinitos
    num = int(input('Deseja ver a tabuada de que número? '))
    if num < 0:
        print('Processo encerrado.')
        break
    print(37 * '-')
    for c in range(0, 10):
        c += 1
        r = c * num
        print(f'{c} x {num} = {r}')
    print(37 * '-')
