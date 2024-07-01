print('{:=^25}'.format('Desafio38'))
"""
escreva um programa que leia dois números inteiros e compareos
mostre na tela as seguintes frases:
- o primeiro valor é maior
- o segundo valor é maior
- Não existe valor maior, os dois são iguais
"""
num1 = int(input('Digite o primeiro valor inteiro: '))
num2 = int(input('Digite o segundo valor inteiro: '))
#qual número é maior
if num1 > num2:
    maior = num1
    print('O primeiro valor é maior')
elif num1 < num2:
    maior = num2
    print('O segundo valor é o maior')
else:
    maior = num1
    print('Não existe valor maior, os dois são iguais ')
