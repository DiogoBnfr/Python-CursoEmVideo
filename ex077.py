# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

words = ('trabalhar', 'estudar', 'acordar', 'programar', 'python', 'curso', 'futuro')

for word in words:
    print(f'\nNa palavra {word.upper()} as vogais são: ', end='')
    for letter in word:
        if letter in 'aeiou':
            print(letter, end=' ')