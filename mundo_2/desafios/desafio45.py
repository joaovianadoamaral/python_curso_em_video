from random import randint
from time import sleep
#Crie um programa que faça o computador jogar jokenpô com você
print('{:=^25}'.format('Desafio 45'))
#formatação de cores que irei usar
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo= '\033[35m'
padrao = '\033[m'
#inicio de programa
print('\033[34m-=-'*25)
print('{}Vamos jogar jokenpô? {}' .format(roxo, padrao))
print('\033[34m-=-\033[m'*25)
escolha = int(input('\033[35mEu escolhi uma opção, escolha a sua:\n'
      '(1) pedra\n'
      '(2) papel\n'
      '(3) tesoura\n'
      '->> '))
escmaquina = randint(1, 3)
#mostrar qual a escolha da maquina
if escmaquina == 1:
    escmaquina = 'pedra'
elif escmaquina == 2:
    escmaquina = 'papel'
elif escmaquina == 3:
    escmaquina = 'tesoura'
#mostrar qual a escolha do jogador
if escolha == 1:
    escolha = 'pedra'
elif escolha == 2:
    escolha = 'papel'
elif escolha == 3:
    escolha = 'tesoura'
#mostrar o jogador como vencedor
if escolha == 'pedra' and escmaquina == 'tesoura' or escolha == 'papel' and escmaquina == 'pedra' or escolha == 'tesoura' and escmaquina == 'papel':
    print('{}Jo{}'.format(roxo, padrao))
    sleep(1)
    print('{}ken{}'.format(roxo, padrao))
    sleep(1)
    print('{}PÔ{}'.format(roxo, padrao))
    sleep(1)
    print('{}Parabéns!!! Você conseguiu me vencer, '
          'eu escolhi {}{} {}e você escolheu {}{}{}'
          ''.format(verde, vermelho, escmaquina.upper(), verde, amarelo, escolha.upper(), padrao))
#mostra a maquina como vencedora
elif escmaquina == 'pedra' and escolha == 'tesoura' or escmaquina == 'papel' and escolha == 'pedra' or escmaquina == 'tesoura' and escolha == 'papel':
    print('{}Jo{}'.format(roxo, padrao))
    sleep(1)
    print('{}ken{}'.format(roxo, padrao))
    sleep(1)
    print('{}PÔ{}'.format(roxo, padrao))
    sleep(1)
    print('{}Eu ganhei perderdor, '
          'eu escolhi {}{} {}e você escolheu {}{}{}'
          ''.format(vermelho, amarelo, escmaquina.upper(), vermelho, verde, escolha.upper(), padrao))
#mostra o empate entre a maquina e o vencedor
elif escolha == escmaquina:
    print('{}Jo{}'.format(roxo, padrao))
    sleep(1)
    print('{}ken{}'.format(roxo, padrao))
    sleep(1)
    print('{}PÔ{}'.format(roxo, padrao))
    sleep(1)
    print('{}Nós empatamos mas da próxima vez eu ganharei, '
          'eu escolhi {}{} {}e você escolheu {}{}{}'
          ''.format(amarelo, vermelho, escmaquina.upper(), amarelo, verde, escolha.upper(), padrao))
else:
    print('{}Você digitou uma opção invalida{}'.format(vermelho, padrao))
