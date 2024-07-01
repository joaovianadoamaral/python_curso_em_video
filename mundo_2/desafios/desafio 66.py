print('{:=^25}'.format('DESAFIO 66'))
"""
leia varios inteiros e quando o usuário digitar '999' voce para, use break
mostre a quantidade de números digitados.
mostre a soma entre eles
A soma dos {} valores é igual a {}
"""
soma = qntd = 0
while True:
    num = int(input('Digite um número inteiro ->> '))
    if num == 999:
        break
    soma += num
    qntd += 1
print(f'A soma dos {qntd} valores é igual a {soma} ')
