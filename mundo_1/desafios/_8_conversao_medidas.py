print('{:=^25}'.format('desafio08'))
#escreva um programa que leia o valor em metros, e converta para centimetros e milimetros
metro = float(input('digite o valor de medida em metros: '))
milimetro = metro*1000
centimetro = metro*100
decimetro = metro * 10
decametro = metro * .1
hectametro = metro * .01
kilometro = metro * .001
print('{:.2f} metros é equivalente a:\n{:.2f} milimetros\n{:.2f} centimetros\n{:.2f} decimetros \n{:.2f} decametros\n{:.2f} hectometros\n{:.2f} kilometros'.format(metro, milimetro, centimetro, decimetro, decametro, hectametro, kilometro))
