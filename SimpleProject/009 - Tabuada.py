print('{:*^40}'.format(' Tabuada '))
n = int(input('Digite um número: '))
print('A tabuada de {} é: '.format(n))
for i in range(1, 11, 1):
    print('{:<2} x {:2} = {:2}'.format(n, i, (i * n)))