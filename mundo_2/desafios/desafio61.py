print('{:=^25}'.format('Desafio 61'))
"""
leia o primeiro termo de uma PA e sua razão
mostre os 10 primeiros termos
use while e não for
"""

pt = float(input('Digite o primeiro termo da PA ->'))
razao = float(input('Digite a razão dessa PA ->'))
# mostrar os 10 primeiros termos
aux = 0
soma = 0
while aux < 10:
    aux += 1
    # somatorio dos n termos mostrados da PA
    if aux == 1:
        soma = pt
    else:
        soma += pt
    # mostra os números da pa
    print('{}'.format(pt), end=' ')
    # próximo termo
    pt += razao
print('\nFim da Pa')
print('Soma dos 10 primeiros termos dessa PA: {}'.format(soma))
