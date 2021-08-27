import math

co = float (input('Cumprimento do cateto oposto: '))
ca = float (input('Cumprimento do cateto adjacente: '))

hi = math.hypot(co,ca)
print (' A hipotenuza terá {:.2f}'.format(hi))
