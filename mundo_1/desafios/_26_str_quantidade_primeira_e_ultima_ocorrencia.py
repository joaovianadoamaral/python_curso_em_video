print('{:=^25}'.format('Desafio26'))
"""
faça um programa que leia uma frase pelo teclado e mostre:
*Quantas vezes aparece a letra 'a'
*Em que posição ela aparece pela primeira vez
*Em que posição ela parece da ultima vez
"""
frase = str(input('Digite uma frase -> ')).strip()
aux = ''.join(frase.upper().split())
#contagem de as
cont_a = aux.count('A')
#mostrar onde aparece o primeiro a
pri_a = aux.find('A')+1
#mostrar onde aparece o ultimo a
ult_a = aux.rfind('A')+1
print('Existem {} As'.format(cont_a))
print('O primeiro A aparece em: {}'.format(pri_a))
print('O último A aparece em: {}'.format(ult_a))
