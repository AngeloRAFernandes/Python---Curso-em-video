'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
 No final, mostre os 10 primeiros termos dessa progressão.'''

print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('=' * 30)

n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dec = n + (10 - 1) * r

for pa in range (n, dec + r, r):
        print('{} '.format(pa), end = '-> ')

print('ACABOU')
