print('{:*^40}'.format(' Conversão Métrica '))
m = float(input('Digite um valor para conversão métrica: '))
print('{}m vale {:.0f}cm ou {:.0f}mm.'.format(m, (m * 100), (m * 1000)))