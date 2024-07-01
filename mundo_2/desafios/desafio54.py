#importa o ano atual
from datetime import date
print('{:=^25}'.format('Desafio 54'))
"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final
mostre quantas pessoas ja atingiram a maioriadade e quantas não atingiram
"""
cont_ma = 0
cont_mi = 0
for i in range(1, 8):
    ano = int(input('Digite o ano em que a {}° pessoa nasceu: '.format(i)))
    idade = date.today().year - ano
    #considere a maioridade como 21 anos
    if idade >= 21:
        cont_ma += 1
    else:
        cont_mi += 1
print('Das pessoas digitadas {} são maiores de idade'.format(cont_ma))
print('Das pessoas digitas {} são menores de idade'.format(cont_mi))
