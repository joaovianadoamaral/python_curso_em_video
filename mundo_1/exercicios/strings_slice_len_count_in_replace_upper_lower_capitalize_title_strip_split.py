#exemplos de manipulação de texto
#o ragange pega o primeiro valor, começa nele, e
frase = 'Curso em video de Python'
frase_aux = frase
print(frase)
print('veja a notação frase[3] = {}'.format(frase[3]))
print('veja a notação frase[3:5] = {}'.format(frase[3:5]))
print('veja a notação frase[3:21:2] = {}'.format(frase[3:21:2]))
print('veja a notação frase[3:] = {}'.format(frase[3:]))
print('veja a notação frase[:3] = {}'.format(frase[:3]))
print('veja a notação frase[3::4] = {}'.format(frase[3::4]))
print('veja a notação frase[3] = {}'.format(frase[3]))
#analise
print('Veja o comprimento de frase: {}'.format(len(frase)))
print('Veja a contagem de Os minusculos dentro de frase: {}'.format(frase.count('o')))
#podemos mostrar count com intervalo usando frase.count('o',0,10) -> ele começa no 0 e termina no 9 (10 - 1)
print('Veja se existe (deo) na frase, sim? mostra o indice. não? mostra -1 === {}'.format(frase.find('deo')))
#caso houver mais de um (deo) na frase ele mostra somente o do primeiro indice
print('É verdade que existe (curso) em frase? {}'.format('curso' in frase))
#trasnformação
print('Veja a substituição de Android por Python: {}'.format(frase.replace('Python', 'Android')))
print('Veja a transformação da frase para maiuscula: {}'.format(frase.upper()))
print('Veja a transformação da frase para minusculas: {}'.format(frase.lower()))
print('Veja a transformação da frase para capitalizada: {}'.format(frase.capitalize()))
print('Veja a trasnformação da frase para title: {}'.format(frase.title()))
print('Veja a transformação da frase para strip(se houver): {}'.format(frase.strip()))
#pode-se adicionar r(right) e l(left) na frente de strip para eliminação seletivo do começo ou do fim
frase_aux.split()
print('Veja a transformação da frase para split: {}'.format(frase_aux))
'-'.join(frase_aux)
print('Veja a transformação da frase splitada com uma nova junção: {}'.format(frase_aux))
print('Veja a tranformação da frase mudada para upper e encontrar os nela :{}'.format(frase.upper().find('O')))
