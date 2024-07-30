'''A Confederação Nacional de Natação precisa de um programa que leia o
ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''

from datetime import date

ano = int(input('Ano de nascimento: '))

idade = date.today().year - ano

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    cla = 'MIRIN'
elif idade <= 14:
    cla = 'INFANTIL'
elif idade <= 19:
    cla = 'JÚNIOR'
elif idade <= 25:
    cla = 'SÊNIOR'
else:
    cla = 'MASTER'

print('Classificação: {}'.format(cla))
