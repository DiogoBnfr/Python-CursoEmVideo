# Faça um programa que leia nome e média de um aluno, guardando também a 
# situação em um dicionário. No final, mostre o conteúdo da estrutura na 
# tela.
data = {}
data['Aluno'] = str(input('Aluno: ')).capitalize()
while True:
    data['Média'] = float(input('Média do Aluno: '))
    if data['Média'] < 5:
        data['Situação'] = 'Reprovado'
        break
    elif 5 <= data['Média'] <= 6:
        data['Situação'] = 'Recuperação'
        break
    elif 10 >= data['Média'] > 6 :
        data['Situação'] = 'Aprovado'
        break
    else:
        print('Erro! Insira uma média entre 0 e 10.')
for k, v in data.items():
    print(f'{k}: {v}')