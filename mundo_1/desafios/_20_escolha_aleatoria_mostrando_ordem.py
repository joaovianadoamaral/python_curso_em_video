from random import shuffle
print('{:=^25}'.format('Desafio20'))
#O mesmo professor do desafio anterior quer sortear a ordem de apresentações de
#trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre
#a ordem sorteada
nome1 = input('Digite o nome do 1° aluno -> ')
nome2 = input('Digite o nome do 2° aluno -> ')
nome3 = input('Digite o nome do 3° aluno -> ')
nome4 = input('Digite o nome do 4° aluno -> ')
ordem = [nome1, nome2, nome3, nome4]
shuffle(ordem)
#a maior sequencia que shuffle pode embaralhar é 2080
print('Segue a ordem de nomes: {}, {}, {} e {}'.format(ordem[0], ordem[1], ordem[2], ordem[3]))
#ao invés de dar um print em cada posição pode-se dar um print(ordem), que ja mostra tudo
