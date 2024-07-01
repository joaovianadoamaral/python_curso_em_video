print('{:=^25}'.format('Desafio 49'))
#peça o usuario um número inteiro e mostre a ele a tabuada usando o laço for
num = int(input('Digite um número inteiro: '))
print('-=-'*15)
print('Taboada')
for aux in range(0, 11):
    resultado = num*aux
    print('{:<3} x {:<3} = {:<3}'.format(num, aux, resultado))
print('-=-'*15)
