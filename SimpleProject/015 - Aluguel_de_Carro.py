print('{:*^40}\n{}\n{}\n{}'.format(' Aluguel de Carros ','Valor por dia = R$60,00', 'Valor por KM Rodado = R$0,15', '*'*40))
dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
print('Valor a pagar: R${:.2f}'.format(dia * 60 + km * 0.15))
