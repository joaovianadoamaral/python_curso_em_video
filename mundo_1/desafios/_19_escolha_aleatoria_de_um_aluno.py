from random import choice
print('{:=^25}'.format('Desafio19'))
#faça um programa que leia o nome de 4 alunos para que o professor sortei 1 e faça ele apagar o quadro
nome1 = input('Digite o nome do 1° aluno: ')
nome2 = input('Digite o nome do 2° aluno: ')
nome3 = input('Digite o nome do 3° aluno: ')
nome4 = input('Digite o nome do 4° aluno: ')
lista = [nome1, nome2, nome3, nome4]
#o metodo choice escolhe algo de uma sequencia não vazia
aux = choice(lista)
print('O aluno {} foi escolhido'.format(aux))
