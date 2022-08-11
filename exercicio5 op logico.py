idade = int(input('Qual sua idade: '))
peso = float(input('Qual seu peso: '))
alt = float(input('Qual sua altura: '))

if idade >= 18 and peso >= 60 and alt >= 1.70:
    print('está apto para entrar no exercito')
else:
    print('não está apto para entrar no exercito')