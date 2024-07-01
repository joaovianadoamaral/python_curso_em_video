desafio = 'desafio 64'
print(f'{desafio:=^25}')
"""
leia vários números inteiros pelo teclado.
ultilize o flag 999, ou seja, se o usuario digitar 999 o programa para.
não use ele na conta da soma entre os inteiros
"""
num = -1
soma = 0
while num != 999:
    num = int(input('Digite um número(999 para sair) ->> '))
    if num != 999:
        soma += num
print('A soma dos números inteiros digitados é igual a: {}'.format(soma))
