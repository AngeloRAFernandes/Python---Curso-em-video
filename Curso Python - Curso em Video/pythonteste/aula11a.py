print ('\033[1;31;43mOlá, Mundo!\033[m')
print ('\033[4;30;45mOlá, Mundo!\033[m')
print ('\033[30mOlá, Mundo!\033[m')
print ('\033[37mOlá, Mundo!\033[m')
print ('\033[7;30mOlá, Mundo!\033[m')
print ('\033[0;33;44mOlá, Mundo!\033[m')
print ('\033[7;33;44mOlá, Mundo!\033[m')


a = 3
b = 5

print('O valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))


nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))


nome1 = 'Guanabara'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome1, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome1, cores['limpa']))