# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em 
# uma lista composta. No final, mostre um boletim contendo a média de cada um e 
# permita que o usuário possa mostrar as notas de cada aluno individualmente.
from time import sleep
alunos = []
aluno = []
while True:
    aluno.append(str(input('Nome do aluno: ')))
    aluno.append(float(input('Primeira nota: ')))
    aluno.append(float(input('Segunda nota: ')))
    alunos.append(aluno[:])
    aluno.clear()    
    if str(input('Deseja continuar[S/N]? ')) in 'Ss':
        pass
    else:
        break
print('-' * 30)
print(f'{"N."}{"NOME":^12}{"MÉDIA":^16}')
print('-' * 30)
for aluno in alunos:
    print(f'{alunos.index(aluno)}{aluno[0]:^16}{aluno[1] + aluno[2] / 2:^10}')
print('-' * 30)
while True:    
    n = int(input('Insira o número do aluno que deseja ver as notas [00 para encerrar]: '))
    if n == 00:
        print('Encerrando. . .')
    elif n <= len(alunos) - 1:
        print('-' * 30)
        print(f'{alunos[n][0]}{alunos[n][1]:^16}{alunos[n][2]:^10}')
        print('-' * 30)
    else:
        print('Erro! O valor digitado não corresponde à nenhum dos alunos cadastrados.')
