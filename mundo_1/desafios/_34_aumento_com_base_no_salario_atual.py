print('{:=^25}'.format('Desafio34'))
"""
Escreva um programa que pergunte o sálario de um funcionário e calcule o vlaor do 
seu aumento.
*para salários superiores a R$1.250,00 calcule um aumento de 10%
*para salários inferiores ou iguais o aumento é de 15%
"""
salario = float(input('Digite o salário do funcionário ->'))
if salario <= 1250:
    aumento = salario * 1.15
    prct = 15
else:
    aumento = salario * 1.10
    prct = 10
print('Para o salario de R${:.2f} houve um aumento de {}%'.format(salario, prct))
print('Novo salário: R${:.2f}'.format(aumento))
