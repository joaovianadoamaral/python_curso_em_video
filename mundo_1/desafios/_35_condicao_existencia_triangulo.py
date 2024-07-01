print('{:=^25}'.format('Desafio35'))
#leia tres lados de um triangulo e veja se ele existe
lad1 = float(input('Digite o lado 1 do triangulo -> '))
lad2 = float(input('Digite o lado 2 do triângulo -> '))
lad3 = float(input('Digite o lado 3 do triângulo -> '))
#com essa notação não é preciso especificar se um lado é negativo ou não
if abs(lad1 - lad2) < lad3 and abs(lad1 + lad2) > lad3:
    if abs(lad1 - lad3) < lad2 and abs(lad1 + lad3) > lad2:
        if abs(lad3 - lad2) < lad1 and abs(lad2 + lad3) > lad1:
            print('O triângulo existe')
else:
    print('O triângulo não exite')
