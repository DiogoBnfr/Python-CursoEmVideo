# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
analysis = []
expression = str(input('Digite a expressão matemática: '))
for caractere in expression:
    if caractere == '(':
        analysis.append('(')
    elif caractere == ')':
        if len(analysis) > 0:
            analysis.pop()
        else:
            analysis.append(')')
            break
if len(analysis) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')