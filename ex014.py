# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
cels = float(input('Digite a temperatura em °C:'))
fare = cels * 1.8 + 32
print('A temperatura de {}°C equivale a {}°F'.format(cels, fare))
