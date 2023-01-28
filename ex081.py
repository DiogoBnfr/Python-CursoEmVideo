# Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:                                                                                                                                                
# A) Quantos números foram digitados.                                                                                                                    
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.
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
        break
print(f'''Lista: {list}
Foram digitados {len(list)} número(s)
Lista inversa: {sorted(list, reverse = True)}''')
if 5 in list:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')

