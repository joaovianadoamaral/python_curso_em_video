#leia um número real qualquer pelo teclado e mostre sua porção inteira e sua porção real separadamente
from math import trunc
print('{:=^25}'.format('desafio16'))
num = float(input('Digite um número real qualquer: '))
inum = trunc(num)
fnum = num - inum
print('O número real: {:.3f}\npossui parte inteira: {}\npossui parte real {:.3f}'.format(num, inum, fnum))
