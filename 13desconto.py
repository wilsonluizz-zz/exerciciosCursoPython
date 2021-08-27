produto = float(input('Digite o valor atual do produto: R$ '))
desconto = (produto/100) *5
novopreco = produto-desconto
print('o valor do produto com 5% de desconto é  R$ {:.2f} '.format(novopreco))