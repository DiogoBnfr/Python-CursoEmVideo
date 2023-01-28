# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
# Primeira forma:
for n1 in range(0, 50+1, 2):
    print('.', end='')
    print(n1, end=' ')
print('FIM!')

# Segunda forma:
for n2 in range(0, 51):
    print('.', end='')
    if n2 % 2 == 0:
        print(n2, end=' ')
print('FIM!')

# Demonstrações de uso de processamento do script.
