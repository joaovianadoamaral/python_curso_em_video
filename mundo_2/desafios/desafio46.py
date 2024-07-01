from emoji import emojize
from time import sleep
print('{:=^25}'.format('Desafio 46'))
#faça uma contagem regressiva de 10 a 0 segundos e mostre emoji de fogos de artificio
print('Vamos começar a contagem')
for contagem in range(10, 0, -1):
    print('{}'.format(contagem))
    sleep(1)
print(emojize('Hora dos fogos :fireworks: :fireworks: :fireworks:', language='alias'))
