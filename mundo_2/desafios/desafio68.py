from random import randint
print('{:=^25}'.format('Desafio 68'))
"""
Jogue par ou impar com o usuario
peça um número
P OU I
O jogo só acaba quando o usuario perder
mostre o total de vitórias consecutivas.
"""
print('-=-'*20)
print('Vamos jogar PAR ou ÍMPAR!!')
print('-=-'*20)
vitoria = 0
while True:
    # leitura do número do usuario
    num = int(input('Digite um número: '))
    if num < 0:
        while num < 0:
            num = int(input('Numero inválido! digite outro ->> '))
    # par ou impar
    pi = str(input('Qual você quer [P/I] ->> ')).strip()
    # verifica se ele digitou algo que não é ou P, ou I
    if pi not in 'P p I i':
        while pi not in 'P p I i':
            pi = str(input('Opção invalida!! Qual você quer [P/I] ->> ')).strip()
    # resultado
    num_sis = randint(0, 10)
    print('-=-' * 20)
    print(f'Você jogou {num} e eu joguei {num_sis}')
    # se par e o usuario digitou par
    if (num_sis + num) % 2 == 0 and pi in 'P p':
        print('-=-' * 20)
        print('Você venceu !!!\nVamos jogar novamente....')
        print('-=-' * 20)
        vitoria += 1
    elif (num + num_sis) % 2 == 1 and pi in 'I i':
        print('-=-'*20)
        print('Você venceu !!!\nVamos jogar novamente....')
        print('-=-' * 20)
        vitoria += 1
    # o usuario perdeu e interrompe o loop
    else:
        break
print('GAME OVER!!')
print(f'Você obteve {vitoria} vitorias consecutivas')
