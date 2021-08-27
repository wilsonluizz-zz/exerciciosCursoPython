import math
angulo = float (input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(angulo))
print(' O angulo de {} tem o seno {:.2f}'.format(angulo, seno))
coseno = math.cos(math.radians(angulo))
print ('O angulo de {} tem o coseno de {:.2f}'.format(angulo, coseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo,tangente))