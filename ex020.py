# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.Faça um programa que leia
# o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
al1 = str(input('Primeiro aluno:'))
al2 = str(input('Segundo aluno:'))
al3 = str(input('Terceiro aluno:'))
al4 = str(input('Quarto aluno:'))
list = [al1, al2, al3, al4]
shuffle(list)
print('A ordem das apresentações será: \n{}'.format(list))
