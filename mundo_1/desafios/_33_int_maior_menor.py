print('{:=^25}'.format('Desafio33'))
#faça um programa que leia 3 números, mostre o maior e o menor
num1 = int(input('Digite o 1° número -> '))
num2 = int(input('Digite o 2° número -> '))
num3 = int(input('Digite o 3° número -> '))
#condição maior
if num1 >= num2 and num1 >= num3:
    maior = num1
if num2 >= num1 and num2 >= num3:
    maior = num2
if num3 >= num1 and num3 >= num2:
    maior = num3
#condição menor
if num1 <= num2 and num1 <= num3:
    menor = num1
if num2 <= num1 and num2 <= num3:
    menor = num2
if num3 <= num1 and num3 <= num2:
    menor = num3
print('O menor número é o {}'.format(menor))
print('O maior número é o {}'.format(maior))
