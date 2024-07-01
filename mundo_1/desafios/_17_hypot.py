from math import hypot
#leia os catetos de um triangulo retangulo e descubra a hipotenusa.
print('{:=^25}'.format('desafio17'))
cadj = float(input('Digite a medida do cateto adjacente: '))
cop = float(input('Digite a medida do cateto oposto: '))
#hip = sqrt(cadj**2 + cop**2)
#hypot função que retorna a hipotenusa dando como parametros os catetos
hip = hypot(cadj, cop)
print('O valor da hipotenusa é-> {:.2f}'.format(hip))
