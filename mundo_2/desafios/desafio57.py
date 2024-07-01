print('{:=^25}'.format('Desafio 57'))
# Faça um programa que leia o sexo de uma pessoa 'm' ou 'f'
# não deixe que o programa aceite nada mais
#cores
vermelho = '\033[31m'
padrao = '\033[m'
azul = '\033[34m'
roxo = '\033[35m'
#programa
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite qual o seu sexo [M/F]-> ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('{}Opção ivalida! tente novamente{}'.format(vermelho, padrao))
if sexo == 'M':
    sexo = 'MASCULINO'
    print('O seu sexo é o {}{}{}'.format(azul, sexo, padrao))
else:
    sexo = 'Feminino'
    print('O seu sexo é o {}{}{}'.format(roxo, sexo, padrao))
