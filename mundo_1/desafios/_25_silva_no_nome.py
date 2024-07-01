print('{:=^25}'.format('Desafio 25'))
#leia o nome de uma pessoa e verifique se ela possui 'Silva' no nome
nome = str(input('Digite o seu nome completo -> '))
aux = 'SILVA' in nome.upper()
print('O seu nome possui Silva? {}'.format(aux))
