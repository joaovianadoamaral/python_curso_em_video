print('{:=^25}'.format('Desafio42'))
"""
refaça o desafio 35(condição de existencia de um triangulo) mostrando se:
o triangulo é escaleno, isóceles ou equilatero
"""
#leitura de variaveis
l1 = float(input('Digite o 1° lado -> '))
l2 = float(input('Digite o 2° lado -> '))
l3 = float(input('Digite o 3° lado -> '))

#condição de existencia
if l1 + l2 > l3 and abs(l1 - l2) < l3 and l1 + l3 > l2 and abs(l1 - l3) < l2 and l2 + l3 > l1 and abs(l2 - l3) < l1:
    existe = True
else:
    existe = False
#contagem de lados iguais
# é preciso iniciar o cont com 0 (possivel erro)
cont = 0
if l1 == l2:
    cont += 1
if l1 == l3:
    cont += 1
#qual o tipo do triangulo
if existe:
    if cont == 0:
        print('Esse é um triangulo {}escaleno{}'.format('\033[32m', '\033[m'))
    elif cont == 1:
        print('Esse é um triangulo {}isoceles{}'.format('\033[32m', '\033[m'))
    else:
        print('Esse é um triangulo {}equilatero{}'.format('\033[32m', '\033[m'))
else:
    print('Esse triângulo não existe')
