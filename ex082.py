# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.
list = []
while True:
    list.append(int(input('Digite um número: ')))
    conf = str(input('Deseja continuar [S/N]? '))
    if conf in 'SsNn':
        if conf in 'Ss':
            pass
        else:
            break
    else:
        print('Insira um valor válido.')   
pos = 0
list_1 = []
list_2 = []
while pos < len(list):
    if list[pos] % 2 == 0:
        list_2.append(list[pos])
    else:
        list_1.append(list[pos])
    pos += 1
print(f'''Lista: {sorted(list)}
Números ímpares inseridos: {sorted(list_1)}
Números pares inseridos: {sorted(list_2)}''')
