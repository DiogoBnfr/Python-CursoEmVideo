# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
list = []
while True:
    num = int(input('Insira um número: '))
    if num not in list:
        list.append(num)
        conf = str(input('Deseja continuar [S/N]? '))
        if conf not in 'NnSs':
            print('Erro! Insira um valor válido.')
        else:
            if conf in 'Ss':
                pass
            else:
                break
    else:
        print('Valor repetido! Por favor, digite um valor único.')
list.sort()
print(f'Os números inseridos foram: {list}')