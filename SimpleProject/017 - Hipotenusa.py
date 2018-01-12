from math import hypot
print('{:*^40}'.format("Comprimento da Hipotenusa"))
print('')
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
print('O comprimento da Hipotenusa do triangulo é: {:.2f}'.format(hypot(co, ca)))