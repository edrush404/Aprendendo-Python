# nome = input('qual é seu nome? ')
# print('Prazer em conhecer Sr {:10}!'.format(nome))

n1 = int(input('um numero? '))
n2= int(input('outro numero? '))
s = n1+n2
m = n1*n2
d = n1/n2
sub = n1-n2
divI = n1//n2
pot = n1**n2
por = n1%n2
print('A somas é {} e a multiplicação é {} a divisão é {:.1f}'.format(s, m, d), end=' >>>>>> ') #end para ficar tudo na mesma linha
print('A subtração é {} divisão inteiro {} potencia {} e porcetagem {}'.format(sub, divI, pot, por))