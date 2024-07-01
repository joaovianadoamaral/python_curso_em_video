#no lugar do igual pode-se adicionar qualquer caractere que ele vai preencher o espaço vazio
print('{:=^25}'.format('desafio05'))
#Leia um número inteiro e mostre na tela seu sucessor e seu antecessor
nint = int(input('digite um numero inteiro: '))
nint_suc = nint+1
nint_ant = nint-1
print('O numero digitado: {}\nO seu sucessor: {}\nO seu antecessor: {}'.format(nint, nint_suc, nint_ant))
