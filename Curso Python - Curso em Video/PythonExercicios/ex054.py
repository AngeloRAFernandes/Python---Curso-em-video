'''Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date

atual = date.today().year
contc = 0
conta = 0

for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    if nasc + 21 < atual:
        contc += 1
    else:
        conta += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(contc))
print('E tambem tivemos {} pessoas menores de idade'.format(conta))
