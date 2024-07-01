print('{:=^25}'.format('Desafio37'))
"""
peça o usuario um número inteiro qualquer, pergunte ele 
qual a base de conversão
-1 para binário
-2 para octal
-3 para hexadecimal
"""
num = int(input('Digite um número inteiro -> '))
escolha = int(input('{}Digite a opção de escolha:\n'
                    '-(1) para binario\n'
                    '-(2) para octal\n'
                    '-(3) para hexadecimal\n'
                    '->>> {}'.format('\033[33;40m', '\033[m')))
#usar[2: significa que quero ignorar o indicativo de base como 0b, 0o e 0x
if escolha == 1:
    binario = bin(num)
    print('O número {} em binário é: {}'.format(num, binario[2:]))
elif escolha == 2:
    octal = oct(num)
    print('O número {} em octal é: {}'.format(num, octal[2:]))
elif escolha == 3:
    hexadecimal = hex(num)
    print('O número {} em hexadecimal é: {}'.format(num, hexadecimal[2:]))
else:
    print('{}Você digitou uma escolha invalida{}'.format('\033[31m', '\033[m'))
