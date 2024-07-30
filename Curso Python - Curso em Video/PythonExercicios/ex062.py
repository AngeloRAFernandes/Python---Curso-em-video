'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('=' * 30)
print('{:^30}'.format('Gerador de PA'))
print('=' * 30)

n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

termo = n
cont = 1
max = 10
while cont <= max:
    print('{} -> '.format(termo), end='')
    termo += r
    if cont == max:
        print('PAUSA')
        max += int(input('Quantos termos você quer mostrar a mais? '))
    cont += 1

print('Progressão foi finalizada com {} termos mostrados.'.format(max))
