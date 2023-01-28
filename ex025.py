# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome
n = str(input('Qual o seu nome?')).strip()
print('O nome contém "Silva"? {}'.format("Silva" in n.title()))
