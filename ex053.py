# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(frase)
inverso = junto[::-1]
if inverso == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo!')
