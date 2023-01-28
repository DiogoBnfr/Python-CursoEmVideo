#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
A = int(input('Digite o comprimento do segmento A:'))
B = int(input('Digite o comprimento do segmento B:'))
C = int(input('Digite o comprimento do segmento C:'))
if A + B > C and A + C > B and B + C > A:
    if A == B and B == C:
        print('Com os segmentos acima é possível formar um triângulo equilátero.')
    elif A != B != C != A:
        print('Com os segmentos acima é possível formar um triângulo escaleno.')
    elif A == B or A == C or B == C:  # else também funciona nesse caso.
        print('Com esses segmentos é possível formar um triângulo isóceles.')
else:
    print('Não é possível formar um triângulo com os segmentos acima.')
