# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta nescessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m2.

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))

area = largura * altura
tinta = area / 2

print('Sua parede tem uma área de {}m².'.format(area))
print('Você vai precisar de {}L de tinta para pintar a parede.'.format(tinta))
