from datetime import date
print('{:=^25}'.format('Desafio32'))
#peça ao usuário um ano e descubra se esse ano é bissexto
#esse ano tem que ser dividido por 4
#exceto anos multiplos de 100 que não são multiplos de 400
ano = int(input('Digite um ano ou 0 para o ano atual-> '))
if ano == 0:
    ano = date.today().year
bissexto = ano % 4
if bissexto == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano de {} é um ano bissexto'.format(ano))
else:
    print('O ano de {} não é um ano bissexto'.format(ano))
