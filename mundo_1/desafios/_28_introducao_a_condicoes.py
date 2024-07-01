from random import randint
from time import sleep
print('{:=^25}'.format('desafio28'))
#introdução a condições
print('-='*25)
print(('Vou pensar em um número entre 0 e 5.'))
print('-='*25)
num = int(input('Digite um número-> '))
ale = randint(0, 5)
print('processando...')
sleep(3)
if num == ale:
    print('Parabéns você acertou!!!')
else:
    print('Que pena você errou, o número era: {}'.format(ale))

