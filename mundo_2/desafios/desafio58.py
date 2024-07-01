from random import randint
print('{:=^25}'.format('Desafio 58'))
# cores
amarelo = '\033[33m'
roxo = '\033[35m'
verde = '\033[32m'
vermelho = '\033[31m'
padrao = '\033[m'
"""
melhore o jogo do desafio 28.
computador vai pensar em um número entre 0 e 10 
o jogador vai tentar adivinhar até acertar.
moste ao jogador quantos palpites foram necessários para vencer
"""
# apresentação inicial
print('{}'.format(amarelo), end='')
print('-=-'*20)
print('{}Estou pensando em um número entre 0 e 10. tente advinha-lo{}'.format(roxo, amarelo))
print('-=-'*20)
print('{}'.format(padrao), end='')

# variaveis iniciais
numsis = randint(0, 10)
numjog = - 1
tentativa = 1
# iniciei o número do jogador diferente do número sorteado
while numjog != numsis:
    numjog = int(input(('{}{}° Tentativa -> {}'.format(roxo, tentativa, padrao))))
    tentativa += 1
print('{}Parabéns!! foi um bom jogo, eu tinha pensado no {}{}{}'.format(verde, vermelho, numsis, padrao))
print('{}Você gastou {}{} tentativas{}'.format(verde, vermelho, tentativa - 1, padrao))
