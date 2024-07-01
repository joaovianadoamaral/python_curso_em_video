print('{:=^25}'.format('Desafio 51'))
#leia o primeiro termo e a razão de uma PA, mostre os 10 primeiros termos dessa progressão
pt = float(input('Digite qual o primeiro termo da PA-> '))
razao = float(input('Digite qual a razão da PA -> '))
#mostra os 10 primeiros números da PA
print('Veja os 10 primeiros digitos da sequencia')
soma = 0
for i in range(0, 10):
    pa = pt + razao*i
    soma += pa
    print(pa, end='->')
print('\nO somatorio dos {} primeiros números da PA é {}'.format(i+1, soma))
