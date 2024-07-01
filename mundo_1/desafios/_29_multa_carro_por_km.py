print('{:=^25}'.format('desafio29'))
"""
escreva um programa que leia a velocidade de um carro.
se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado. A multa vai custar R$7,00 por Km
acima do limite
"""
velocidade = float(input('Digite a sua velocidade -> '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite de velocidade permitido que é de 80 Km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança')
