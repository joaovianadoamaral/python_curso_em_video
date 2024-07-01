print('{:=^25}'.format('desafio06'))
#Crie um algoritimo que leia um número e mostre seu dobro, seu triplo e sua raiz quadrada
n=float(input('digite um número: '))
ndobro=n*2
ntriplo=n*3
nraiz=n**(1/2)
print('O numero digitado foi {:.3f}\nO seu dobro é: {:.3f}\nO seu triplo é: {:.3f}\nA sua raiz quadrada é: {:.3f}'.format(n, ndobro, ntriplo, nraiz))
