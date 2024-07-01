#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
from math import tan,cos,sin,radians
print('{:=^25}'.format('Desafio18'))
ang = float(input('Digite o valor do angulo em graus-> '))
#sin, cos e tan mostra sua função em um angulo radianos
#a função degrees faz a conversão de radiano para graus
#a função radians faz a conversão de graus para radiano
ang_rad = radians(ang)
seno_ang = sin(ang_rad)
cosseno_ang = cos(ang_rad)
tangente_ang = tan(ang_rad)
print('O ângulo {}° possui:\nseno {:.2f}\ncosseno {:.2f}\ntangente {:.2f}'.format(ang, seno_ang, cosseno_ang, tangente_ang))
