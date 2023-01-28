# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:                                                                                                    
# A) Quantas pessoas foram cadastradas.                                                                                                                
# B) Uma listagem com as pessoas mais pesadas.                                                                                                    
# C) Uma listagem com as pessoas mais leves.

people = []
min_weight_name = []
max_weight_name = []
data = []
repeat = 0

while True:
    repeat += 1
    data.append(str(input('Nome: ')))

    data.append(int(input('Peso: ')))
    if repeat == 1:
        min_weight = data[1]
        max_weight = data[1]
        min_weight_name.append(data[0])
        max_weight_name.append(data[0])

    else:
        if data[1] < min_weight:
            min_weight = data[1]
            min_weight_name.clear()
            min_weight_name.append(data[0])
        else:
            if data[1] == min_weight:
                min_weight_name.append(data[0])

        if data[1] > max_weight:
            max_weight = data[1]
            max_weight_name.clear()
            max_weight_name.append(data[0])
        else:
            if data[1] == max_weight:
                max_weight_name.append(data[0])

    people.append(data[:])
    data.clear()

    c = str(input('Deseja continuar [S/N]? '))
    if c in 'SsNn':
        if c in 'Ss':
            pass
        else:
            break
    else:
        print('Erro! O valor inserido é invalido.')

if len(people) == 1:
    print(f'{len(people)} pessoa foi cadastrada.')
else:
    print(f'{len(people)} pessoas foram cadastradas.')

print(f'O maior peso registrado foi {max_weight}. Peso de {max_weight_name}.')
print(f'O menor peso registrado foi {min_weight}. Peso de {min_weight_name}')