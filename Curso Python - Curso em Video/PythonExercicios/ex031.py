"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas."""

distancia = float(input('Qual é a distância da sua viagem? '))

"""
if distancia <= 200:
    preço = distancia * 0.5
else:
    preço = distancia * 0.45
"""

preço = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print('Você está prestes a começar uma viagem de {:.1f}km'.format(distancia))
print('E o preço da sua passagem será R${:.2f}.'.format(preço))
