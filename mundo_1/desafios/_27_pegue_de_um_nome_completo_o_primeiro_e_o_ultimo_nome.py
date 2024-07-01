print('{:=^25}'.format('Desafio27'))
"""
faça um programa que leia o nome completo de uma pessoa,mostrando
em seguida o primeiro e o ultimo nome separadament.
ex: Ana Maria de Souza 
primeiro = Ana 
último = Souza
"""
nome = str(input('Digite seu nome completo -> '))
#separar o nome em uma lista de palavras no qual é possivel descobrir o tamanho com len()
aux = nome.split()
tam = len(aux)
#para joao vitor viana do amaral, tam = 5
#logo usaremos 'tam - 1', já que o indice começa em 0
print('Primeiro = {}'.format(aux[0]))
print('Último = {}'.format(aux[tam-1]))
