print('{:=^25}'.format('desafio15'))
#leia a quantidade de dias que o carro foi alugado e a quantidade de KM percorridos
#Calcule o preço a pagar pelo carro alugado sabendo que o carro custa R$60
#por dia e R$0,15 por Km rodado.
#logo y = 60*dias + .15 *km
dia = int(input('Digite quantos dias o carro foi alugado: '))
km = float(input('Digite quantos foram os km rodados: '))
preco = 60 * dia + .15 * km
print('O total a pagar pela locação do carro é: {:.2f}'.format(preco))
