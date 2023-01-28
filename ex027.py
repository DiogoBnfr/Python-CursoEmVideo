# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.

# Primeira forma:
n1 = str(input('Digite seu nome completo:')).strip().title().split()
nome1 = "-".join(n1)
c = nome1.rfind('-')+1
print('Seu primeiro nome é: {}'.format(n1[0]))
print('Seu último nome é: {}'.format(n1[c:]))

# Segunda forma:
n2 = str(input('Digite seu nome completo:')).strip()
nome2 = n2.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome2[0]))
print('Seu último nome é {}'.format(nome2[len(nome2)-1]))
