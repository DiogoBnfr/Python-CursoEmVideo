num = int(input('Insira um número:'))
analysis = num % 2
if analysis == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))
