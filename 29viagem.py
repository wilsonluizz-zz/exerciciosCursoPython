from time import sleep
viagem = int(input('Qual a distangia da viagem? KM: '))
if viagem <= 200:
    preco = viagem* 0.50
else :
    viagem>200 
    preco = viagem* 0.45
print('Calculando valor a ser cobrado pela viagem...')
sleep(2)

print('Sua viagem custará R${:.2f}'.format(preco))