from datetime import date
print('{:=^25}'.format('Desafio39'))
"""
peça o usuario masculino a sua idade
-informe se : 'Você ainda vai se alistar, e quanto tempo falta'
-'é a hora de se alistar'
-'Já passou do tempo de se alistar, e quanto tempo passou do prazo'
"""
ano = float(input('Informe o seu ano de nascimento-> '))
idade = date.today().year - ano
saldo = 18 + ano
#condição de alistamento
if idade < 18:
    prazo = 18 - idade
    #verde
    print('\033[32mQuem nasceu em {} tem {} anos em {}'.format(ano, idade, date.today().year))
    print('\033[32mVocê ainda vai se alistar, espere {} ano(s)\033[m'.format(prazo))
elif idade == 18:
    prazo = idade
    #amarelo
    print('\033[33mQuem nasceu em {} tem {} anos em {}'.format(ano, idade, date.today().year))
    print('\033[33mÉ a hora de se alistar, fique atento para não perder o prazo\033[m')
else:
    prazo = idade - 18
    #vermelho
    print('\033[31mQuem nasceu em {} tem {} anos em {}'.format(ano, idade, date.today().year))
    print('\033[31mVocê perdeu o prazo de alistamento. Você está {} ano(s) atrasado\033[m'.format(prazo))
