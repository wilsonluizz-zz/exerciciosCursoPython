import random
print('OLÁ MALU! DIGITE QUAIS OS NOMES VOCÊ QUER DAR PARA OS SEUS FILHOS COM O JUNIOR!')

n1 = str (input('Primeiro nome: '))
n2 = str (input('Segundo nome: '))
n3 = str (input ('terceiro nome: '))
n4 = str(input('quarto nome: '))
lista=[n1,n2,n3,n4]

escolhido = random.choice(lista)

print ('O nome do primeiro  filho de vocês será {}'.format(escolhido))