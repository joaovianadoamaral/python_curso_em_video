print('{:=^25}'.format('desafio04'))
#Faça um programa que leia algo pelo teclado,mostre seu tipo primitivo e todas as informações sobre ele
teste = input('digite algo na tela: ')
print('a classe primitiva do que voce digitou é {}\n'.format(type(teste)))
print('ele é um numero: {}'.format(teste.isnumeric()))
print('ele é so alfabetico: {}'.format(teste.isalpha()))
print('ele é um alfanumero: {}'.format(teste.isalnum()))
print('ele possui todas as letras maiusculas: {}'.format(teste.isupper()))
print('ele possui todas as letras minusculas: {}'.format(teste.islower()))
print('ele é um codigo ascii: {}'.format(teste.isascii()))
#existem outros porem não sei oq significam ainda
