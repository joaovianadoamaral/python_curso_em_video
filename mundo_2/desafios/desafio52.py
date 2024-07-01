print('{:=^25}'.format('Desafio 52'))
# faça um programa que peça ao usuario para digitar um número inteiro e mostrar se ele é um número primo ou não
num = int(input('Digite um número inteiro -> '))
# Tem que ser divisivel por 1 e por ele mesmo
# basicamente os primeiros primos são 1, 3, 5, 7 e 11. Da para descobrir o resto
cont = 0
for aux in range(1, num+1):
    if num % aux == 0:
        cont += 1
# como um número só é primo se existirem somente dois divisores, fiz um for e contei os divisores
# o 1 é excessão, vai contar somente uma vez
# como um número maior que o outro não pode atrapalhar ele ser primo ou não, testa-se apenas os menores ou iguais
if cont == 2:
    print('O número que você digitou é um número PRIMO')
else:
    print('O número que você digitou não é um número PRIMO')
