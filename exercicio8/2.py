# n1 = int(input('Informe um número: '))
# u = n1 // 1 % 10
# d = n1 // 10 % 10
# c = n1 // 100 % 10
# m = n1 // 1000 % 10
# print(f'Analisando o numero {n1}')
# print(f'Unidade {u}')
# print(f'Dezena {d}')
# print(f'Centena {c}')
# print(f'Milhar {m}')

# cid = str(input('Em que cidade você nasceu? ')).strip()
# lista = cid.split()
# print(lista[0].lower() == 'santo')

# nome = str(input('Qual é seu nome completo? ')).strip()
# print('seu nome tem Silva? {}'.format('silva' in nome.lower()))

frase = str(input('Digite uma frase: ')).lower() .strip()
print('A Letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('a')+1))