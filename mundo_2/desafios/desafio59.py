print('{:=^25}'.format('Desafio 59'))
"""
faça um programa que leia dois valores e mostre um menu
1 somar
2 multiplicar
3 maior
4 novos números
5 sair do programa
qualquer outro número opcao invalida
"""
# cores
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
# valores
opcao = -1
while opcao != 5:
    print('{}'.format(amarelo), end='')
    print('-=-' * 20)
    n1 = float(input('{}Digite o 1° valor -> '.format(roxo)))
    n2 = float(input('Digite o 2° valor -> '))
    # menu
    print('{}'.format(amarelo), end='')
    print('-=-'*20)
    print('{}MENU'.format(roxo))
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    print('{}'.format(amarelo), end='')
    print('-=-'*20)
    opcao = int(input('->> '))
    # somar
    if opcao == 1:
        result = n1 + n2
        print('{}'.format(azul), end='')
        print('A soma de {} com {} é {}'.format(n1, n2, result))
    # multiplicar
    elif opcao == 2:
        result = n1 * n2
        print('{}'.format(azul), end='')
        print('A multiplicação de {} com {} é {}'.format(n1, n2, result))
    # maior
    elif opcao == 3:
        result = n1
        if n2 > result:
            result = n2
        if n1 == n2:
            print('{}'.format(azul), end='')
            print('Não existe maior número.')
        else:
            print('{}'.format(azul), end='')
            print('O maior número entre {} e {} é o {}'.format(n1, n2, result))
    # novos números
    elif opcao == 4:
        print('{}'.format(azul), end='')
        print('Vamos digitar novos valores...')
        continue
    # sair do programa
    elif opcao == 5:
        print('{}'.format(vermelho), end='')
        print('Saindo....')
        break
    else:
        print('{}'.format(vermelho), end='')
        print('Opção inválida! tente novamente.')
