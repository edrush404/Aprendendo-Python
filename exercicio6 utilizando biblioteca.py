# from math import hypot #biblioteca math e hypot = calcula a hipotenusa.
# oposto = float(input('Comprimento do cateto oposto: '))
# adjacente = float(input('Comprimento do  cateto adjacente: '))
# hipo = hypot(oposto, adjacente)
# print(f'A hipotenusa vai medir {hipo:.2f}')

# from math import radians, sin, cos, tan  #biblioteca math
# ang = float(input('Digite o ângulo que você deseja: '))
# sen = sin(radians(ang)) #sin calcular o seno e o radians para converter
# coss = cos(radians(ang))  #cos calcular o cosseno
# tan = tan(radians(ang)) #tan calcular o tangente
# print('O ângulo de {} tem o Seno de {:.2f}'.format(ang, sen))
# print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang, coss))
# print('O ângulo de {} tem o tangente de {:.2f}'.format(ang,tan))

             #SORTEANDO UM ITEM DA LISTA
from random import choice #biblioteca random e choice para escolher nome aleatorios
n1 = input('primeiro aluno: ')
n2 = input('segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista) #choice
print(f'Escolhido foi {escolhido}')

#             #SORTEANDO UMA ORDEM NA LISTA
# from random import shuffle # shuffle para sortear todos da lista
# n1 = input('primeiro aluno: ')
# n2 = input('segundo aluno: ')
# n3 = input('terceiro aluno: ')
# n4 = input('quarto aluno: ')
# lista = [n1, n2, n3, n4]
# shuffle(lista) #shuffle
# print(f'A ordem de apresentação será\n{lista}')






