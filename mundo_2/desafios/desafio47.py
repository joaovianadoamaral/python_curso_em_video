print('{:=^25}'.format('Desafio 47'))
#faça um programa que mostre todos os números pares entre 1 e 50
print('Veja todos os números pares entre 1 e 50')
for par in range(2, 51, 2):
    # para não pular para a próxima linha damos um and com um espaço
    print(par, end=' ')
