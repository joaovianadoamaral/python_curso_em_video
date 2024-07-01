for teste in range(0, 3):
    print(teste)
print('-'*20)
#ele recebe cada valor no intervalo na ordem da vez, mas não cria uma lista
print(teste)
# a variavel teste irá receber o ultimo valor da sequencia sendo range(a, b), b-1

#para 'b' menores que 'a' o programa não executa nenhuma vez por padrão
print('-'*20)
for teste in range(10, 8):
    print(teste)
print('Viu não aparece nada')
print('-'*20)
#para contagens além de +1 positivo use um terceiro parametro 'c' especificando de quanto em quanto se 'pula'
for teste in range (0, 13, 2):
    print(teste)
print('-'*20)
#podemos realizar uma contagem negativa usando o mesmo metodo
#para contagens negativas o range vai de 'a' a 'b+1' pulando 'c' vezes
for teste in range(12, 0, -2):
    print(teste)
