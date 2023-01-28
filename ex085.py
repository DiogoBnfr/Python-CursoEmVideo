# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única 
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

impar = []
par = []
lista = [] # O mesmo pode ser feito através da expressão: lista = [[], []]

for c in range(1, 8):
    r = int(input(f'Insira o {c}o número:'))
    if r % 2 == 0:
        par.append(r)
    else:
        impar.append(r)
lista.append(sorted(impar)) # lista[0].append()
lista.append(sorted(par))

print(f'Os números ímpares digitados foram: {lista[0]}')
print(f'Os números pares digitados foram: {lista[1]}')
