for c in range(1, 10):
    print(c)
print('Fim')
print('-=-'*20)
# mesma coisa com while
aux = 1
while aux < 10:
    print(aux)
    aux += 1
print('Fim')

print('-=-'*20)
# quando o usuario digitar 0 ele para (chamado de flag) ponto de parada
# com for não da para fazer isso
#precisa iniciar a variavel antes
n = 1
while n != 0:
    n = int(input('Digite um valor ( 0 para sair) -> '))
print('Fim')
print('-=-'*20)
resposta = 'S'
while resposta == 'S':
    resposta = str(input('quer continuar [S/N]')).strip().upper()
print('Fim')
