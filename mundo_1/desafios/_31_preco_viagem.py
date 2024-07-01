print('{:=^25}'.format('Desafio31'))
"""
pergunte ao usuário a distancia da viagem em km's e mostre a ele o preço da passagem.
para viagens de até 200 Km cobre R$0,50/Km
para viagens maiores cobre R$0,45/Km
"""
km = float(input('Digite a distância da viagem em Km -> '))
if km <= 200:
    preco = km * .50
    print('O valor da viagem será: R${:.2f}'.format(preco))
else:
    preco = km * .45
    print('O valor da viagem será: R${:.2f}'.format(preco))
print('Tenha uma boa viagem')
