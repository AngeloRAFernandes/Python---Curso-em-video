'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os
10 primeiros termos da progressão usando a estrutura while.'''

print('=' * 30)
print('{:^30}'.format('Gerador de PA'))
print('=' * 30)

n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

termo = n
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1

print('ACABOU')
