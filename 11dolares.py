real = float(input('Digite quantos reais você tem R$'))
dolar = float(input('Digite o valor atual da cotação do dolar: '))
res = real/dolar

print('com {:.2f} R$ você pode comprar {:.2f} US$.'.format(real, res))