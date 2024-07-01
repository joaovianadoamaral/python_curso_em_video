print('{:=^25}'.format('Desafio30'))
#leia um número na tela e digite se ele é par ou impar
num = int(input('Digite um número -> '))
parimpa = num % 2
if parimpa == 0:
    print('O número digitado é par')
else:
    print('O número digitado é impar')
 