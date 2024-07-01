print('{:=^25}'.format('Desafio 53'))
# Crie um programa que leia uma frase qualque e informe se ela é um palindromo desconsiderando os espaços
frase = str(input('Digite uma frase qualquer-> ')).strip().upper()
# eliminei os espaços da frase
frase = ''.join(frase.split())
tam = len(frase)
# pega a frase inversa
aux = 0
rev = ''
#poderiamos fazer de outra forma rev = fras[::-1]
# é necessario iniciar a frase reversa somente com aspas
for i in range(tam - 1, -1, -1):
    #concatena letra por letra até formar a frase inversa
    rev = rev + frase[i]
# verifica se o inverso é igual a frase digitada
print('O inverso de {} é {}'.format(frase, rev))
if frase == rev:
    print('A sua frase é um palindromo')
else:
    print('A sua frase não é um palindromo')
