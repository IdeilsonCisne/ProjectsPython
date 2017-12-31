print('{:*^40}'.format(' Conversor de Temperatura '))
celsius = float(input('Informe a temperatura em graus Celsius(ºC): '))
fahre = float(input('Informe a temperatura em graus Fahrenheit(ºF): '))
print('A temperatura de {:.1f}ºC vale {:.1f}ºF.\n'
      'A temperatura de {:.1f}ºF vale {:.1f}ºC.'.format(celsius, 1.8 * celsius + 32, fahre, (fahre - 32)/1.8))
