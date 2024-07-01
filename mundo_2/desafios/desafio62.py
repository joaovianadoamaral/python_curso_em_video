desafio = 'deasfio62'
print(f'{desafio:=^25}')
# método fstring
"""
melhore o desafio 61.
mostre os 10 primeiros números da pa
pergunte ao usuário se ele quer continuar? se sim mais quantos números da sequencia
o programa para quando ele digitar que quer mais 0 termos
"""
# loop até num == 1
num = -1
a = 1
b = 11
# leitura das variaveis
pt = float(input('Digite o primeiro termo dessa PA -> '))
razao = float(input('Digite a razão dessa PA -> '))
while num != 0:
    # mostrar os 10 primeiros termos + adicionais
    for i in range(a, b):
        if i == 1:
            print(f'O {i}° termo dessa PA é: {pt}')
        else:
            pt += razao
            print(f'O {i}° termo dessa PA é: {pt}')
    # mostra os próximos termos dessa PA
    print('-=-'*15)
    num = int(input('Mais quantos termos da PA o usuario deseja(0 para terminar)-> '))
    print('-=-'*15)
    # verifica se o usuario digitou um número negativo de vezes
    if num < 0:
        while num < 0:
            num = int(input('número inválido. digite um número inteiro não negativo-> '))
            print('-=-' * 15)
    a = b
    b = b + num
print('FIM...')
