'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o
maior e o menor peso lidos.'''

menor = 0
maior = 0

for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        elif peso > maior:
            maior = peso

print('O maior peso lido foi de {:.1f}kg'.format(maior))
print('O menor peso lido foi de {:.1f}kg'.format(menor))
