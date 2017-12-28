print('{:*^40}'.format(' Calculando Descontos '))
valor = float(input('Digite um valor R$ '))
desconto = valor * 0.05
print('O valor R${} com desconto de 5% será R${:.2f}'.format(valor, valor - valor * 0.05))