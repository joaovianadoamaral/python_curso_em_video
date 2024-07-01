print('{:=^25}'.format('Desafio67'))
"""
faça um programa de tabuada até o número digitado pelo usuario for negativo
"""
while True:
    num = int(input('Você quer ver a tabuada de qual valor ->> '))
    print('-=-'*20)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num:^3} x {i:^3} = {num * i:^3}')
    print('-=-'*20)
print('Fim da tabuada!! Volte sempre')
