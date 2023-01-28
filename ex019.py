# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
# ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# Primeira forma:
import random
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno:'))
lista = [a1, a2, a3, a4]
esc = random.choice(lista)
print('O aluno escolhido foi: {}'.format(esc))

# Segunda forma:
al1 = str(input('Primeiro aluno:'))
al2 = str(input('Segundo aluno:'))
al3 = str(input('Terceiro aluno:'))
al4 = str(input('Quarto aluno:'))
list = [al1, al2, al3, al4]
print('O aluno escolhido foi: {}'.format(random.choice(list)))
