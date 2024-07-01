desafio = 'desafio 65'
print(f'{desafio:=^25}')
"""
leia vários números inteiros pelo teclado.
pergunte a cada interação se o usuario deseja digitar mais números
ao fim do programa mostre a média, o maior e o menor.
"""
num = soma = qntd = 0
resposta = 's'
while resposta in 'S s':
    print('-=-' * 20)
    num = int(input('Digite um número ->> '))
    resposta = str(input('Deseja continuar [S/N] ->> '))
    print('-=-' * 20)
    # verifica se o usuario digitou certo
    if resposta not in 'S s N n ':
        while resposta not in 'S s N n':
            resposta = str(input('Opção inválida! deseja continuar [S/N] ->> ')).strip()
    # operação da soma para definir a média depois
    soma += num
    # define o maior e o menor
    if qntd == 0:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    # quantidade de números lidos
    qntd += 1
# mostrar a média, o maior e o menor
media = soma / qntd
print(f'A média dos inteiros é igual a {media}')
print(f'O maior número digitado é o {maior}')
print(f'O menor número digitado é o {menor}')
