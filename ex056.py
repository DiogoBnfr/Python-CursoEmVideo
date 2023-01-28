soma = 0
velho = 0
cont = 0
patriarca = ''
contador = 0
print('CADASTRO SOCIAL')
user = int(input('Quantas pessoas deseja cadastrar?'))
for c in range(1, user + 1):
    contador += 1
    print(' - - - - {}a pessoa - - - - '.format(c))
    nome = str(input('Digite seu nome:')).capitalize().strip()
    idade = int(input('Digite sua idade:'))
    print('[ M ] Masculino')
    print('[ F ] Feminino')
    sexo = str(input('Digite seu sexo:')).upper().strip()
    soma += idade
    if c == 1 and sexo == 'M':
        patriarca = nome
        velho = idade
    else:
        if idade > velho and sexo == 'M':
            patriarca = nome
    if sexo == 'F' and idade < 20:
        cont += 1
media = soma / contador
print('A média de idade do grupo é de: {:.2f} anos'.format(media))
if patriarca == '':
    print('Não há homens no grupo')
else:
    print('O homem mais velho do grupo é: {}'.format(patriarca))
if cont == 0:
    print('O grupo não possui mulheres com menos de 20 anos')
elif cont == 1:
    print('Ao total, o grupo possui {} mulher com menos de 20 anos'.format(cont))
else:
    print('Ao total, o grupo possui {} mulheres com menos de 20 anos'.format(cont))
