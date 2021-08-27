print('-=-'*10)
print('Analisafor de Triângulos')
print('-=-'*10)

reta1 = float(input('Digite o primeir segmento: '))
reta2 = float(input('Digite o segundo segmento: '))
reta3 = float(input('Digite o terceiro segmento: '))
if reta1< reta2+ reta3 and reta2< reta1+reta3 and reta3 < reta1+reta2:
    print( 'Os segmentos acima PODE FORMAR um Triângulo.')
else:
    print('Os segumento acima NÃO PODE FORMAR um Triângulo.')