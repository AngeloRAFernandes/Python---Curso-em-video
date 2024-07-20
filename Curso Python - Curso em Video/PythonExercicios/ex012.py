# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço
# com 5% de desconto.

p = float(input('Digite o preço do produto: R$ '))

np = p - (p * (5/100))

print('O Preço do produto que custava R$ {:.2f} com 5% de desconto fica R$ {:.2f}'.format(p, np))
