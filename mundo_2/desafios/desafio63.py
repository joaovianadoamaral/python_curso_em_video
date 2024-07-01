desafio = 'desafio 63'
print(f'{desafio:=^25}')
"""
peça ao usuario um número inteiro n.
mostre os n primeiros termos da sequencia de fibonacci
os dois primeiros termos são iguais a 1.
os próximos termos são iguais a soma dos dois anteriores
"""
# leitura de quantidade de número da sequencia pelo usuario
num = int(input('Digite quantos números da sequencia de fibonacci você deseja --> '))
# condição para loop verdadeiro
if num <= 0:
    while num <= 0:
        print('opção invalida!! Tente de novo')
        num = int(input('->> '))
i = 0
n1 = 0
n2 = 1
n3 = n1 + n2
#loop para mostrar a sequencia
while i < num:
    # dois primeiros loops mostrar :
    if i == 0:
        print(f'{n1} -> ', end='')
    elif i == 1:
        print(f'{n2} ', end='')
    # próximos números da sequência
    else:
        # :, para ficar fácil de ler números altos
        print(f'-> {n3:,} ', end='')
        #muda a condição da soma
        n1 = n2
        n2 = n3
        n3 = n1 + n2
    i += 1
print('\nFim')
