l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
ar = l * a
print('Sua parede tem a dimensão de {}X{} e sua área é de {}m²'.format(l, a, ar))
tinta = ar / 2
print('Para pintar todas as paredes, você precisa de {}l de tinta'.format(tinta))

