# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
# Primeira forma:
num1 = int(input('Digite o primeiro valor:'))
num2 = int(input('Digite o segunndo valor:'))
num3 = int(input('Digite o terceiro valor:'))
if num1 > num2 and num1 > num3:
    print('O maior número é {}'.format(num1))
else:
    pass
if num2 > num1 and num2 > num3:
    print('O maior número é {}'.format(num2))
else:
    pass
if num3 > num1 and num3 > num2:
    print('O maior número é {}'.format(num3))

if num1 < num2 and num1 < num3:
    print('O menor número é {}'.format(num1))
else:
    pass
if num2 < num1 and num2 < num3:
    print('O menor número é {}'.format(num2))
else:
    pass
if num3 < num1 and num3 < num2:
    print('O menor número é {}'.format(num3))

# Segunda forma:
a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi: {}'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi: {}'.format(maior))
