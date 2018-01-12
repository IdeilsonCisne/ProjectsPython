from math import sin, cos, tan, radians

print('{:*^40}'.format(' Seno, Cosseno e Tangente '))
an = float(input('Digite um valor de ângulo: '))
print('O angulo de {} tem SENO {:.3f}.\n'
      'O angulo de {} tem COSSENO {:.3f}.\n'
      'O angulo de {} tem TANGENTE {:.3f}'.format(an, sin(radians(an)),an, cos(radians(an)), an, tan(radians(an))))
