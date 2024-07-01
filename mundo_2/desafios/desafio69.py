print('{:=^25}'.format('Desafio 69'))
"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário 
quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
b) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""
maioridade = homens = mmulher = 0
while True:
    # mensagem inicial
    print('-=-' * 12)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-=-' * 12)

    # ler idade e sexo
    idade = int(input('Idade ->> '))

    # verifica se digitou uma opção certa
    if idade < 0:
        while idade < 0:
            idade = int(input('Opção inválida!!\nIdade ->> '))

    # quantas pessoas tem mais de 18
    if idade > 18:
        maioridade += 1

    sexo = str(input('Sexo [M/F] ->> ')).strip()

    # verifica se digitou uma opcao certa
    if sexo.upper() not in 'F M':
        while sexo.upper() not in 'F M':
            sexo = str(input('Opção inválida!!\nSexo [M/F] ->> '))

    # quantos homens foram cadastrados
    if sexo.upper() == 'M':
        homens += 1

    # quantas mulheres tem menos de 20 anos
    if sexo.upper() == 'F' and idade < 20:
        mmulher += 1

    print('-=-'*12)

    # quer continuar?
    continuar = str(input('Quer continuar? [S/N] ->> ')).strip()

    # opcao valida
    if continuar.upper() not in 'S N':
        while continuar.upper() not in 'S N':
            continuar = str(input('Opção inválida!!\nQuer continuar? [S/N] ->> ')).strip()
    print('-=-'*12)
    if continuar.upper() == 'N':
        break
    # não precisa desse continue pq é a ultima linha do código mas pra ficar organizado
    else:
        continue

# mostra A) quantas pessoas tem mais de 18 anos.
print('{:=^25}'.format('FIM DO PROGRAMA'))
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mmulher} mulheres com menos de 20 anos')
