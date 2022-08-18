casa = float(input('valor da casa: R$'))
salario = float(input('salário do comprador: R$'))
anos = int(input('quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'para pagar uma casa de {casa:.2f}\nem {anos} anos\nvalor para pagar 1 ano {prestacao:.2f}')
if prestacao <= minimo:
    print('emprestimo concedido')
else:
    print('emprestimo negado')




