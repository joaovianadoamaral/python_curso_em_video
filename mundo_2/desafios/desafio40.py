print('{:=^25}'.format('Desafio40'))
"""
Crie um programa que leia duas notas de um aluno e calcule
sua média. Mostrando uma mensagem no final, de acordo com a 
média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: aprovado
"""
not1 = float(input('Digite a 1° nota: '))
not2 = float(input('Digite a 2° nota: '))
media = (not1 + not2)/2
if media < 5:
    print('Aluno {}Reprovado.{}'.format('\033[31m', '\033[m'))
elif media >= 5 and media <= 6.9:
    print('Aluno em {}recuperação{}'.format('\033[33m', '\033[m'))
else:
    print('Aluno {}aprovado{}'.format('\033[32m', '\033[m'))
print('A média desse aluno foi: {}'.format(media))
