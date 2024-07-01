from datetime import date
print('{:=^25}'.format('Desafio41'))
"""
A confederação nacional de natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
- até 9 anos: mirim 
- até 14 anos: infantil
- até 19 anos: junior
- até 20 anos: senior
- acima: master
"""
idade = float(input('Digite o seu ano de nascimento -> '))
idade = date.today().year - idade
if idade <= 9:
    categoria = 'mirim'
elif idade <= 14:
    categoria = 'infantil'
elif idade <= 19:
    categoria = 'junior'
elif idade <= 20:
    categoria = 'senior'
else:
    categoria = 'master'
print('A categoria do atleta é:{}{}{}'.format('\033[32m', categoria, '\033[m'))
