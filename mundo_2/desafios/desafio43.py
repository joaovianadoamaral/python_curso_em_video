print('{:=^25}'.format('Desafio43'))
"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa.
calcule sue IMC e mostre seu status, de acordo com a tabela
abaixo:
- abaix de 18.5: abaixo do peso
- entre 18.5 e 24.9: peso ideal
- entre 25 até 29.9: sobrepeso
- 30 até 39.9 : obesidade
- acima de 40: obesidade morbida
"""
altura = float(input('Digite sua altura em metros-> '))
peso = float(input('Digite seu peso em Kg-> '))
#calculo imc
imc = peso / altura ** 2
#grau de obesidade
if imc < 18.5:
    grau = 'abaixo do peso'.upper()
    print('O seu imc é {}{:.1f}{} e você está {}{}{}'.format('\033[31m', imc, '\033[m', '\033[31m', grau, '\033[m',))
elif imc >= 18.5 and imc < 25:
    grau = 'no peso ideal'.upper()
    print('O seu imc é {}{:.1f}{} e você está {}{}{}'.format('\033[33m', imc, '\033[m', '\033[32m', grau, '\033[m', ))
elif imc >= 25 and imc <30:
    grau = 'com sobrepeso'.upper()
    print('O seu imc é {}{:.1f}{} e você está {}{}{}'.format('\033[32m', imc, '\033[m', '\033[33m', grau, '\033[m', ))
elif imc >= 30 and imc < 40:
    grau = 'com obesidade'.upper()
    print('O seu imc é {}{:.1f}{} e você está {}{}{}'.format('\033[33m', imc, '\033[m', '\033[33m', grau, '\033[m', ))
else:
    grau = 'com obesidade morbida'.upper()
    print('O seu imc é {}{:.1f}{} e você está {}{}{}'.format('\033[31m', imc, '\033[m', '\033[31m', grau, '\033[m', ))