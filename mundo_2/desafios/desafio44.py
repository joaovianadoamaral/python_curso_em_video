print('{:=^25}'.format('Desafio 44'))
"""
Calcule o preço do produto considerando o preço normal e o método de pagamento:
- (1)A vista / cheque : 10% de desconto
- (2)A vista no cartão: 5% de desconto
- (3)Até 2x :preço normal
- (4)3 ou mais vezes:20% de juros
"""
metodo = int(input('Digite o método a ser pago: \n'
                   '(1)A vista / cheque : 10% de desconto\n'
                   '(2)A vista no cartão: 5% de desconto\n'
                   '(3)Até 2x :preço normal\n'
                   '(4)3 ou mais vezes:20% de juros\n'
                   '->> '))
valor = float(input('Digite o valor normal do produto: '))
#calculo do novo valor
if metodo == 1:
    npreco = .9 * valor
    print('O valor do produto passara de {}R${:.2f}{} para {}R${:.2f}{}, '
          'usando dinheiro/cheque'.format('\033[33m', valor, '\033[m', '\033[32m', npreco, '\033[m'))
elif metodo == 2:
    npreco = .95 * valor
    print('O valor do produto passara de {}R${:.2f}{} para {}R${:.2f}{}, '
          'a vista no cartão'.format('\033[33m', valor, '\033[m', '\033[32m', npreco, '\033[m'))
elif metodo == 3:
    npreco = valor
    parcela = npreco/2
    print('O valor do produto será de {}R${:.2f}{}, '
          'até 2x sem juros'.format('\033[33m', npreco, '\033[m'))
    print('Cada parcela será de {}R${:.2f}{}'.format('\033[33m', parcela, '\033[m'))
elif metodo == 4:
    qntd = int(input('Digite a quantidade de vezes: '))
    npreco = valor * 1.2
    parcela = npreco/qntd
    print('O valor do produto passara de {}R${:.2f}{} para {}R${:.2f}{}, '
          'usando 3x ou mais'.format('\033[32m', valor, '\033[m', '\033[31m', npreco, '\033[m'))
    print('Cada parcela será de {}R${:.2f}{}'.format('\033[33m', parcela, '\033[m'))
else:
    print('{}O metodo de pagamento é invalido{}'.format('\033[31m', '\033[m'))
