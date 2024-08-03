'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

print('-' * 30)
print(f'{'LOJA SUPER BARATÃO':^30}')
print('-' * 30)

total = maiorpreco = menorpreco = cont = 0
produtobarato = ' '

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))

    cont += 1
    total += preco

    if preco > 1000:
        maiorpreco += 1

    if cont == 1 or preco < menorpreco:
        menorpreco = preco
        produtobarato = produto

    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if esc == 'N':
        break

print(f'{' FIM DO PROGRAMA ':-^30}')
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {maiorpreco} produto custando mais de R$ 1,000.00')
print(f'O produto mais barato foi {produtobarato} que custa R$ {menorpreco:.2f}')
