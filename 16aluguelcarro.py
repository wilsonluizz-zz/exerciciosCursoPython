print('-'*32)
print('Check out de locação de veículo')
print('-'*32)

dias = float(input('Você usou o veículo por quantos dias ?  '))
diaria = dias*60
quilometros = float(input('Quantos quilômetros você rodou com o veículo ? KM: '))
km = quilometros* 0.15

total = diaria+km

print ('O valor total a ser pago pelo aluguel é de R$ {:.2f} '.format(total))
