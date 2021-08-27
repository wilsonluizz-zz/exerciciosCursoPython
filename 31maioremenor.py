a = int(input('Diteige o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
#verificando quem é menor.

menor = a
if b< a and b<c:
    menor= b
if c<a and c<b:
    menor = c
print('O menor número entre {}, {} e {} é {}'.format(a,b,c,menor))
#verificando quem é maior
maior = a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior =c
print('O maior número entre {}, {} e {} é {}'.format(a,b,c,maior))