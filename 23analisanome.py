
nome = str (input('Digite o seu nome completo: ')).strip()
print('Seu nome em letras maiúscilas é {}'.format(nome.upper()))
print (' Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))