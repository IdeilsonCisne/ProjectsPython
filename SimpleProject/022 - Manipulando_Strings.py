print('{:*^40}'.format(' Manipulando Strings '))
nome = input('Digite seu nome completo: ')
nome2 = nome.split() #função split() - Cortar cada palavra e adiciona em uma lista
nome3 = ''.join(nome2) #função ''.join() - junta todas as palavras de uma lista
print('Seu nome em maiúsculas é: {}\n'
      'Seu nome em minúsculas é: {}\n'
      'Seu nome tem {} letras\n'
      'Seu primeiro nome é {} e tem {} letras'.format(nome.upper(), nome.lower(), len(nome3), nome2[0], len(nome2[0])))