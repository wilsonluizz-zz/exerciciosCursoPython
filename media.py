nota1 = float(input('Digite a nota do 1º bimestre: '))
nota2 = float(input('Digite a nota do 2º bimestre: '))
nota3 = float(input('Digite a nota do 3º bimestre: '))
nota4 = float(input('Digite a nota do 4º bimestre: '))
notafinal = (nota1+nota2+nota3+nota4)/4
if notafinal >=7:
    print ('Sua nota final foi {:.1f} parabéns você passou de ano!'.format(notafinal))
else: 
    notafinal <7
    print('sua nota final foi de {:.1f} você foi reprovado, estude mais da próxima vez'.format(notafinal))


    

