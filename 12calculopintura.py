altura= float(input('Digite a altura da parede m: '))
largura = float(input('Digite a largura da parede m: '))
mquadrado= altura*largura
rendimento = mquadrado/2

print('A parede possui {:.2f} m², \n logo para pintá-la são necessários {:.2f}L  de tinta'.format(mquadrado, rendimento))