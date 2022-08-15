from random import randint
from time import sleep
PC = randint(0, 10) #faz o sorteio dos números entre 0 a 10
print('-=-'*20)
print('Vou pensar em um numero de 0 a 10 tente advinhar... ')
print('-=-'*20)
jogador = int(input('Em qual número eu pensei? '))
print('PROCESANDO...')
sleep(3)
if jogador == PC:
    print('OH NÃO, você conseguiu me vencer!!!')
else:
    print(f'ganhei ! pensei no número {PC} e não no {jogador}')


# velo = int(input('Qual é a velocidade do carro? '))
# multa = (velo-80)*7
# if velo > 80:
#     print('A multa vai custar R$ 7,00 por cada Km acima do limite')
#     print(f'Você está multado! você pagará {multa:.2f}')
# print('Boa Viajem.')

            #Descobrir se o número é par ou impar
# n1 = int(input('Digite um número: '))
# result = n1 % 2
# if result == '0':
#     print('par')
# else:
#     print('impar')












