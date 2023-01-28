# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer 
# mostrar 0 termos.

count = 0

# Interface de terminal
print('Bem-vindo ao Gerador de Progressões Aritméticas 3.0')

# Dados necessários para o cálculo
term_quantity = int(input('Digite quantos termos deseja calcular: '))
if term_quantity == 0:
    pass
else:
    term_initial = int(input('Digite o termo inicial de sua progressão: '))
    term_reason = int(input('Digite a razão da sua progressão: '))
    count = term_quantity

while count > 0:
    if term_quantity != 0:
        if count > 1:
            print(f'{term_initial} > ', end='')
        else:
            print(f'{term_initial}')
        term_initial += term_reason
        count -= 1
        if count == 0:
            term_quantity = int(input('Digite quantos termos deseja calcular: '))
            if term_quantity == 0:
                pass
            else:
                term_initial = int(input('Digite o termo inicial de sua progressão: '))
                term_reason = int(input('Digite a razão da sua progressão: '))
                count = term_quantity
        else:
            pass
    else:
        count = 0
print('Encerrando calculadora...')
