print('{:=^25}'.format('Desafio 22'))
"""
Faça um programa que leia um número de 0 9999 e mostre na tela cada um dos digitos
separados.

ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1

faça matematicamente e por string
"""
#string
numero = str(input('Digite na tela um número entre 0 e 9999 -> '))
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(numero[3], numero[2], numero[1], numero[0]))
#número
num = int(input('Digite na tela um número entre 0 e 9999 -> '))
aux = num
#é possivel continuar a sequencia para cima seguindo a lógica a baixo
#faz a divisão inteira para receber o digito mais significativo
#guarda ele e retira sua casa decimal. se obtem um novo número e repete
milhar = aux//1000
aux = aux - milhar * 1000
centena = aux//100
aux = aux - centena * 100
dezena = aux//10
aux = aux - dezena * 10
unidade = aux
"""
maneira fácil de fazer:
unidade = num//1 % 10
dezena = num//10 % 10
centena = num//100 % 10
milhar = num//1000 % 10
"""
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))
