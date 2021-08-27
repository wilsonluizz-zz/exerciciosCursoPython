import random
from time import sleep

print('-=-'*20)
print('JODO DE ADIVINHAÇÃO PYTHON! ADIVINHE E VENÇA O JOGO.')
print('-=-'*20)
num2 = int(input('Em qual número eu estou pensando de 1 a 10 ? R: '))
print('Processando...')
sleep(1)

num = random.randint(1,10)
while num != num2 :
    print('Você ERROU! pensei no {} tente outra vez:'.format(num))
    num2= int(input('Em qual número eu estou pensando de 1 a 10 ? R: '))
    print('Processando...')
    sleep(2)
    num= random.randint(1,10)
if num == num2:
    print('VOCÊ VENCEU! PENSEI EXATAMENTE NO NÚMERO {}'.format(num2))
    print('FIM DE JOGO.')
