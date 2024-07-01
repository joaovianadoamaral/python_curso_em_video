print('{:=^25}'.format('Desafio 55'))
"""
Crie um programa que leia o peso de 5 pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""
"""
gambiarra
maior = -1000000000000
menor = 1000000000000
"""
for i in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(i)))
    # fugir da gambiarra, ocorre só no primeiro laço
    if i == 1:
        # só acontece uma vez devido ao auxiliar
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso encontrado foi: {}Kg'.format(maior))
print('O maior peso encontrado foi: {}Kg'.format(menor))
