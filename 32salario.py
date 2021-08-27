salario = float(input('Digite o valor do seu salário para saber o valo do aumento: R$ '))
if salario <=1250:
    novo = salario + (salario*15/100)
else:
    novo = salario + (salario*10/100)
print('Com salário de R$ {:.2f} o seu novo salário passa a ser R$ {:.2f}'.format(salario,novo))
