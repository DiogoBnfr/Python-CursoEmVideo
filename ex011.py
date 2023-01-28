#  Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#  necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
lar = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = float(lar) * float(alt)
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(lar, alt, area))
tinta = area / 2
print('Para pintar sua parede você precisará de {}l de tinta.'.format(tinta))
