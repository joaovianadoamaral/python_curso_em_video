print('{:=^25}'.format('Desafio 56'))
"""
leia o nome de 4 pessoas, idade e sexo [M/F]
mostre a média das idades 
a idade e o nome do homem mais velho
quantidade de mulheres com menos de 20 anos
"""
# variaveis importantes
homem_velho = ''
aux = 0

aux2 = 0
cont = 0
# laço for
for i in range(1, 5):
    print('-'*8, end='')
    print(' {}° PESSOA '.format(i), end='')
    print('-' * 8)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()

    # media das idades
    if i == 1:
        media = idade
    else:
        # realiza um somatório das idades para fazer a média fora do loop
        media += idade

    # idade e nome do homem mais velho
    if sexo == 'M' and aux == 0:
        # primeira vez digitado o nome de um homem
        homem_velho = nome
        maior_idade = idade
        aux += 1
    elif sexo == 'M' and aux != 0:
        if idade > maior_idade:
            homem_velho = nome
            maior_idade = idade
    # else não é homem, não precisa fazer nada

    # mulheres com — de 20 anos
    if sexo == 'F':
        if idade < 20:
            cont += 1
        aux2 += 1
media = media/4
print('A média de idade do grupo é de {} anos'.format(media))
# fazer algo caso não for digitado nenhum homem
if aux == 1:
    print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade, homem_velho.capitalize()))
else:
    print('Não existe homem mais velho')

# fazer algo caso não foi digitado nenhum nome feminino
if aux2 != 0:
    print('Ao todo são {} mulheres com menos de 20 anos'.format(cont))
else:
    print('Não existem mulheres')
