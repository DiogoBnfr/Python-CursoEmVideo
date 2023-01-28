#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
# seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
P = float(input('Digite seu peso (em quilogramas):'))
A = float(input('Digite sua altura (em metros):'))
IMC = P / A ** 2
print('Resultado:', end=' ')
if IMC < 18.5:
    print('Abaixo do peso')
elif 25 > IMC >= 18.5:
    print('Peso ideal')
elif 30 > IMC >= 25:
    print('Sobrepeso')
elif 40 > IMC >= 30:
    print('Obesidade')
else:
    print('Obesidade mórbida')
