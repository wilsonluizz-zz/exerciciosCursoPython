salario= float(input('Digite o valor do seu salário atual: R$ '))
aumento = (salario/100)*15
novosalario = salario+aumento

print('Com o reajuste de 15% o seu salário que era de {:.2f}, com o reajuste de 15% passa a ser R$ {:.2f}'.format(salario,novosalario))