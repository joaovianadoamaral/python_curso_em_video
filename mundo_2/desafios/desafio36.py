print('{:=^25}'.format('Desafio36'))
"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa vai perguntar o valor da Casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o Valor da prestação mensal, sabendo que ela não pode exceder 30% do salário senão o emprestimo será negado
"""
salario = float(input('Qual o seu salário? R$'))
casa = float(input('Qual o valor da casa? R$'))
temp = int(input('Em quantos anos você irá pagar? '))
#valor da casa divido pela quantidade de meses
mensalidade = casa/(temp*12)
if mensalidade <= .3*salario:
    print('{}Parabens!!, o empréstimo foi aprovado'.format('\033[0;32m'))
    print('A prestação sera de R${:.2f} por mês'.format(mensalidade))
else:
    print('{}O empréstimo foi recusado'.format('\033[0;31m'))
    print('A prestação seria de R${:.2f} por mês'.format(mensalidade))
print('O máximo de cada parcela aceita para o seu salário é {}'.format(.3*salario))