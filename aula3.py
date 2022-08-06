# n1 = int(input('digite um numero:'))
# n2 = int(input('digite outro numero:'))
# s = n1 + n2
# print('A soma entre {} e {} é {}'.format(n1, n2, s))

a = input('Digite algo: ')
print('O tipo primitivo desse valor é',type(a))
print('só tem espaços? ',a.isspace())
print('é um numero?', a.isnumeric())
print('é alfabetico?', a.isalpha())
print('é alfanumerico?', a.isalnum())
print('está em maiusculas?', a.isupper())
print('está em minusculas?', a.islower())
print('está capitalizada?', a.istitle())

palavra = input('digite algo:')
print('só tem espaço?{}'.format(palavra.isspace()))    #usando o format



