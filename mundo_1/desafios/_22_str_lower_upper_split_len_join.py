print('{:=^25}'.format('desafio22'))
"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
* O nome com todas as letras maiusculas
* O nome com todas as letras minusculas
* Quantas letras têm o nome sem considerar os espaços
* Quantas letras têm o primeiro nome
"""
nome = str(input('Digite o seu nome completo -> '))
#minuscula e maiuscula
nome_mi = nome.lower()
nome_ma = nome.upper()
#tamanho sem espaços, separei e juntei sem espaços
aux = nome.split()
aux = ''.join(aux)
tam_nome = len(aux)
#quantas letras têm o primeiro nome, separei e peguei a primeira palavra da lista
aux = nome.split()
aux = len(aux[0])
#mostrar na tela
print('Olá {}! Veja na tela algumas curiosidades:\n\nSeu nome com letras maiúsculas: {}\nSeu nome com letras minúsculas: {}\nQuantas letras tem seu nome: {}\nQuantas letras tem o seu primeiro nome:{}'.format(nome, nome_ma, nome_mi, tam_nome, aux))
