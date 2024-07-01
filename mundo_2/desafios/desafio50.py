print('{:=^25}'.format('Desafio 50'))
#leia 6 números inteiros, e faça a soma somente dos pares
soma = 0
for i in range(1, 7):
    num = int(input('Digite o {}° número inteiro: '.format(i)))
    #verifica se o número é par e realiza a soma
    if num % 2 == 0:
        soma += num
print('A soma dos números pares digitados é {}'.format(soma))
