# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela
# aparece a primeira vez e em que posição ela aparece a última vez.
f = str(input('Digite uma frase:')).strip().lower()
print('A letra "A" aparece {} vezes na frase'.format(f.count('a')))
print('A letra "A" aparece pela primeira vez na posição: {}'.format(f.find('a')+1))
print('A letra "A" aparece pela última vez na posição: {}'.format(f.rfind('a')+1))
