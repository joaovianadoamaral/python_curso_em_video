print('{:=^25}'.format('Desafio 70'))
"""
Loja super baratao
leia o nome do produto e o preço varias vezes até o usuario quise sair
quer continuar?
a) mostra o total de preços
b) quantidade de produtos custando mais de 1000,00
c) o produto mais barato foi {} que custa {}
"""
# apresentação da loja
print('-'*30)
print('{:^30}'.format('Loja super baratao'))
print('-'*30)

# variaveis uteis
total = qntd = 0
aux = 0
while True:
    nome = str(input('O nome do produto ->> ')).strip().upper()
    preco = float(input('O preço do produto ->> '))
    # preço negativo
    if preco < 0:
        while preco < 0:
            preco = float(input('Opção inválida!\nO preço do produto ->> '))

    # quer continuar
    continuar = str(input('Quer continuar? [S/N] ->> ')).strip().upper()
    # opcao valida
    if continuar not in 'S N':
        while continuar not in 'S N':
            continuar = str(input('Opção iválida!\nQuer continuar? [S/N] ->> ')).strip().upper()

    # total da compra
    total += preco

    # produtos com mais de 1000 reais
    if preco > 1000:
        qntd += 1

    # produto mais barato
    if aux == 0:
        barato = preco
        nbarato = nome
        aux += 1
    elif preco < barato:
        barato = preco
        nbarato = nome

    if continuar == 'N':
        break
    else:
        continue

print('{:-^30}'.format('FIM DO PROGRAMA'))
# mostra os dados obtidos
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {qntd} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nbarato} que custa R${barato}')
