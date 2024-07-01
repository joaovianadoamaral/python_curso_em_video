print('{:=^25}'.format('Desafio 60'))
"""
faça um programa que leia um número qualquer 
e mostre o seu fatorial
não existe o fatorial de números negativos
fatorial de 0 é 1
"""
num = int(input('Digite um número -> '))
aux = 1
if num > 0:
    print('{}! = '.format(num), end='')
    if num > 1:
        while num != 1:
            if aux == 1:
                fatorial = num
                aux += 1
            else:
                fatorial *= num
            print('{}x'.format(num), end='')
            num -= 1
    else:
        fatorial = 1
    print('1 = {}'.format(fatorial))
elif num == 0:
    fatorial = 1
    print('O fatorial desse número é {}'.format(fatorial))
else:
    print('O fatorial desse número não existe')
