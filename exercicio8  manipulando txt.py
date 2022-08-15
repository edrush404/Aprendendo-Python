# nome = str(input('Digite seu nome completo: ')).strip()
# print('Analisando seu nome.......')
# print(f'{nome.upper()}\n{nome.lower()}')
# print('{}'.format(len(nome)-nome.count(' ')))
# # print('{}'.format(nome.find(' '))) # em baixo de outra forma
# separar = nome.split()
# print('{}'.format(len(separar[0]))) # de outra forma

nome = str(input('Digite seu nome completo: ')).strip().split()
print(nome[0])
print(nome[-1])
